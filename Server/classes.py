entityNum = 0
reclaimedEntityNums = []

def newEntityNum():
  global entityNum
  global reclaimedEntityNums
  if len(reclaimedEntityNums) > 0:
    return reclaimedEntityNums.pop()
  else:
    entityNum = entityNum + 1
    return entityNum

class Entity:
  """ Base class for all game entities """
  def __init__(self,x,y,newId,ws):
    #x is integer in range WS_WIDTH * BLOCK_SIZE
    #y is integer in range WS_HEIGHT * BLOCK_SIZE
    self.x = x
    self.y = y
    self.id = newId
    self.ws = ws
    self.dx = 0
    self.dy = 0
    ws.addEntity(self)

  def changeWs(self,ws):
    self.ws.removeEntity(self)
    self.ws = ws
    ws.addEntity(self)

class Player(Entity):
  def __init__(self,sock,ws):
    Entity.__init__(self,320,320,newEntityNum(),ws)
    self.sock = sock
    self.prefix = 'p'

  def move(self, direction):
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
    self.prifix = 'r'

class WorldSection:
  """ WorldSection class: to break the world into digestable chunks for the client """

  def __init__(self,x,y):
    self.entities = dict()
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