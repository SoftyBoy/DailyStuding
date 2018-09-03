import urllib.request
import re

url = "http://www.baidu.com"
print("-------------scrapting baidu-------------")
print("-------------------begin-----------------")
data = urllib.request.urlopen(url).read().decode("utf-8")
print(len(data))
print("--------------------end------------------")
print("hello world")