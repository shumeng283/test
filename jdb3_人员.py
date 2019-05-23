# Author :lixinhao
import requests
import json
import unittest
from ssid import ssidx

ssid = ssidx()
class pers_list(unittest.TestCase):
    '''人员'''
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
            "rb": "%7B%22searchWord%22%3A%22%u5317%u4EAC%22%2C%22corptype%22%3A-1%2C%22positiontype%22%3A-1%2C%22pageNumber%22%3A1%7D",
            "Referer": "https://jdb.hffss.com/PersonSearch",
            "sid": ssid,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) \
            AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 Safari/601.1 \
            wechatdevtools/1.02.1904090 MicroMessenger/6.7.3 Language/zh_CN \
            webview/15570249937402471 webdebugger port/30076"
        }

    def test1_search1(self):
        '''搜索'''
        url = 'https://api.jdb.hffss.com/comm/searchpeople'
        payload = {
            'searchWord': "北京",
            'corptype': -1,
            'positiontype': -1,
            'pageNumber': 1
        }
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'],'success')
        self.assertEqual(r.json()['data']['totalCount'],16)

    def test1_search2(self):
        '''筛选-高管'''
        url = 'https://api.jdb.hffss.com/comm/searchpeople'
        payload = {
            'searchWord': "北京",
            'corptype': 1,
            'positiontype': 2,
            'pageNumber': 1
        }
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')
        self.assertEqual(r.json()['data']['totalCount'], 7)

    def test1_search3(self):
        '''筛选-私募'''
        url = 'https://api.jdb.hffss.com/comm/searchpeople'
        payload = {
            'searchWord': "林虹",
            'corptype': 1,
            'positiontype': -1,
            'pageNumber': 1
        }
        r = requests.post(
            url=url,
            headers=self.headers,
            data=json.dumps(payload)
        )
        print(r.json())
        print(r.status_code)
        self.assertEqual(r.json()['status'], 'success')
        self.assertEqual(r.json()['data']['totalCount'], 3)

def suite():
    loginTestCase = unittest.makeSuite(crop, "test")
    return loginTestCase

if __name__ == '__main__':
    unittest.main()
