#! /usr/bin/python3.4
# -- coding:utf-8 --

from concurrent.futures import *
import urllib.request
import gzip, io
import time

#yiping.luoyp@gmail.com 840406a
#sgllxiaohao1@163.com 840406
#sgllxiaohao2@163.com 840406


	
def doRefresh(w):
	print("\nstart" + str(w))
	weburl = "http://castingcall2015.gap.cn/api/like_work?callback=jQuery17104459619396366179_1433408401803&platform=wap&share_id=556eafeecf0f0&_=1433408832729"
	time.sleep(2)
	req = urllib.request.Request(weburl)
	req.add_header("Accept", "text/javascript, application/javascript, application/ecmascript,application/x-ecmascript, */*; q=0.01")
	req.add_header("Accept-Encoding", "gzip, deflate")
	req.add_header("Accept-Language", "zh-cn")
	req.add_header("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53")
	req.add_header("X-Requested-With", "XMLHttpRequest")
	req.add_header("Cookie", "ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2289ea31ea798d4a6fceb1a25de5c71fc6%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%22192.168.10.60%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+7_1_2+like+Mac+OS+X%29+AppleWebKit%2F537.51.2+%28KHTML%2C+like+Gecko%29+Version%2F7.0+Mobile%2F11D2%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1433408971%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Def75d3e6bf71d6374a2e2675f0c75128; like_work_20150604=4; PHPSESSID=pbukttses10joaoeoggdk7btt4; _ga=GA1.2.2057529714.1433408402")
	req.add_header("DNT", "1")
	req.add_header("Connection", "keep-alive")
	req.add_header("Content-Type", "application/x-www-form-urlencoded")
	req.add_header("Referer", "http://castingcall2015.gap.cn/cs/wap/index.html?share_id=556eafeecf0f0")
	req.add_header("Host", "castingcall2015.gap.cn")
	response = urllib.request.urlopen(req)
	print(response.status, response.reason)
	text = response.read()
	print(text)
	return 1

if __name__ == '__main__':
        while 1:
                try:
                        time.sleep(2)
                        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                        e = ThreadPoolExecutor(max_workers=10)
                        fs = e.map(doRefresh, range(1, 20))
                        for f in fs:                                
                                print(f)
                except Exception as err:
                        print(err)
		
	
