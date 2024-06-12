import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""


def test_capitalize():
    """POSITIVE"""
    assert utils.capitilize("string") == "String"
    assert utils.capitilize("1234") == "1234"
    assert utils.capitilize("10 июня 2024") == "10 июня 2024"
    assert utils.capitilize("10 June 2024") == "10 June 2024"
    assert utils.capitilize("строка12345") == "Строка12345"
    assert utils.capitilize("string12345") == "String12345"

    """NEGATIVE"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("1234строка") == "1234строка"

"""trim"""


def test_trim():
    """POSITIVE"""
    assert utils.trim(" string") == "string"
    assert utils.trim(" string ") == "string "
    assert utils.trim(" string 1234 ") == "string 1234 "
    """NEGATIVE"""
    assert utils.trim("") == ""


@pytest.mark.xfail()
def test_trim_with_mumbers_input():
    assert utils.trim(1234) == "1234"


@pytest.mark.xfail()
def test_trim_with_space_input():
    assert utils.trim(" string ") == " string "


"""to list"""


@pytest.mark.parametrize('string, delimeter, result', [
    # POSITIVE
    ("картошка,морковь,лук", ",", ["картошка", "морковь", "лук"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    # NEGATIVE
    ("", None, []),
    ("1,2,3,4 5", ",", ["1", "2", "3", "4 5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


"""contains"""


@pytest.mark.parametrize('string, symbol, result', [
    ("банан", "б", True),
    ("холодная зима", " ", True),
    ("диван-кровать", "-", True),
    ("09091994", "4", True),
    ("Москва", "м", False),
    ("привет", "з", False),
    ("", "p", False),
    ("123", "h", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


"""delete_symbol"""


@pytest.mark.parametrize('string, symbol, result', [
    ("банан", "б", "анан"),
    ("гвоздь", "д", "гвозь"),
    ("диван кровать", " ", "диванкровать"),
    ("145", "1", "45"),
    ("Москва", "", "Москва"),
    ("привет", "з", "привет"),
    ("", "p", ""),
    ("", "", ""),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


"""starts_with"""


@pytest.mark.parametrize('string, symbol, result', [
    ("апельсин", "а", True),
    ("", "", True),
    ("bed", "b", True),
    ("09091994", "0", True),
    ("Чехов", "ч", False),
    ("привет", "П", False),
    ("", "@", False),
    ("карта", "о", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""end_with"""


@pytest.mark.parametrize('string, symbol, result', [
    ("банан", "н", True),
    ("", "", True),
    ("divan", "n", True),
    ("145", "5", True),
    ("Москва ", "", True),
    ("привет", "л", False),
    ("", "@", False),
    ("дверь", "Ь", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


"""is_empty"""


@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("рыба", False),
    ("09091994", False),
    (" Чехов", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_string"""


@pytest.mark.parametrize('lst, joiner, result', [
    (["s", "o", "s"], ".", "s.o.s"),
    (["н", "о", "с"], "", "нос"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    ([], None, ""),
    ([], ",", ""),
    ([], "кот", ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
