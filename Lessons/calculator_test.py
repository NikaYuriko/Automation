import pytest

from calculator import Calculator

calculator = Calculator()

@pytest.mark.skip
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(4.5, 5.5)
    assert res == 10

def test_sum_zer_nums():
    calculator = Calculator()
    res = calculator.sum(0, 9)
    assert res == 9

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)

    



# проверка сложения: 
# положительные числа, 
# отрицательные числа, 
# положительное+отрицательное, 
# числа с запятой,
# сложение с нулем

# res = calculator.sum(4, 5)
# assert res == 9

# res = calculator.sum(-6, -10)
# assert res == -16

# res = calculator.sum(6, -6)
# assert res == 0

# res = calculator.div(10, 2)
# assert res == 5


# res = calculator.sum(5.6, 4.3)
# res = round(res, 1)
# assert res == 9.9

# res = calculator.sum(10, 0)
# assert res == 10

# numbers = []
# res = calculator.avg(numbers)
# assert res == 0


# res = calculator.div(10, 0)
# assert res == None
