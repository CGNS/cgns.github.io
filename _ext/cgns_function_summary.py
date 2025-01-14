from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from sphinx.addnodes import pending_xref
from pathlib import Path
import re

class CGNSExtractDoxygenFunctionsDirective(SphinxDirective):
    """
    A Sphinx directive to extract function names and their brief descriptions
    from Doxygen-generated XML files. The extracted information is displayed as
    a nested bullet list in the documentation.

    Arguments:
        group_name (str): The name of the group, used to locate the
            corresponding Doxygen XML file. This is the first required argument.
            The group_name is the same as used for the doxygengroup directive.
            The XML file is expected to be at xml/group__{group_name} where
            any underscores in group_name are repeated (so they appear twice).
            A link is expected elsewhere in the rst file with the format
            .. _{group_name}-ref:
        group_name_display_text (str, optional): A custom display text for the
            group name in the generated documentation. If not provided, a
            formatted version of `group_name` is used.

    Usage:
        .. cgns-group-function-summary:: DataArrays

            The group name is formatted as Data Arrays.  The xml file is
            xml/group__DataArrays.xml.

        .. cgns-group-function-summary:: CGNSFile Opening and Closing a CGNS File

            The group name is Opening and Closing a CGNS File.  The xml file is
            xml/group__CGNSFile.xml.
    """
    required_arguments = 1  # Argument for group name
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        # Get the group name from the directive argument
        group_name = self.arguments[0]
        xml_file = f"group__{group_name.replace('_', '__')}.xml"
        full_path = Path(self.env.app.confdir) / 'xml' / xml_file

        # Check if the XML file exists
        if not full_path.exists():
            error = self.state_machine.reporter.error(
                f"File not found: {xml_file}",
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]

        # Extract function names and descriptions
        functions = self._extract_functions(full_path)

        # Create a bullet list node for the group
        bullet_list = nodes.bullet_list()

        # Create the main list item for the group name
        group_item = nodes.list_item()
        group_paragraph = nodes.paragraph()

        # Add the group name as a reference
        group_ref = pending_xref('', refdomain='std', reftype='ref',
                                 reftarget=f"{group_name.lower()}-ref",
                                 refexplicit=True)
        # Format the group name for display by adding a space before each
        # capital letter after the first.
        group_name_display_text = (
            self.arguments[1] if len(self.arguments) > 1 else ''.join(
                [' ' + char if char.isupper() and i > 0 else char
                 for i, char in enumerate(group_name)]))
        group_ref += nodes.Text(group_name_display_text)
        group_paragraph += group_ref
        group_item += group_paragraph

        # Create a sublist for the functions
        sublist = nodes.bullet_list()

        for func_name, func_desc in functions:
            # Create a list item for each function
            func_item = nodes.list_item()
            func_paragraph = nodes.paragraph()

            # Create a cross-reference node for :cpp:func:
            xref = pending_xref('', refdomain='cpp', reftype='func',
                                reftarget=func_name, refexplicit=True)
            xref += nodes.literal('', func_name)
            func_paragraph += xref
            if func_desc:
                func_paragraph += nodes.Text(f" - {func_desc}")
            else:
                func_paragraph += nodes.Text(
                    " - ⚠️ No description provided.")
            func_item += func_paragraph
            sublist += func_item

        # Add the sublist to the group item
        group_item += sublist
        bullet_list += group_item

        return [bullet_list]

    def _extract_functions(self, file_path: Path) -> list[tuple[str, str]]:
        """
        Scan the XML file and extract function names and descriptions.
        Only considers <name> and <briefdescription> tags within a
        <memberdef kind="function"> block.
        """
        functions = []
        with file_path.open("r") as file:
            func_name = None
            func_desc = None
            inside_brief = False
            inside_func = False
            buffer = []  # Buffer for handling multi-line <para> content

            for line in file:
                # Detect start of <memberdef kind="function">
                if '<memberdef kind="function"' in line:
                    inside_func = True

                # Process content only if inside a function definition
                elif inside_func:
                    # Detect end of </memberdef>
                    if '</memberdef>' in line:
                        inside_func = False

                    # Look for function name
                    elif "<name>" in line:
                        # Name found without brief description
                        if func_name is not None:
                            functions.append((func_name, ""))
                        # Issue warning if inside brief
                        if inside_brief:
                            self.state_machine.reporter.warning(
                                "Invalid XML structure: <name> tag found "
                                "inside <briefdescription>.  This indicates a "
                                "malformed XML file.  Previous description "
                                "discarded.",
                                line=self.lineno)
                            inside_brief = False
                        func_name = self._extract_tag_content(line, "name")

                    # Detect start of <briefdescription>
                    elif "<briefdescription>" in line:
                        if inside_brief:
                            self.state_machine.reporter.warning(
                                "Invalid XML structure: found nested "
                                "<briefdescription>.  This indicates a "
                                "malformed XML file.",
                                line=self.lineno)
                        if func_name is None:
                            self.state_machine.reporter.warning(
                                "Invalid XML structure: found "
                                "<briefdescription> without function name.  "
                                "This indicates a malformed XML file.",
                                line=self.lineno)
                        inside_brief = True
                        buffer = []

                    # Detect end of <briefdescription>
                    elif "</briefdescription>" in line:
                        if not inside_brief:
                            self.state_machine.reporter.warning(
                                "Invalid XML structure: found "
                                "</briefdescription> before "
                                "<briefdescription>.  This indicates a "
                                "malformed XML file.",
                                line=self.lineno)
                        elif func_name is None:
                            self.state_machine.reporter.warning(
                                "Invalid XML structure: found "
                                "</briefdescription> without function name.  "
                                "This indicates a malformed XML file.",
                                line=self.lineno)
                        else:
                            # Extract the brief description from buffered <para>
                            # content
                            func_desc = self._extract_tag_content(
                                "".join(buffer), "para")
                            functions.append((func_name, func_desc or ""))
                        inside_brief = False
                        func_name = None
                        func_desc = None

                    # Collect lines inside <briefdescription>
                    elif inside_brief:
                        buffer.append(line)

            # If we ended with a name and no description, save the name
            if func_name is not None:
                functions.append((func_name, ""))

        return functions

    def _extract_tag_content(self, text: str, tag: str) -> str:
        """
        Extract content between <tag> and </tag>, handling multi-line tags.
        Removes any nested tags found within the extracted content.
        """
        start = text.find(f"<{tag}>")
        end = text.find(f"</{tag}>")
        if start != -1 and end != -1:
            content = text[start + len(f"<{tag}>") : end].strip()
            # Remove any nested tags
            content = re.sub(r"<[^>]+>", "", content)
            return content
        return ""

def setup(app):
    app.add_directive("cgns-group-function-summary",
                      CGNSExtractDoxygenFunctionsDirective)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
