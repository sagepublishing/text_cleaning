def test_with_options(inStr: str, opts: list):
    return inStr[opts['num_letters_remove']:]
