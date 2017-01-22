import pandas as pd
import os
import time
from datetime import datetime

path = './intraQuarter'

def features(gather='Total Debt/Equity (mrq)'):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]

    # first one is root path itself(./intraQuarter/_KeyStats)
    for stock_data in stock_list[1:]:
        each_file = os.listdir(stock_data)
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                print(date_stamp, unix_time)
                time.sleep(15)


features()