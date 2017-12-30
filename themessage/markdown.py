import re

header_regex = re.compile('(#+)\s*(.*)')


def get_title(md):
    """
    get title of markdown text.
    It will be any header on first none empty line

    :param md:
    :return:
    """
    md_lines = md.strip().splitlines()
    if len(md_lines) == 0:
        return None

    first_line = md_lines[0].strip()
    match = header_regex.search(first_line)
    if match is None:
        return None
    return match.group(2)
