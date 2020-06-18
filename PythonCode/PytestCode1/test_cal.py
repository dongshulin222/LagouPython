import pytest
import yaml


class TestCal:
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["multiply"])
    @pytest.mark.parametrize('a,b,r', yaml.safe_load(open('CalData_Div.yml', encoding='utf-8')))
    def check_div(self, calculator_start, a, b, r, cmdoption):
        print(f"{cmdoption}")
        r = ("%.2f" % r)
        assert r == calculator_start.div(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    @pytest.mark.parametrize('a,b,r', yaml.safe_load(open('CalData_Add.yml', encoding='utf-8')))
    def test_add(self, calculator_start, a, b, r, cmdoption):
        print(f"{cmdoption}")
        r = ("%.2f" % r)
        assert r == calculator_start.add(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='multiply')
    @pytest.mark.parametrize('a,b,r', yaml.safe_load(open('CalData_Multiply.yml', encoding='utf-8')))
    def test_multiply(self, calculator_start, a, b, r, cmdoption):
        print(f"{cmdoption}")
        r = ("%.2f" % r)
        assert r == calculator_start.multiply(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["add"])
    @pytest.mark.parametrize('a,b,r', yaml.safe_load(open('CalData_Sub.yml', encoding='utf-8')))
    def check_sub(self, calculator_start, a, b, r, cmdoption):
        print(f"{cmdoption}")
        r = ("%.2f" % r)
        assert r == calculator_start.sub(a, b)
