import pygame
import requests
from pygame.locals import *
pygame.init()
try:
  ip = input('Enter_IP')
except:
  ip = raw_input('Enter_IP')

running = True
screen = pygame.display.set_mode((200,200))
command = ''
while running:

    for event in pygame.event.get():

        if "KeyDown" in str(event):
            command = str(event).split("'scancode':")[1].split(" ")[1].split('}')[0]
            


        if "KeyUp" in str(event):
            command = 'stop'
        if event.type == QUIT:
            running = False
        get_command = requests.get('http://'+ip+'/robotcommand/'+command)
        print(command)
