import ast
import sys
from io import BytesIO
from token import COMMENT, ENCODING, INDENT, NEWLINE, OP
from tokenize import tokenize, untokenize


def add_tokens_around(line):
    start = True
    spaces = ""  # stores indentation
    result = []
    tokens = tokenize(BytesIO(line.encode("utf-8")).readline)
    for token in tokens:
        if token.type == ENCODING:
            result.append((token.type, token.string))
            continue
        elif token.type == INDENT:
            result.append((token.type, token.string))
            spaces += token.string
            continue
        elif start:
            result.append((OP, ("(")))
            result.append((token.type, token.string))
            start = False
        elif token.type in (COMMENT, NEWLINE):
            result.append((OP, (")")))
            result.append((token.type, token.string))
        else:
            result.append((token.type, token.string))
    return spaces + untokenize(result).decode("utf-8")


def wrap_walrus_assignment(lines):
    code = "".join(lines)
    # If original code does not raise SyntaxError
    # there is no need to modify it
    try:
        ast.parse(code)
    except SyntaxError as e:
        original_exception = e
    else:
        return lines

    new_lines = []
    # For each line with walrus, add ()
    for line in lines:
        if ":=" in line:
            new_lines.append(add_tokens_around(line))
        else:
            new_lines.append(lines)

    new_code = "".join(new_lines)

    try:
        ast.parse(new_code)
    except SyntaxError:
        raise original_exception from None
    else:
        return new_lines


def load_ipython_extension(ipython):
    if sys.version_info >= (3, 8):
        ipython.input_transformers_post.append(wrap_walrus_assignment)
    else:
        print(
            (
                "Python {}.{} is too old. Walrus operator is available ",
                "since Python 3.8".format(*sys.version_info[:2]),
            )
        )


def unload_ipython_extension(ipython):
    try:
        ipython.input_transformers_post.remove(wrap_walrus_assignment)
    except ValueError:
        pass
