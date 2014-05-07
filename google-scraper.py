import urllib
import re
import json

htmltext = urllib.urlopen('http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US')

'''
htmltext = urllib.urlopen('http://www.google.com/finance/getprices?q=GOOG&x=NASD&i=8000&p=40Y&f=c&df=cpct&auto=0&ei=Ef6XUYDfCqSTiAKEMg').read()

regex = '<span id="ref_[^.]*_l">(.+?)</span>'

pattern = re.compile(regex)

results = re.findall(pattern,htmltext)

print results
'''

data = json.load(htmltext)

print data["last_price"]


