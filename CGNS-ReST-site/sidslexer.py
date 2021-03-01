# CGNS Documentation files
# See LICENSING/COPYRIGHT at root dir of this documentation sources
#
import re
from pygments.lexer import RegexLexer, bygroups, words, using, this
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation


class SidsLexer(RegexLexer):
    """
    Lexer for CGNS SIDS description.

    .. versionadded:: 1.0
    """
    name = 'Sids'
    aliases = ['sids', 'cgns']
    filenames = ['*.sids']
    mimetypes = ['application/sids',
                 'application/cgns']


    operators = (
        ";;", "=", "=.", "!=" "==", ":=", "->", ":>", "/.", "+", "-", "*", "/",
        "^", "&&", "||", "!", "<>", "|", "/;", "?", "@", "//", "/@", "@@",
        "@@@", "~~", "===", "&", "<", ">", "<=", ">=", "×",
    )

    punctuation = (",", ";", "(", ")", "[", "]", "{", "}", "...", ".")

    def _multi_escape(entries):
        return '(%s)' % ('|'.join(re.escape(entry) for entry in entries))

    tokens = {
        'root': [
            (r'!(\n|[\w\W]*?[^\\]\n)', Comment.Single),
            (r'(?s)\(\*.*?\*\)', Comment),

            (r'([a-zA-Z]+[A-Za-z0-9]*`)', Name.Namespace),
            (r'([A-Za-z0-9]*_t)', Keyword.Type),
            #(r'([A-Za-z0-9]*_+[A-Za-z0-9]*)', Name.Variable),
            (r'#\d*', Name.Variable),
            (r'(int|real|char|bit)\b', Keyword.Type),
            (words(('do', 'else', 'for',
                    'if', 'return', 'while',
                    'List', 'Enumeration', 'Data', 'LogicalLink', 'Identifier'),
                   suffix=r'\b'), Keyword),
            (r'\([ro](:[ro])*\)', Keyword.Reserved),
            (r'\(o/d\)', Keyword.Reserved),
            (r'([a-zA-Z]+[a-zA-Z0-9]*)', Name),
            (r'([A-Za-z]*_[0-9]*)', Name),

            (r'-?\d+\.\d*', Number.Float),
            (r'-?\d*\.\d+', Number.Float),
            (r'-?\d+', Number.Integer),

            (words(operators), Operator),
            (words(punctuation), Punctuation),
            (r'".*?"', String),
            (r'\s+', Text.Whitespace),
            # function declarations
           # (r'((?:[\w*\s])+?(?:\s|[*]))'  # return arguments
           #  r'([a-zA-Z_]\w*)'  # method name
           #  r'(\s*\[[^;]*?\])'  # signature
           #  r'([^;]*)(;)',
           #  bygroups(using(this), Name.Function, using(this), using(this),
           #           Punctuation))
        ],
    }

# --- last line
