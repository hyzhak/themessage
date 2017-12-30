def get_header(md):
    md_lines = md.strip().splitlines()
    first_line = md_lines[0].strip()
    if first_line[:2] == '# ':
        return first_line[2:]
    return None
