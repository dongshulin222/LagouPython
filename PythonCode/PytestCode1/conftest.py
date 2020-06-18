from typing import List
import pytest
import yaml

import PythonCode.PytestCode1.Calculator


@pytest.fixture(autouse=True)
def calculator_start():
    print("--------计算开始--------")
    calc = PythonCode.PytestCode1.Calculator.Calc()
    yield calc
    print("--------计算结束--------")


def pytest_addoption(parser):
    mygroup = parser.getgroup("dongshulin")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取test环境数据")
        with open("TestDatas/test/testdata.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print("获取dev环境数据")
        with open("TestDatas/dev/devdata.yml") as f:
            datas = yaml.safe_load(f)
    else:
        print("获取st环境数据")
        with open("TestDatas/st/stdata.yml") as f:
            datas = yaml.safe_load(f)
    return datas


# 用例名称根据acsii排序
# def pytest_collection_modifyitems(session, config, items):
#     items.sort(key=lambda x: x.name)
# 解码
# for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')