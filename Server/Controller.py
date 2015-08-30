import Model
import random

BLOCK_SIZE = 32
WS_WIDTH = 20
WS_HEIGHT = 20
WORLD_WS_WIDTH = 15
WORLD_WS_HEIGHT = 15

def isPlayer(thread):
  return Model.isPlayer(thread)

def newPlayer(args):
  Model.newPlayer(args)

def movePlayer(args):
  pass

def stopPlayer(args):
  pass

def closeSock(args):
  args[1].close()

def initWorld():
  for x in range(0,WORLD_WS_WIDTH):
    Model.world.append([])
    for y in range(0,WORLD_WS_HEIGHT):
      Model.world[x].append(Model.WorldSection(x,y))
      for i in range(0,10):
        xpos = random.randrange(32*19)
        ypos = random.randrange(32*19)
        Model.Rock(xpos,ypos,Model.world[x][y])


def handleInput(msg,sock,thread):
  command = msg.partition(' ')
  msgSwitch[command[0]]([command[2],sock,thread])

def sendWorldSection(sock,thread):
  print "sending world state"
  player = Model.getPlayer(thread);
  sendStr = ''
  sendStr += str(player.get('x')) + ' '
  sendStr += str(player.get('y')) + ' '
  sendStr += str(player.get('wx')) + ' '
  sendStr += str(player.get('wy')) + ' '
  try:
    sock.sendall(sendStr)
  except:
    Model.removePlayer(thread)


msgSwitch = {'np':newPlayer,'go':movePlayer,'stop':stopPlayer,'close':closeSock}


