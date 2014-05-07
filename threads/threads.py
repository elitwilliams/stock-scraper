from threading import Thread
import urllib
import re

def th(ur):
    base = "http://finance.yahoo.com/q?s="+ur
    htmltext = urllib.urlopen(base).read()
    regex = '<span id="yfs_l84_'+ur+'">(.+?)</span>'
    pattern = re.compile(regex)
    results = re.findall(pattern,htmltext)
    print h
#    print "The price of ",ur,' is ',results

symbolslist = open('symbols2.txt').read()
symbolslist = symbolslist.replace("\n",",").split(',')

threadlist = []

for u in symbolslist:
    t = Thread(target=th,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()

