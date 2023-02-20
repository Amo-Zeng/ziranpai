import time, json, requests
def 获取爬果(url):
    return requests.get(url=url)
def 爬果文字(re):
    return re.text()
def 爬果内容(re):
    return re.content()
def 爬果杰森(re):
    return re.json()
def 爬果关键字(re):
    return re.key()

函子={"获取爬果":获取爬果,"爬果文字":爬果文字,"爬果内容":爬果内容,"爬果杰森":爬果杰森,"爬果关键字":爬果关键字}#接受一个变量的函数字典
函丑={}#接受两个变量的函数字典，依此类推
函寅={}
函卯={}
函辰={}
函巳={}
函午={}
函未={}
函申={}
函酉={}
函戌={}
函亥={}
函括={}#接受任意个变量的函数字典，引用函数时需要用括号把函数和变量括起来。
