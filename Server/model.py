BLOCK_SIZE = 32
WS_WIDTH = 20
WS_HEIGHT = 20
WORLD_WS_WIDTH = 15
WORLD_WS_HEIGHT = 15
# the implied max screen width in pixels is : BLOCK_SIZE * WS_WIDTH * 2

world = []
players = {}


def newEntityNum(entityNum=0,reclaimedEntityNums=[]):
  if len(reclaimedEntityNums) > 0:
    return reclaimedEntityNums.pop()
  else:
    entityNum = entityNum + 1
    return entityNum

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

class WorldSection:
  """ WorldSection class: to break the world into digestable chunks for the client """
  entities = dict()

  def __init__(self,x,y):
    self.x = x
    self.y = y

  def get(self,attr):
    if attr == 'x':
      return self.x
    elif attr == 'y':
      return self.y

  def addEntity(self,ent):
    self.entities[ent.id] = ent

  def removeEntity(self,ent):
    del self.entities[ent.id]

class Entity:
  """ Base class for all game entities """
  def __init__(self,x,y,newId,ws):
    #x is integer in range WS_WIDTH * BLOCK_SIZE
    #y is integer in range WS_HEIGHT * BLOCK_SIZE
    self.x = x
    self.y = y
    self.id = newId
    self.ws = ws
    ws.addEntity(self)

  def changeWs(ws):
    self.ws.removeEntity(self)
    ws.addEntity(self)

class Player(Entity):
  def __init__(self,sock):
    Entity.__init__(self,320,320,newEntityNum(),world[7][7])
    self.sock = sock
    self.dx = 0
    self.dy = 0

  def move(self, direction):
    print 'moving player direction, ','nnn'+direction+'nnn'
    if direction == 'up\n':
      if (self.dx == 1) or (self.dx == 0.707):
        self.dx = 0.707
        self.dy = -0.707
      elif (self.dx == -1) or (self.dx == -0.707):
        self.dx = -0.707
        self.dy = -0.707
      else: 
        self.dy = -1
    elif direction == 'down\n':
      if (self.dx == 1) or (self.dx == 0.707):
        self.dx = 0.707
        self.dy = 0.707
      elif (self.dx == -1) or (self.dx == -0.707):
        self.dx = -0.707
        self.dy = 0.707
      else: 
        self.dy = 1
    elif direction == 'left\n':
      if (self.dy == 1) or (self.dy == 0.707):
        self.dx = -0.707
        self.dy = 0.707
      elif (self.dy == -1) or (self.dy == -0.707):
        self.dx = -0.707
        self.dy = -0.707
      else: 
        self.dx = -1
    elif direction == 'right\n':
      if (self.dy == 1) or (self.dy == 0.707):
        self.dx = 0.707
        self.dy = 0.707
      elif (self.dy == -1) or (self.dy == -0.707):
        self.dx = 0.707
        self.dy = -0.707
      else: 
        self.dx = 1

  def stop(self, direction):
    if direction == 'up\n' or direction == 'down\n':
      self.dy = 0
    elif direction == 'right\n' or direction == 'left\n':
      self.dx = 0

  def get(self,attr):
    if attr == 'x':
      return self.x
    elif attr == 'y':
      return self.y
    elif attr == 'wx':
      return self.ws.get('x')
    elif attr == 'wy':
      return self.ws.get('y')
    elif attr == 'dx':
      return self.dx
    elif attr == 'dy':
      return self.dy

  def set(self,attr,value):
    if attr == 'x':
      self.x = value
    elif attr == 'y':
      self.y = value

class Rock(Entity):
  def __init__(self,x,y,ws):
    Entity.__init__(self,x,y,newEntityNum(),ws)

def updateModel():
  global players
  for player in players:
    print 'updating player : ',player
    print 'dx, dy is',players[player].get('dx'),players[player].get('dy')
    players[player].set('x', players[player].get('x') + players[player].get('dx'))
    players[player].set('y', players[player].get('y') + players[player].get('dy'))
