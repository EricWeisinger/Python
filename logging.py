
import datetime

name=input('What is your name? ')
filename='log.txt'
fp= open(filename, 'a')
login_time =datetime.datetime.now()
login_string = login_time.strftime('%a, %m/%d/%y, %I:%M:%S%p') 
fp.write(name + ' logged in at ' + login_string + '\n')

input('Press Enter to log out')
logout_time=datetime.datetime.now()
logout_string = logout_time.strftime('%a, %m/%d/%y, %I:%M:%S%p')
fp.write(name + ' logged out at ' + logout_string + '\n')
fp.close()
