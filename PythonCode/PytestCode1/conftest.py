import pytest
import PythonCode.PytestCode1.Calculator


@pytest.fixture(autouse=True)
def calculator_start():
    print("--------计算开始--------")
    calc = PythonCode.PytestCode1.Calculator.Calc()
    yield calc
    print("--------计算结束--------")
