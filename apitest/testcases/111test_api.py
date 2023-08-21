import requests
import jsonpath as jsonpath
import re
import pytest

from common.yaml_util import write_yaml, read_yaml, read_yaml_testcase


# requests.post()
# requests.get()
# requests.delete()
# requests.put()


class TestApi:
    @pytest.mark.parametrize("caseinfo",read_yaml_testcase("testcases/test_api.yaml"))
    def test_get_token(self,caseinfo):
        write_yaml({"name":"张三"})
        print(caseinfo)
        # urls = "https://api.weixin.qq/cig-bin/token"
        # datas = {
        #     "grant_type":"client_credential",
        #     "appid":"wx8a9de038e93f77ab",
        #     "secret":"8326fc915928dee3165720c910effb86"
        # }
        # head = {'connection':'close'}
        # # res = TestApi.sess.request("get",url=urls,headers=head,params=datas)
        # # # lis = jsonpath.jsonpath(res.json(),"$.access_token")
        # # TestApi.access_token = res.json()["access_token"]
        # print(TestApi.access_token)

    # #查询标签接口
    # def test_select_flag(self):
    #     print(read_yaml("name"))
    #     urls = "https://api.weixin.qq.com/cgi-bin/tags/get"
    #     datas ={
    #         "access_token":TestApi.access_token
    #     }
    #     res = TestApi.sess.request("get",url=urls,params=datas)
    #     print(res.json())
    #
    # #编辑标签接口
    # def test_edit_flag(self):
    #     urls = "https://api.weixin.qq.com/cgi-bin/tags/upload"
    #     datas1 = {
    #         "access_token": TestApi.access_token
    #     }
    #     datas2 = {"tag":{"id":134,"name":"广东人"}}
    #     res = TestApi.sess.request("post",url=urls,json=datas2,params=datas1)
    #     print(res.json())
    #

    #
    # #访问php首页接口
    # @pytest.mark.smoke
    # def test_homepage_php(self):
    #     urls = "https://47.107.116.139/phpwind/"
    #     res = TestApi.sess.request("get",url=urls)
    #     TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"',res.text).group(1)
    #     print(TestApi.csrf_token)
    #
    #
    # #登录接口
    # def test_login(self):
    #     urls = "https://47.107.116.139/phpwind/"
    #     header = {
    #         "Accept":"application/json,text/javascript,/; q=0.01",
    #         "as4dq2we":"123456"
    #     }
    #     datas = {
    #         "username":"zs",
    #         "password":"1234546",
    #         "csrf_token":TestApi.csrf_token,
    #         "burl":"https://wwww.baidu.com",
    #         "invite":""
    #
    #     }
    #     res = TestApi.sess.request("post",url=urls,headers=header,data=datas)
    #     print(res.json())

# if __name__ == '__main__':
#     TestApi().test_get_token()
#     TestApi().test_select_flag()
#     TestApi().test_edit_flag()
#     TestApi().test_files_upload()






