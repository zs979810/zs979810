import pytest
import requests

from common.requrest_util import RequestUtil
from common.yaml_util import read_yaml, read_yaml_testcase

# requests.post()
class Test_api_weixin():

    # @pytest.mark.parametrize("caseinfo",read_yaml_testcase("testcases/test_selectflag.yaml"))
    # def test_get_AccessToken(self,caseinfo):
    #     method = caseinfo["request"]["method"]
    #     urls = caseinfo["request"]["url"]
    #     # json = caseinfo["request"]["json"]
    #     res = RequestUtil().send_all_request(method=method,url=urls)
    #     print(res.json())

    @pytest.mark.parametrize("caseinfo", read_yaml_testcase("testcases/test_api.yaml"))
    def test_login(self, caseinfo):
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]

