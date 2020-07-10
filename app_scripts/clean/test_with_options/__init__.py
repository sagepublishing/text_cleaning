def test_with_options(inStr: str, opts: dict):
    return inStr[opts['num_letters_remove']:], {'my_metadata': 'Hello'}
