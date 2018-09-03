import re
import urllib.request
req = urllib.request.Request('https://tieba.baidu.com/p/3823765471?red_tag=3097386551')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
page = urllib.request.urlopen(req)
html = page.read().decode('utf-8')
p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*? width="560" height="497">'
imglist = re.findall(p,html)
for each in imglist:
    print(each)