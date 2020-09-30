
import json
import re
import urllib


def scraper_bloomberg() -> None:
	"""
	Scrapes latest (delayed) price from Bloomberg.com.
	"""
	htmltext = urllib.urlopen('http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US')
	data = json.load(htmltext)

	print data["last_price"]

	return None


def scraper_google() -> None:
	"""
	Scrapes latest (delayed) price from Google Finance.
	"""
	htmltext = urllib.urlopen('http://www.google.com/finance/getprices?q=GOOG&x=NASD&i=8000&p=40Y&f=c&df=cpct&auto=0&ei=Ef6XUYDfCqSTiAKEMg').read()
	regex = '<span id="ref_[^.]*_l">(.+?)</span>'
	pattern = re.compile(regex)
	results = re.findall(pattern,htmltext)

	print results

	return None


def main():
	scraper_bloomberg()


if __name__ == '__main__':
	main()
