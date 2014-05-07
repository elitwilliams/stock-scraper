import urllib
import re
import json

symbolslist = open('symbols.txt').read()
symbolslist = symbolslist.split("\n")

for symbol in symbolslist:
    myfile = open('daily-prices/'+symbol+'.txt','w+')
    myfile.close()

    htmltext = urllib.urlopen('http://www.bloomberg.com/markets/chart/data/1D/'+symbol+':US')
    data = json.load(htmltext)
    datapoints = data['data_values']

    myfile = open('daily-prices/'+symbol+'.txt','a')

    for point in datapoints:
        # print point[1]
        myfile.write(symbol+','+str(point[0])+','+str(point[1])+'\n')
    myfile.close()

# print 'The number of points is: ',len(datapoints)

# Most recent price: data['data_values'][len(data['data_values'])-1][1]

