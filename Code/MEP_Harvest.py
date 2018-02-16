
''' This script will harvest Mexican power market data.
This is ment to be run daily and upload the data into a database,
although it is a function and can be used to download up to 7 days of data and
20 nodes at a time.
Created on Tuesday, Decemeber 12, 2017
by Sebastian Kadamany (SKADAMAN)'''

import requests
#import pandas as pd
import numpy as np
def mexharvest(report ,system ,process ,nodes ,datestart ,dateend):
    reports=['PML']
    if report not in reports:
        raise ValueError("Invalid report type. Expected one of: %s" % reports)
    systems=['SIN','BCA','BCS']
    if system not in systems:
        raise ValueError("Invalid system type. Expected one of: %s" % systems)
    processes=['MDA','MTR']
    if process not in processes:
        raise ValueError("Invalid process type. Expected one of: %s" % processes)
    if np.logical_and(len(nodes) >9,"," not in nodes):
        raise ValueError("Invalid node format. Node codes are usually 9 characters long."
                         "If requesting more than one node please separate with commas.")
    if np.logical_and(len(datestart) > 12, "/" not in datestart):
        raise ValueError("Invalid date format. Dates should have format YYYY/MM/DD")
    if np.logical_and(len(dateend) > 12, "/" not in dateend):
        raise ValueError("Invalid date format. Dates should have format YYYY/MM/DD")
    if (int(dateend[-2])-int(datestart[-2]))>7:
        raise ValueError("Invalid date range. Can pull a maximum of seven days at a time")

    url_head=  'https://ws01.cenace.gob.mx:8082/apiSIM/'
    url_tail=report+'/'+system+'/'+process+'/'+nodes+'/'+datestart+'/'+dateend
    url=url_head+url_tail
    data=requests.get(url)
    with open('/Users/W1/Downloads/MexXML.xml','wb') as file:
        file.write(data.content)

#sample call mexharvest("PML","SIN","MDA","01PLO-115","2018/01/12","2018/01/12")

