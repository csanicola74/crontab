#######################
##  Import Packages  ##
#######################
import airflow
import testFile
import requests
import json
import os
import sys
import time

# get the current time
now = time.time()
timestart = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', timestart)

# get current working directory
cwd = os.getcwd()

# print cws
print(cwd)

# create a new dictionary with dummy data
bitcoin_data = requests.get(
    'https://api.coindesk.com/v1/bpi/currentprice.json')

# save data to a local csv file
bitcoin_data.to_csv('data/bitcoin_data.csv')

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/home/caroline/crontab/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(bitcoin_data))

# time end
now = time.time()
endTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', endTime)
