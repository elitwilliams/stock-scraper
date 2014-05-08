from threading import Thread
import urllib
import re
import MySQLdb

symbolslist = open('symbols.txt').read()
symbolslist = symbolslist.replace("\n",",").split(',')
threadlist = []
gmap = {}

def th(ur):
    base = "http://finance.yahoo.com/q?s="+ur
    htmltext = urllib.urlopen(base).read()
    regex = '<span id="yfs_l84_.+?">(.+?)</span>'
    pattern = re.compile(regex)
    results = re.findall(pattern,htmltext)
    try:
        gmap[ur] = results[0]
    except:
        print 'got an error'

# Original print statement: print "The price of "+str(ur)+' is '+str(results[0])

for u in symbolslist:
    t = Thread(target=th,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()

# Connect to MySQL Database 'stock_data'

conn = MySQLdb.connect(host='localhost',user='root',passwd="",db='stock_data')

for key in gmap.keys():
    print key,gmap[key]
    query = "INSERT INTO tutorial (symbol,last) values ('"+key+"',"+gmap[key]+")"
    x = conn.cursor()
    x.execute(query)
    row = x.fetchall()
    conn.commit()

