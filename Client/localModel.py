import pygame
import os
from player import *
import helpers

BLOCK_SIZE = 32
WS_WIDTH = 20
WS_HEIGHT = 20
WORLD_WS_WIDTH = 15
WORLD_WS_HEIGHT = 15

entities = {}
sections = [[None,None,None],[None,None,None],[None,None,None]]
display = None

def sectionsLoad(x,y):
  global sections
  sections[1][1] = pygame.image.load(os.path.join('Assets','ws'+str(x)+'_'+str(y)+'.png'))
  if (x > 0):
    if (y > 0):
      sections[0][0] = pygame.image.load(os.path.join('Assets','ws'+str(x-1)+'_'+str(y-1)+'.png'))
    else:
      sections[0][0] = pygame.image.load(os.path.join('Assets','Ocean.png'))

    sections[1][0] = pygame.image.load(os.path.join('Assets','ws'+str(x-1)+'_'+str(y)+'.png'))

    if (y < WORLD_WS_HEIGHT - 1):
      sections[2][0] = pygame.image.load(os.path.join('Assets','ws'+str(x-1)+'_'+str(y+1)+'.png'))
    else:
      sections[2][0] = pygame.image.load(os.path.join('Assets','Ocean.png'))

  else:
    sections[0][0] = pygame.image.load(os.path.join('Assets','Ocean.png'))
    sections[1][0] = pygame.image.load(os.path.join('Assets','Ocean.png'))
    sections[2][0] = pygame.image.load(os.path.join('Assets','Ocean.png'))

  if (y > 0):
    sections[0][1] = pygame.image.load(os.path.join('Assets','ws'+str(x)+'_'+str(y-1)+'.png'))
  else:
    sections[0][1] = pygame.image.load(os.path.join('Assets','Ocean.png'))
  if (y < WORLD_WS_HEIGHT - 1):
    sections[2][1] = pygame.image.load(os.path.join('Assets','ws'+str(x)+'_'+str(y+1)+'.png'))
  else:
    sections[2][1] = pygame.image.load(os.path.join('Assets','Ocean.png'))

  if (x < WORLD_WS_WIDTH - 1):
    if (y > 0):
      sections[0][2] = pygame.image.load(os.path.join('Assets','ws'+str(x+1)+'_'+str(y-1)+'.png'))
    else:
      sections[0][2] = pygame.image.load(os.path.join('Assets','Ocean.png'))

    sections[1][2] = pygame.image.load(os.path.join('Assets','ws'+str(x+1)+'_'+str(y)+'.png'))

    if (y < WORLD_WS_HEIGHT - 1):
      sections[2][2] = pygame.image.load(os.path.join('Assets','ws'+str(x+1)+'_'+str(y+1)+'.png'))
    else:
      sections[2][2] = pygame.image.load(os.path.join('Assets','Ocean.png'))

  else:
    sections[0][2] = pygame.image.load(os.path.join('Assets','Ocean.png'))
    sections[1][2] = pygame.image.load(os.path.join('Assets','Ocean.png'))
    sections[2][2] = pygame.image.load(os.path.join('Assets','Ocean.png'))

def init(disp):
  global display
  global sections
  global player
  display = disp
  sectionsLoad(7,7)

def changeWorldSection(newX,newY):
  pass

def handleResp(data):
  global player
  global entities
  print 'recieved data : ',data
  handle = data.partition(' ')
  while len(handle) > 1:
    prefix = handle[0]
    handle = handle[2].partition(' ')
    # switch on the prefixes
    if prefix == 's':
      # self (x,y,wx,wy)
      player['x'] = handle[0]
      handle = handle[2].partition(' ')
      player['y'] = handle[0]
      handle = handle[2].partition(' ')
      if player['wx'] != handle[0]:
        changeWorldSection(player['wx'],handle[0])
        player['wx'] = handle[0]
      handle = handle[2].partition(' ')
      if player['wy'] != handle[0]:
        changeWorldSection(handle[0],player['wy'])
        player['wy'] = handle[0]
      handle = handle[2].partition(' ')
    elif prefix == 'r':
      # rock (id,x,y,wx,wy)
      entId = handle[0]
      entities[entId] = { 'rect':pygame.image.load(os.path.join('Assets','rock.png')) }
      handle = handle[2].partition(' ')
      entities[entId]['x'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['y'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['wx'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['wy'] = handle[0]
      handle = handle[2].partition(' ')
    elif prefix == 'p':
      # player (id,x,y,wx,wy,dir,anim)
      entId = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['x'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['y'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['wx'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['wy'] = handle[0]
      handle = handle[2].partition(' ')
      entDir = handle[0]
      handle = handle[2].partition(' ')
      entAnim = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['rect'] = player['surfaces'][entDir][entAnim]
    elif prefix == 'b':
      # projectile (id,x,y,wx,wy,dx,dy)
      entId = handle[0]
      entities[entId] = { 'rect':pygame.image.load(os.path.join('Assets','shotDown1.png')) }
      handle = handle[2].partition(' ')
      entities[entId]['x'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['y'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['wx'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['wy'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['dx'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['dy'] = handle[0]
      handle = handle[2].partition(' ')
    elif prefix == 'rm':
      # remove (id)
      del entities[handle[0]]
      handle = handle[2].partition(' ')
    elif prefix == 'm':
      # move (id,x,y,wx,wy)
      entId = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['x'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['y'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['wx'] = handle[0]
      handle = handle[2].partition(' ')
      entities[entId]['wy'] = handle[0]
      handle = handle[2].partition(' ')
    # end switch    


def boardRender():
  global sections
  global display
  global player
  wsx = player['wx']
  wsy = player['wy']
  display.blit(sections[0][0],(500-player['x']-640,300-player['y']-640))
  display.blit(sections[0][1],(500-player['x'],300-player['y']-640))
  display.blit(sections[0][2],(500-player['x']+640,300-player['y']-640))
  display.blit(sections[1][0],(500-player['x']-640,300-player['y']))
  display.blit(sections[1][1],(500-player['x'],300-player['y']))
  display.blit(sections[1][2],(500-player['x']+640,300-player['y']))
  display.blit(sections[2][0],(500-player['x']-640,300-player['y']+640))
  display.blit(sections[2][1],(500-player['x'],300-player['y']+640))
  display.blit(sections[2][2],(500-player['x']+640,300-player['y']+640))
  
  if (player['attacking']):
    if (player['firstAttackFrame']):
      display.blit(player['surfaces'][player['facing']]['atk1'],(484,284))
      player['firstAttackFrame'] = False
    else:
      if (player['facing'] == 'left'):
        display.blit(player['surfaces'][player['facing']]['atk2'],(472,284))
      else:
        display.blit(player['surfaces'][player['facing']]['atk2'],(484,284))
      player['firstAttackFrame'] = True
  elif (player['moving']):
    if (player['firstMoveFrame']):
      display.blit(player['surfaces'][player['facing']]['move1'],(484,284))
      player['firstMoveFrame'] = False
    else:
      display.blit(player['surfaces'][player['facing']]['move2'],(484,284))
      player['firstMoveFrame'] = True
  else:
    display.blit(player['surfaces'][player['facing']]['stand'],(484,284))
  pygame.display.flip()
