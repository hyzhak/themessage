from themessage import markdown


def test_header_of_md_with_header_is_header():
    md = '# A Vision in a Dream.\n' \
         'In Xanadu did Kubla Khan\n' \
         'A stately pleasure-dome decree:\n' \
         'Where Alph, the sacred river, ran\n' \
         'Through caverns measureless to man\n' \
         '    Down to a sunless sea.\n' \
         '# The End'

    assert markdown.get_header(md) == 'A Vision in a Dream.'


def test_header_of_an_empty_md_is_none():
    assert markdown.get_header('') is None


def test_header_of_an_md_without_header_on_start_is_none():
    md = 'So twice five miles of fertile ground\n' \
         'With wa\'lls and towers were girdled round:\n' \
         'And there were gardens bright with sinuous rills,\n' \
         'Where blossomed many an incense-bearing tree;\n' \
         'And here were forests ancient as the hills,\n' \
         'Enfolding sunny spots of greenery.\n'
    assert markdown.get_header(md) is None
