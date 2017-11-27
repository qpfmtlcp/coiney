from crawler.loaders import replace_useless_chars


def test_replace_useless_chars():
    text = '''
        test \n
        some content \n
        \n\r\t
        \r\n
        test \r\tcontent
        \n\xa0
    '''
    
    expected = '''
        test \n
        some content \n
        \n
        \n
        test content
        \n
    '''
    assert replace_useless_chars(text) == expected
