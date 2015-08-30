import pygame
import os

player = {'x':0,'y':0,'wx':0,'wy':0,'surface':None}
entities = {}
sections = [[],[],[]]
display = None

def init(disp):
  global display
  global sections
  global player
  display = disp
  player['surface'] = pygame.image.load(os.path.join('Assets','sorcerer.png'))
  rockSurface =  pygame.image.load(os.path.join('Assets','Rock.png'))
  for i in range(3):
    for j in range(3):
      sections[i].append(pygame.image.load(os.path.join('Assets','Field.png')))

def handleResp(data):
  print "recieved : ",data
  global player
  global entities
  handle = data.partition(' ')
  player['x'] = int(handle[0])
  handle = handle[2].partition(' ')
  player['y'] = int(handle[0])
  handle = handle[2].partition(' ')
  player['wx'] = int(handle[0])
  handle = handle[2].partition(' ')
  player['wy'] = int(handle[0])
  # commands:
    # a: id x y wsx wsy type
    # d: id
    # m: id x y
  while len(handle) > 1:
    handle = handle[2].partition(' ')
    if handle[0] == 'a':
      handle = handle[2].partition(' ')
      iD = int(handle[0])
      handle = handle[2].partition(' ')
      x = int(handle[0])
      handle = handle[2].partition(' ')
      y = int(handle[0])
      handle = handle[2].partition(' ')
      wx = int(handle[0])
      handle = handle[2].partition(' ')
      wy = int(handle[0])
      handle = handle[2].partition(' ')
      entType = int(handle[0])
      entities[iD] = {'x':x, 'y':y, 'wx':wx, 'wy':wy, 'type':entType}
    elif handle[0] == 'd':
      handle = handle[2].partition(' ')
      iD = int(handle[0])
      del entities[iD]
    elif handle[0] == 'm':
      handle = handle[2].partition(' ')
      iD = int(handle[0])
      handle = handle[2].partition(' ')
      x = int(handle[0])
      handle = handle[2].partition(' ')
      y = int(handle[0])
      entities[iD]['x'] = x
      entities[iD]['y'] = y
    else:
      raise ValueError('Server sent an unknown command : ',handle[0])

def boardRender():
  print "rendering board"
  global sections
  global display
  global player
  display.blit(sections[0][0],(500-player['x']-640,300-player['y']-640))
  display.blit(sections[0][1],(500-player['x'],300-player['y']-640))
  display.blit(sections[0][2],(500-player['x']+640,300-player['y']-640))
  display.blit(sections[1][0],(500-player['x']-640,300-player['y']))
  display.blit(sections[1][1],(500-player['x'],300-player['y']))
  display.blit(sections[1][2],(500-player['x']+640,300-player['y']))
  display.blit(sections[2][0],(500-player['x']-640,300-player['y']+640))
  display.blit(sections[2][1],(500-player['x'],300-player['y']+640))
  display.blit(sections[2][2],(500-player['x']+640,300-player['y']+640))
  display.blit(player['surface'],(484,284))
  pygame.display.flip()
