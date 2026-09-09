from solution import convert


def test_single_symbol():
    assert convert("I") == 1
    assert convert("V") == 5


def test_repeated_symbols():
    assert convert("II") == 2
    assert convert("III") == 3


def test_added_symbols():
    assert convert("VI") == 6
    assert convert("XVI") == 16


def test_subtractive_notation():
    assert convert("IV") == 4
    assert convert("IX") == 9


def test_combined_subtractive():
    assert convert("XIX") == 19


def test_tens_and_hundreds_subtractive():
    assert convert("XL") == 40
    assert convert("XC") == 90