# coding:utf-8
import json
import requests
import unittest
from ssid import ssidx

ssid = ssidx()
class corp_fundmanager(unittest.TestCase):
    '''私募机构'''
    def setUP(self):
        pass

    @property
    def headers(self):
        return {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Content-Type": "application/json, text/plain, */*",
            "Host": "api.jdbtest.hffss.com",
            "oid": "obgs71WOxNmem_hMWqxBWwOtEstc",
            "sid": ssid,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
        AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
        wechatdevtools/1.02.1901230 MicroMessenger/6.7.3 Language/zh_CN \
        webview/15561554780482248 webdebugger port/55904"
        }

    def test1_type(self):
        '''搜索类型'''
        url = 'https://api.jdb.hffss.com//attent/corpids/list'
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps({}))
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')

    def test2_hot(self):
        '''热门搜索'''
        url = 'https://api.jdb.hffss.com/corp/orghotwords'
        r = requests.post(
            url=url,
            data=json.dumps({}),
            headers=self.headers)
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')

    def test3_search(self):
        '''机构搜索'''
        url = 'https://api.jdb.hffss.com/corp/search'
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "api.jdb.hffss.com",
            "oid": "obgs71WOxNmem_hMWqxBWwOtEstc",
            "Origin": "https://jdb.hffss.com",
            "rb": "%7B%22type%22%3A0%2C%22ccsstart%22%3A%22%22%2C%22ccsend%22%3A%22%22%2C%22keyword%22%3A%22%u6052%u5929%22%2C%22page%22%3A1%2C%22provinces%22%3A%5B%5D%2C%22officepros%22%3A%5B%5D%2C%22edatestart%22%3A%22%22%2C%22edateend%22%3A%22%22%2C%22rdatestart%22%3A%22%22%2C%22rdateend%22%3A%22%22%2C%22rcapitalstart%22%3A%22%22%2C%22rcapitalend%22%3A%22%22%2C%22prodcountstart%22%3A%22%22%2C%22prodcountend%22%3A%22%22%2C%22personstart%22%3A%22%22%2C%22personend%22%3A%22%22%2C%22faex%22%3Afalse%2C%22icex%22%3Afalse%2C%22rpex%22%3Afalse%2C%22jrex%22%3Afalse%2C%22legalnotsame%22%3Afalse%2C%22abnormal%22%3Afalse%2C%22invests%22%3A%5B%5D%2C%22aums%22%3A%5B%5D%2C%22starlevel%22%3A0%2C%22totc%22%3A-1%2C%22natureenterprises%22%3A%5B%5D%2C%22isinvestmentsuggestion%22%3A%5B%5D%2C%22scpsstatus%22%3A%5B%5D%2C%22members%22%3A%5B%5D%2C%22isvalid%22%3A%5B%5D%2C%22isnew%22%3Afalse%2C%22sort%22%3A%7B%22type%22%3A0%2C%22desc%22%3Atrue%7D%7D",
            "Referer": "https://jdb.hffss.com/ManageAgency",
            "sid": ssid,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X)\
            AppleWebKit/602.3.12 (KHTML, like Gecko)\
            Mobile/14C92 Safari/601.1 wechatdevtools/1.02.1901230\
            MicroMessenger/6.7.3 Language/zh_CN webview/15561554780482248 webdebugger port/55904",
        }
        payload = {
            'abnormal': 'false',
            'aums': [],
            'ccsend': "",
            'ccsstart':"",
            'edateend': "",
            'edatestart':"",
            'faex': 'false',
            'icex': 'false',
            'invests': [],
            'isinvestmentsuggestion': [],
            'isnew': 'false',
            'isvalid': [],
            'jrex': 'false',
            'keyword': "恒天",
            'legalnotsame':'false',
            'members': [],
            'natureenterprises': [],
            'officepros': [],
            'page': 1,
            'personend': "",
            'personstart':"",
            'prodcountend': "",
            'prodcountstart':"",
            'provinces': [],
            'rcapitalend': "",
            'rcapitalstart':"",
            'rdateend': "",
            'rdatestart':"",
            'rpex': 'false',
            'scpsstatus': [],
            'sort': {'type': 0, 'desc':'true'},
            'starlevel': 0,
            'totc': -1,
            'type': 0
        }
        r = requests.post(
            url=url,
            headers=headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'],'success')
        self.assertEqual(r.json()['data']['count'],17)

    def test4_corp(self):
        '''管理人详情'''
        url = 'https://api.jdb.hffss.com/fundManager/infolist'
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "api.jdb.hffss.com",
            "oid": "obgs71WOxNmem_hMWqxBWwOtEstc",
            "Origin": "https://jdb.hffss.com",
            "rb": "%7B%22corpid%22%3A100003150%7D",
            "Referer": "https://jdb.hffss.com/ManagersDetails?corpid=100003150",
            "sid": ssid,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
            AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
            wechatdevtools/1.02.1904090 MicroMessenger/6.7.3 \
            Language/zh_CN webview/15565863467247017 webdebugger port/46333",
        }
        payload = {"corpid":100003150}
        r = requests.post(
            url=url,
            headers=headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['data']['corplist']['fullname'],'恒天中岩投资管理有限公司')
        self.assertEqual(r.json()['status'],'success')

def suite():
    loginTestCase = unittest.makeSuite(crop, "test")
    return loginTestCase

if __name__ == '__main__':
    #fr = open("res3.html", "wb")
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title="接口测试报告",description="测试用例结果",tester=u"舒萌")
    #runner.run(suite())
    #fr.close()
    unittest.main()
