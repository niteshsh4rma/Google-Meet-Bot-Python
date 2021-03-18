import schedule
import time
from join import JoinNow

def join(link, length, name):
    print('Joined', name)
    JoinNow(link, 'Email', 'Password', length)

# scheduling the time table
# length is in minutes

schedule.every().tuesday.at("time in 24 hours format").do(
    join, 
    link='google meet link',
    length= "length of the class in hours in integer",
    name='Class Name'
)


while 1:
    schedule.run_pending()
