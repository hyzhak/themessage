from themessage import markdown


def test_get_header_of_md_with_header():
    md = '# Header !\n' \
         'some additional text\n' \
         '# blah-blah-blah\n' \
         'Hello World!'

    assert markdown.get_header(md) == 'Header !'


def test_get_header_of_emtpy_md_is_none():
    assert markdown.get_header('') is None
