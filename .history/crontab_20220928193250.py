#######################
##  Import Packages  ##
#######################
import airflow
import crontab
import requests
import json
import os
import sys
import time

# get current working directory
cwd = os.getcwd()

# print cws
print(cwd)

# create a new dictionary with dummy data
bitcoin_data = requests.get('')


# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/crontab_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))
