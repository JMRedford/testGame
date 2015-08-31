import pygame
import os

BLOCK_SIZE = 32
WS_WIDTH = 20
WS_HEIGHT = 20
WORLD_WS_WIDTH = 15
WORLD_WS_HEIGHT = 15

player = {'x':0,'y':0,'dx':0,'dy':0,'wx':0,'wy':0,'surfaces':{
              'right':{
                'stand':pygame.image.load(os.path.join('Assets','wizardRightStand.png')),
                'move1':pygame.image.load(os.path.join('Assets','wizardRightWalk1.png')),
                'move2':pygame.image.load(os.path.join('Assets','wizardRightWalk2.png')),
                'atk1' :pygame.image.load(os.path.join('Assets','wizardRightAtk1.png')),
                'atk2' :pygame.image.load(os.path.join('Assets','wizardRightAtk2.png'))
              },'left':{
                'stand':pygame.image.load(os.path.join('Assets','wizardLeftStand.png')),
                'move1':pygame.image.load(os.path.join('Assets','wizardLeftWalk1.png')),
                'move2':pygame.image.load(os.path.join('Assets','wizardLeftWalk2.png')),
                'atk1' :pygame.image.load(os.path.join('Assets','wizardLeftAtk1.png')),
                'atk2' :pygame.image.load(os.path.join('Assets','wizardLeftAtk2.png'))
              },'up':{
                'stand':pygame.image.load(os.path.join('Assets','wizardBackStand.png')),
                'move1':pygame.image.load(os.path.join('Assets','wizardBackWalk1.png')),
                'move2':pygame.image.load(os.path.join('Assets','wizardBackWalk2.png')),
                'atk1' :pygame.image.load(os.path.join('Assets','wizardBackAtk1.png')),
                'atk2' :pygame.image.load(os.path.join('Assets','wizardBackAtk2.png'))
              },'down':{
                'stand':pygame.image.load(os.path.join('Assets','wizardFrontStand.png')),
                'move1':pygame.image.load(os.path.join('Assets','wizardFrontWalk1.png')),
                'move2':pygame.image.load(os.path.join('Assets','wizardFrontWalk2.png')),
                'atk1' :pygame.image.load(os.path.join('Assets','wizardFrontAtk1.png')),
                'atk2' :pygame.image.load(os.path.join('Assets','wizardFrontAtk2.png'))
              }
            },
            'facing':'down',
            'moving': False,
            'firstMoveFrame' : True,
            'attacking' : False,
            'firstAttackFrame' : True
          }
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

def handleResp(data):
  global player
  global entities
  print 'recieved data : ',data
  handle = data.partition(' ')
  player['x'] = int(handle[0])
  handle = handle[2].partition(' ')
  player['y'] = int(handle[0])
  handle = handle[2].partition(' ')
  newWx = int(handle[0])
  handle = handle[2].partition(' ')
  newWy = int(handle[0])
  if player['wy'] != newWy or player['wx'] != newWx:
    sectionsLoad(newWx,newWy)  
    player['wy'] = newWy
    player['wx'] = newWx
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
