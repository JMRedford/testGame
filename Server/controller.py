import model
import random

BLOCK_SIZE = 32
WS_WIDTH = 20
WS_HEIGHT = 20
WORLD_WS_WIDTH = 15
WORLD_WS_HEIGHT = 15

def isPlayer(thread):
  return model.isPlayer(thread)

def newPlayer(args):
  model.newPlayer(args)

def movePlayer(args):
  model.players[args[2]].move(args[0])

def stopPlayer(args):
  model.players[args[2]].stop(args[0])

def closeSock(args):
  args[1].close()


def handleInput(msg,sock,thread):
  command = msg.partition(' ')
  msgSwitch[command[0]]([command[2],sock,thread])

def sendWorldSection(sock,thread):
  
  player = model.getPlayer(thread);
  sendStr = 's '
  sendStr += str(player.get('x')) + ' '
  sendStr += str(player.get('y')) + ' '
  sendStr += str(player.get('wx')) + ' '
  sendStr += str(player.get('wy')) + ' '

  entDict = model.world[player.get('wx')][player.get('wy')].entities
  count = 0
  for entity in entDict:
    count += 1
    if entity.dirty:
      pass

  print count, ' entities'
  
  try:
    sock.sendall(sendStr)
  except:
    print ('removing player in thread ',threading.current_thread())
    model.removePlayer(thread)


msgSwitch = {'np':newPlayer,'go':movePlayer,'stop':stopPlayer,'close':closeSock}


