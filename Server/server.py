import Controller
from socket import *
import threading
import thread
import time

Controller.initWorld()

# def sendAndSetTimer(sock,thread):
#   print 'timer for thread',threading.current_thread().name
#   if Controller.isPlayer(thread):
#     Controller.sendWorldSection(sock,thread)
#     t = threading.Timer(0.05,sendAndSetTimer,[sock,thread])
#     t.start()

def handler(clientsock,addr):
  clientsock.sendall("320 320 7 7 \n")
  threadName = threading.current_thread().name
  threadDat = threading.local()
  threadDat.time = time.time()
  while 1:
    try:
      data = clientsock.recv(BUFSIZ)
      print 'caught data',data
      Controller.handleInput(data,clientsock,threadName)
    except:
      pass
    if not Controller.isPlayer(threadName):
      break
    if (time.time() - threadDat.time > 0.1):
      threadDat.time = time.time()
      Controller.sendWorldSection(clientsock,threadName)

if __name__=='__main__':
  HOST = 'localhost'
  PORT = 9999
  BUFSIZ = 1024
  ADDR = (HOST, PORT)
  serversock = socket(AF_INET, SOCK_STREAM)
  serversock.bind(ADDR)
  serversock.listen(5)

  while 1:
    print 'waiting for connection...'
    clientsock, addr = serversock.accept()
    clientsock.setblocking(0)
    print '...connected from:', addr
    thread.start_new_thread(handler, (clientsock, addr))