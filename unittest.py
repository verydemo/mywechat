import requests
import json

baseurl = "http://127.0.0.1:8020"
url1 = baseurl+"/login"
url2 = baseurl+"/register"
url3 = baseurl+"/wechatThePublic"
url4 = baseurl+"/wechatThePublic/1"
url5 = baseurl+"/wechatBusiness"
url6 = baseurl+"/wechatBusiness/1"
url7 = baseurl+"/wechatGroup"
url8 = baseurl+"/wechatGroup/1"
url9 = baseurl+"/wechatArticle"
url10 = baseurl+"/wechatArticle/1"
url11 = baseurl+"/wechatPersonal"
url12 = baseurl+"/wechatPersonal/1"

# imgpath="C:/Users/zjl/Desktop/google.png"
imgpath = "/root/51liuxiaolu.jpg"


class Test():

    def __init__(self):
        self.headers = {}

    def register(self):
        payload = {
            "username": "zjl",
            "password": "1234"
        }
        self.run_request("POST", url2, data=payload)

    def login(self):
        payload = {
            "username": "zjl",
            "password": "1234"
        }
        ret = self.run_request("POST", url1, data=payload)
        self.headers = {
            "Authorization": "bearer "+ret["data"]["token"]
        }

    def post_wechatThePublic(self):
        payload = {
            "industry": "industry",
            "area": "area",
            "title": "title",
            "Id": "zhangjl",
            "desc": "desc",
            "contact": "zjl",
            "phone": "123456",
            "qq": "qq",
            "username": "zjl"
        }
        files = {
            "CoverImg": ("google.png", open(imgpath, "rb")),
            "QRImg1": ("google.png", open(imgpath, "rb"))
        }
        self.run_request("POST", url3, data=payload, files=files)

    def get_wechatThePublics(self):
        self.run_request("GET", url3)

    def get_wechatThePublic(self):
        self.run_request("GET", url4)

    def post_wechatBusiness(self):
        payload = {
            "industry": "industry",
            "area": "area",
            "title": "title",
            "desc": "desc",
            "username": "zjl",
            "wechat": "zjlwechat"
        }
        files = {
            "CoverImg": ("google.png", open(imgpath, "rb")),
            "QRImg1": ("google.png", open(imgpath, "rb"))
        }
        self.run_request("POST", url5, data=payload, files=files)

    def get_wechatBusinesss(self):
        self.run_request("GET", url5)

    def get_wechatBusiness(self):
        self.run_request("GET", url6)

    def post_wechatGroup(self):
        payload = {
            "industry": "industry",
            "area": "area",
            "title": "title",
            "desc": "desc",
            "contact": "zjl",
            "phone": "123456",
            "qq": "qq",
            "username": "zjl",
            "wechat": "zjlwechat"
        }
        files = {
            "HeadImg": ("google.png", open(imgpath, "rb")),
            "QRImg1": ("google.png", open(imgpath, "rb")),
            "QRImg2": ("google.png", open(imgpath, "rb"))
        }
        self.run_request("POST", url7, data=payload, files=files)

    def get_wechatGroups(self):
        self.run_request("GET", url7)

    def get_wechatGroup(self):
        self.run_request("GET", url8)

    def post_wechatArticle(self):
        payload = {
            "column": "column",
            "title": "title",
            "Content": "Content",
            "contact": "zjl",
            "username": "zjl"
        }
        files = {
            "CoverImg": ("google.png", open(imgpath, "rb"))
        }
        self.run_request("POST", url9, data=payload,
                         files=files)

    def get_wechatArticles(self):
        self.run_request("GET", url9)

    def get_wechatArticle(self):
        self.run_request("GET", url10)

    def post_wechatPersonal(self):
        payload = {
            "industry": "industry",
            "area": "area",
            "desc": "desc",
            "contact": "zjl",
            "phone": "123456",
            "qq": "qq",
            "username": "zjl",
            "wechat": "zjlwechat"
        }
        files = {
            "HeadImg": ("google.png", open(imgpath, "rb")),
            "QRImg1": ("google.png", open(imgpath, "rb"))
        }
        self.run_request("POST", url11, data=payload,
                         files=files)

    def get_wechatPersonals(self):
        self.run_request("GET", url11)

    def get_wechatPersonal(self):
        self.run_request("GET", url12)

    def run_request(self, method, url, data={}, files={}):
        response = requests.request(
            method, url, data=data, files=files, headers=self.headers).text
        ret = json.loads(response)
        print(ret["msg"], ret["status"])
        return ret


if __name__ == "__main__":
    tmp = Test()
    tmp.register()
    tmp.login()

    tmp.post_wechatThePublic()
    tmp.get_wechatThePublics()
    tmp.get_wechatThePublic()

    tmp.post_wechatBusiness()
    tmp.get_wechatBusinesss()
    tmp.get_wechatBusiness()

    tmp.post_wechatGroup()
    tmp.get_wechatGroups()
    tmp.get_wechatGroup()

    tmp.post_wechatArticle()
    tmp.get_wechatArticles()
    tmp.get_wechatArticles()

    tmp.post_wechatPersonal()
    tmp.get_wechatPersonals()
    tmp.get_wechatPersonal()

    for i in range(100):
        tmp.post_wechatThePublic()
        tmp.post_wechatBusiness()
        tmp.post_wechatGroup()
        tmp.post_wechatArticle()
        tmp.post_wechatPersonal()

    print(tmp.headers)