import socket
import sys
import pygame
import localModel
import threading
import time

pygame.init()
disp = pygame.display.set_mode([1000,600],pygame.NOFRAME)
localModel.init(disp)


HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)

try:
  # Connect to server and send data
  sock.connect((HOST, PORT))
except:
  pass
finally:
  sock.sendall('np \n')

def startMove(direction):
  localModel.player['facing'] = direction
  localModel.player['moving'] = True
  sock.sendall("go "+direction+"\n")

def stopMove(direction):
  localModel.player['moving'] = False
  sock.sendall("stop "+direction+"\n")

def startShoot():
  localModel.player['attacking'] = True

def stopShoot():
  localModel.player['attacking'] = False

commands = {}

lastRender = 0

while(1):
  e = pygame.event.poll()
  if (e.type == pygame.KEYDOWN):
    if (e.key == pygame.K_ESCAPE):
      sock.sendall('close')
      sock.close()
      break
    elif (e.key == pygame.K_UP):
      startMove('up')
    elif (e.key == pygame.K_DOWN):
      startMove('down')
    elif (e.key == pygame.K_LEFT):
      startMove('left')
    elif (e.key == pygame.K_RIGHT):
      startMove('right')
    elif (e.key == pygame.K_SPACE):
      startShoot()
    else:
      if e.key in commands:
        commands[e.key]()
  if (e.type == pygame.KEYUP):
    if (e.key == pygame.K_UP):
      stopMove('up')
    elif (e.key == pygame.K_DOWN):
      stopMove('down')
    elif (e.key == pygame.K_LEFT):
      stopMove('left')
    elif (e.key == pygame.K_RIGHT):
      stopMove('right')
    elif (e.key == pygame.K_SPACE):
      stopShoot()
  try:
    data = sock.recv(1024)
    localModel.handleResp(data)
  except:
    pass
  if (time.time() - lastRender > 0.1):
    lastRender = time.time()
    localModel.boardRender()
  