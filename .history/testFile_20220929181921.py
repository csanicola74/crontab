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


# create a new file in the current working directory
with open(cwd + '/home//testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(bitcoin_data))