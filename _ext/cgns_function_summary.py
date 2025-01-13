from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from sphinx.addnodes import pending_xref
from pathlib import Path

class CGNSExtractDoxygenFunctionsDirective(SphinxDirective):
    required_arguments = 1  # Argument for group name
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        # Get the group name from the directive argument
        group_name = self.arguments[0]
        xml_file = f"group__{group_name}.xml"
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
        # The name we want to display
        group_name_display_text = ''.join([' ' + char if char.isupper() and
                                           i > 0 else char for i, char in
                                           enumerate(group_name)])
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
                func_paragraph += nodes.Text(" - ⚠️ No description "
                                             "provided.")
            func_item += func_paragraph
            sublist += func_item

        # Add the sublist to the group item
        group_item += sublist
        bullet_list += group_item

        return [bullet_list]

    def _extract_functions(self, file_path):
        """
        Scan the XML file and extract function names and descriptions.
        """
        functions = []
        with file_path.open("r") as file:
            func_name = None
            func_desc = None
            inside_brief = False
            buffer = []  # Buffer for handling multi-line <para> content

            for line in file:
                # Look for function name
                if "<name>" in line:
                    # Name found without brief description
                    if func_name is not None:
                        functions.append((func_name, ""))
                    # Issue warning if inside brief
                    if inside_brief:
                        self.state_machine.reporter.warning(
                            "Invalid XML structure: <name> tag found inside "
                            "<briefdescription>.  This indicates a malformed "
                            "XML file.  Previous description discarded.",
                            line=self.lineno)
                        inside_brief = False
                    func_name = self._extract_tag_content(line, "name")

                # Detect start of <briefdescription>
                elif "<briefdescription>" in line:
                    if inside_brief:
                        warning = self.state_machine.reporter.warning(
                            "Invalid XML structure: found nested "
                            "<briefdescription>.  This indicates a malformed "
                            "XML file.",
                            line=self.lineno)
                    if func_name is None:
                        warning = self.state_machine.reporter.warning(
                            "Invalid XML structure: found <briefdescription> "
                            "without function name.  This indicates a "
                            "malformed XML file.",
                            line=self.lineno)
                    inside_brief = True
                    buffer = []

                # Detect end of <briefdescription>
                elif "</briefdescription>" in line:
                    if not inside_brief:
                        warning = self.state_machine.reporter.warning(
                            "Invalid XML structure: found </briefdescription> "
                            "before <briefdescription>.  This indicates a "
                            "malformed XML file.",
                            line=self.lineno)
                    elif func_name is None:
                        warning = self.state_machine.reporter.warning(
                            "Invalid XML structure: found </briefdescription> "
                            "without function name.  This indicates a "
                            "malformed XML file.",
                            line=self.lineno)
                    else:
                        # Extract the brief description from buffered <para>
                        # content
                        func_desc = self._extract_tag_content("".join(buffer),
                                                              "para")
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

    def _extract_tag_content(self, text, tag):
        """
        Extract content between <tag> and </tag>, handling multi-line tags.
        """
        start = text.find(f"<{tag}>")
        end = text.find(f"</{tag}>")
        if start != -1 and end != -1:
            return text[start + len(f"<{tag}>") : end].strip()
        return ""

def setup(app):
    app.add_directive("cgns-group-function-summary",
                      CGNSExtractDoxygenFunctionsDirective)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
