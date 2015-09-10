from classes import *

BLOCK_SIZE = 32
WS_WIDTH = 20
WS_HEIGHT = 20
WORLD_WS_WIDTH = 15
WORLD_WS_HEIGHT = 15

PLAYER_SPEED = 10
# the implied max screen width in pixels is : BLOCK_SIZE * WS_WIDTH * 2

world = []
players = {}

def newPlayer(args):
  global players
  print 'making player with key',args[2]
  players[args[2]] = Player(args[1])

def getPlayer(thread):
  return players[thread]

def removePlayer(thread):
  global players
  del players[thread]

def isPlayer(thread):
  return thread in players

def updateModel():
  global players
  for player in players:
    newX = int(players[player].get('x') + (players[player].get('dx')*PLAYER_SPEED))
    newY = int(players[player].get('y') + (players[player].get('dy')*PLAYER_SPEED))
    if (newX < 0):
      wsx = players[player].get('wx')
      wsy = players[player].get('wy')
      if (wsx > 0):
        players[player].changeWs(world[wsx-1][wsy])
        newX = (BLOCK_SIZE * WS_WIDTH) + newX
      else:
        newX = 0
    elif (newX > BLOCK_SIZE * WS_WIDTH):
      wsx = players[player].get('wx')
      wsy = players[player].get('wy')
      if (wsx < WORLD_WS_WIDTH):
        players[player].changeWs(world[wsx+1][wsy])
        newX = newX - (BLOCK_SIZE * WS_WIDTH)
      else:
        newX = BLOCK_SIZE * WS_WIDTH
    if (newY < 0):
      wsx = players[player].get('wx')
      wsy = players[player].get('wy')
      if (wsy > 0):
        players[player].changeWs(world[wsx][wsy-1])
        newY = (BLOCK_SIZE * WS_HEIGHT) + newY
      else:
        newY = 0
    elif (newY > BLOCK_SIZE * WS_HEIGHT):
      wsx = players[player].get('wx')
      wsy = players[player].get('wy')
      if (wsy < WORLD_WS_HEIGHT):
        players[player].changeWs(world[wsx][wsy+1])
        newY = newY - (BLOCK_SIZE * WS_HEIGHT)
      else:
        newY = BLOCK_SIZE * WS_HEIGHT

    players[player].set('x',newX )
    players[player].set('y',newY )
