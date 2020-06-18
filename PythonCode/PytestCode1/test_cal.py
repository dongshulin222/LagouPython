import pytest
import yaml


class TestCal:
    @pytest.mark.parametrize('a,b,r', yaml.safe_load(open('CalData_Add.yml', encoding='utf-8')))
    def test_add(self, calculator_start, a, b, r):
        assert r == calculator_start.add(a, b)

    @pytest.mark.parametrize('a,b,r', yaml.safe_load(open('CalData_Sub.yml', encoding='utf-8')))
    def test_sub(self, calculator_start, a, b, r):
        assert r == calculator_start.sub(a, b)

    @pytest.mark.parametrize('a,b,r', yaml.safe_load(open('CalData_Multiply.yml', encoding='utf-8')))
    def test_multiply(self, calculator_start, a, b, r):
        assert r == calculator_start.multiply(a, b)

    @pytest.mark.parametrize('a,b,r', yaml.safe_load(open('CalData_Div.yml', encoding='utf-8')))
    def test_div(self, calculator_start, a, b, r):
        assert r == calculator_start.div(a, b)