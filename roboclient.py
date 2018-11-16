import requests
from rrb3 import *
import time
power = 10.0
speed = 1
rr = RRB3(12.0,power)
command = ''
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
try:
    while True:

        get_command = requests.get('http://18.222.193.168/commanderEd')
        print(get_command.text+','+str(get_command.status_code))
        if get_command.status_code == 200:
            command = get_command.text
        else:
            command = 'stop'
        if command == '72':
            print('forward')
            rr.set_motors(speed,1,speed,1)
        if command == '75':
            print('left')
            rr.set_motors(0,0,speed,1)
        if command == '77':
            print('right')
            rr.set_motors(speed,1,0,0)
        if command == 'stop':
            print('stop')
            rr.stop()
        if command == '80':

            rr.set_motors(speed,0,speed,0)
            print('reverse')
        if speed < 1:
            if command == '81':
                #increase speed
                speed+=.1
        if speed > 0.1:
            if command == '73':
                #decrease speed
                speed-=.1
        print('speed '+str(speed))
except KeyboardInterrupt:
    GPIO.cleanup()
