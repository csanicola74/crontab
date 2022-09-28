# crontab
HHA 507 // Assignment #6

#### ________________________________________
# Schedule of Cron Jobs:
## Every Day at 5am
### $ 00 05 * * * /usr/bin/python crontab.py

## Every Sunday Night at 10:00pm
### $ 00 22 * * SUN /usr/bin/python crontab.py

## ### $ * * * * * /usr/bin/python crontab.py


### Confirm Crontab is already installed
#### crontab -h
#### sudo apt-get install nano

## CREATE A NEW VIRTUAL MACHINE
### 1. SET UP BASIC SETTINGS
### 2. use VM IP, username, and password to connect to VM through own terminal
### 3. $ sudo apt-get update
### 4. $ python3
### 5. $ crontab -h
### 6. $ select-editor
### 7. Choose 1-4 [1]
### 8. $ ls -l
### 9. $ nano test.py
### 10. CTRL O  # to save the file
### 11. crontab -e
### 12. 
