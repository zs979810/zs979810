import pytest

from common.yaml_util import clear_yaml


@pytest.fixture(scope="function",autouse=True)
def send_mes(request):
    clear_yaml()
    print("清空了yaml文件")
    yield
    print("接口请求结束")