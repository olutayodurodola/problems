import time
import webbrowser

def somelist(delay,url):
	by = delay
	webbrowser.open(url)
	time.sleep(by)

myurl = [[10,"www.yahoo.com"],[20,"www.google.com"],[30,"www.cashcraft.com"]]
for i in myurl:
	somelist(i[0],i[1])	