Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> import requests
>>> r=requests.get('http://stock.jrj.com.cn/share,600031,zcfzb.shtml')
>>> data=r.text
>>> result =re.findall(r"<tr><td\s*class=\u0022txl\u0022>([^<]+)</td><td>", data)
