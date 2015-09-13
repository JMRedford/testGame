import socket
import sys
import pygame
import localModel
import threading
import time
from constants import *

pygame.init()
disp = pygame.display.set_mode([1000,600],pygame.NOFRAME)
localModel.init(disp)

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)

try:
  # Connect to server and send data
  sock.connect((HOST, PORT))
except:
  pass
finally:
  # send initial message(s) to server here

lastRender = 0

while(1):
  e = pygame.event.poll()
  if (e.type == pygame.KEYDOWN):
    if (e.key == pygame.K_ESCAPE):
      sock.sendall('close')
      sock.close()
      break
    elif (e.key == pygame.K_UP):
      pass
    elif (e.key == pygame.K_DOWN):
      pass
    elif (e.key == pygame.K_LEFT):
      pass
    elif (e.key == pygame.K_RIGHT):
      pass
    elif (e.key == pygame.K_SPACE):
      pass
    else:
      pass
  if (e.type == pygame.KEYUP):
    if (e.key == pygame.K_UP):
      pass
    elif (e.key == pygame.K_DOWN):
      pass
    elif (e.key == pygame.K_LEFT):
      pass
    elif (e.key == pygame.K_RIGHT):
      pass
    elif (e.key == pygame.K_SPACE):
      pass
  try:
    data = sock.recv(1024)
    # call something to handle incoming data
  except:
    pass
  if (time.time() - lastRender > 0.1):
    lastRender = time.time()
    # localModel.boardRender() render the board

### Stuff from before the refactor for reference ###
  
# def boardRender():
#   global sections
#   global display
#   global player
#   wsx = player['wx']
#   wsy = player['wy']
#   display.blit(sections[0][0],(500-player['x']-640,300-player['y']-640))
#   display.blit(sections[0][1],(500-player['x'],300-player['y']-640))
#   display.blit(sections[0][2],(500-player['x']+640,300-player['y']-640))
#   display.blit(sections[1][0],(500-player['x']-640,300-player['y']))
#   display.blit(sections[1][1],(500-player['x'],300-player['y']))
#   display.blit(sections[1][2],(500-player['x']+640,300-player['y']))
#   display.blit(sections[2][0],(500-player['x']-640,300-player['y']+640))
#   display.blit(sections[2][1],(500-player['x'],300-player['y']+640))
#   display.blit(sections[2][2],(500-player['x']+640,300-player['y']+640))
  
#   if (player['attacking']):
#     if (player['firstAttackFrame']):
#       display.blit(player['surfaces'][player['facing']]['atk1'],(484,284))
#       player['firstAttackFrame'] = False
#     else:
#       if (player['facing'] == 'left'):
#         display.blit(player['surfaces'][player['facing']]['atk2'],(472,284))
#       else:
#         display.blit(player['surfaces'][player['facing']]['atk2'],(484,284))
#       player['firstAttackFrame'] = True
#   elif (player['moving']):
#     if (player['firstMoveFrame']):
#       display.blit(player['surfaces'][player['facing']]['move1'],(484,284))
#       player['firstMoveFrame'] = False
#     else:
#       display.blit(player['surfaces'][player['facing']]['move2'],(484,284))
#       player['firstMoveFrame'] = True
#   else:
#     display.blit(player['surfaces'][player['facing']]['stand'],(484,284))
#   pygame.display.flip()

# player = {'x':0,'y':0,'dx':0,'dy':0,'wx':0,'wy':0,'surfaces':{
#               'right':{
#                 'stand':pygame.image.load(os.path.join('Assets','wizardRightStand.png')),
#                 'move1':pygame.image.load(os.path.join('Assets','wizardRightWalk1.png')),
#                 'move2':pygame.image.load(os.path.join('Assets','wizardRightWalk2.png')),
#                 'atk1' :pygame.image.load(os.path.join('Assets','wizardRightAtk1.png')),
#                 'atk2' :pygame.image.load(os.path.join('Assets','wizardRightAtk2.png'))
#               },'left':{
#                 'stand':pygame.image.load(os.path.join('Assets','wizardLeftStand.png')),
#                 'move1':pygame.image.load(os.path.join('Assets','wizardLeftWalk1.png')),
#                 'move2':pygame.image.load(os.path.join('Assets','wizardLeftWalk2.png')),
#                 'atk1' :pygame.image.load(os.path.join('Assets','wizardLeftAtk1.png')),
#                 'atk2' :pygame.image.load(os.path.join('Assets','wizardLeftAtk2.png'))
#               },'up':{
#                 'stand':pygame.image.load(os.path.join('Assets','wizardBackStand.png')),
#                 'move1':pygame.image.load(os.path.join('Assets','wizardBackWalk1.png')),
#                 'move2':pygame.image.load(os.path.join('Assets','wizardBackWalk2.png')),
#                 'atk1' :pygame.image.load(os.path.join('Assets','wizardBackAtk1.png')),
#                 'atk2' :pygame.image.load(os.path.join('Assets','wizardBackAtk2.png'))
#               },'down':{
#                 'stand':pygame.image.load(os.path.join('Assets','wizardFrontStand.png')),
#                 'move1':pygame.image.load(os.path.join('Assets','wizardFrontWalk1.png')),
#                 'move2':pygame.image.load(os.path.join('Assets','wizardFrontWalk2.png')),
#                 'atk1' :pygame.image.load(os.path.join('Assets','wizardFrontAtk1.png')),
#                 'atk2' :pygame.image.load(os.path.join('Assets','wizardFrontAtk2.png'))
#               }
#             },
#             'facing':'down',
#             'moving': False,
#             'firstMoveFrame' : True,
#             'attacking' : False,
#             'firstAttackFrame' : True
#           }