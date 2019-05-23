# Author :lixinhao
import json
import requests
import unittest
from ssid import ssidx

ssid = ssidx()
class prod_fund(unittest.TestCase):
    '''私募产品'''
    def setUp(self):
        pass

    @property
    def headers(self):
        return {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "api.jdb.hffss.com",
            "oid": "obgs71WOxNmem_hMWqxBWwOtEstc",
            "Origin": "https://jdb.hffss.com",
            "rb": "%7B%22type%22%3A4%2C%22page%22%3A1%2C%22sort%22%3A%7B%22type%22%3A1%2C%22desc%22%3Atrue%7D%7D",
            "Referer": "https://jdb.hffss.com/ProductSearch",
            "sid": ssid,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
            AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
            wechatdevtools/1.02.1904090 MicroMessenger/6.7.3 Language/zh_CN \
            webview/15565863467247017 webdebugger port/46333"
        }

    def test1_hot(self):
        '''热门搜索'''
        url = 'https://api.jdb.hffss.com/pro/hotwords'
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "api.jdb.hffss.com",
            "oid": "obgs71WOxNmem_hMWqxBWwOtEstc",
            "Origin": "https://jdb.hffss.com",
            "rb": "%7B%22type%22%3A2%7D",
            "Referer": "https://jdb.hffss.com/ProductSearch",
            "sid": ssid,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
            AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
            wechatdevtools/1.02.1904090 MicroMessenger/6.7.3 Language/zh_CN \
            webview/15565863467247017 webdebugger port/46333"
        }
        payload = {'type': 2}
        r = requests.post(
            url=url,
            headers=headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'],'success')

    def test2_type1(self):
        '''筛选-私募基金'''
        url = 'https://api.jdb.hffss.com/product/search'
        payload = {
            'type':1,
            'page':1,
            'sort': {'type': 1, 'desc': 'true'},
            'scpsstatus': []
        }
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')
        self.assertEqual(r.json()['data']['count'],108680)

    def test2_type2(self):
        '''筛选-基金专户'''
        url = 'https://api.jdb.hffss.com/product/search'
        payload = {
            'type': 2,
            'page': 1,
            'sort': {'type': 1, 'desc': 'true'},
        }
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')
        self.assertEqual(r.json()['data']['count'], 29948)

    def test2_tpye3(self):
        '''筛选-期货资管'''
        url = 'https://api.jdb.hffss.com/product/search'
        payload = {
            'type': 4,
            'page': 1,
            'sort': {'type': 1, 'desc': 'true'},
        }
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')
        self.assertEqual(r.json()['data']['count'], 7201)

class prod_information(unittest.TestCase):
    '''产品详情'''
    def setUp(self):
        pass

    @property
    def headers(self):
        return {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "api.jdb.hffss.com",
            "oid": "obgs71WOxNmem_hMWqxBWwOtEstc",
            "Origin": "https://jdb.hffss.com",
            "rb": "%7B%22type%22%3A2%7D",
            "Referer": "https://jdb.hffss.com/ProductSearch",
            "sid": ssid,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
            AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
            wechatdevtools/1.02.1904090 MicroMessenger/6.7.3 Language/zh_CN \
            webview/15565863467247017 webdebugger port/46333"
        }

    def test1_prod1(self):
        '''基协基本信息'''
        url = 'https://api.jdb.hffss.com/product/smcp'
        payload = {'prodid' : 110012428}
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')

    def test1_prod2(self):
        '''工商基本信息'''
        url = 'https://api.jdb.hffss.com/fundManager/combusiness'
        payload = {'corpid' : 9510080164}
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')

    def test1_prod3(self):
        '''家族树'''
        url = 'https://api.jdb.hffss.com/profund/familysearch'
        payload = {
            'companyType' : 0,
            'corpid' : 9510080164
        }
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')

def suite():
    loginTestCase = unittest.makeSuite(crop, "test")
    return loginTestCase

if __name__ == '__main__':
    unittest.main()