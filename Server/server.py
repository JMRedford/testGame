import controller
from socket import *
import threading
import thread
import time

model.initWorld()

def handler(clientsock,addr):
  clientsock.sendall("320 320 7 7 \n")
  threadName = threading.current_thread().name
  threadDat = threading.local()
  threadDat.time = time.time()
  while 1:
    try:
      data = clientsock.recv(BUFSIZ)
      controller.handleInput(data,clientsock,threadName)
    except:
      pass
    # send info to player

    # if (time.time() - threadDat.time > 0.1):
    #   threadDat.time = time.time()
    #   try:
    #     # send info to player 
    #   except:
    #     break;

def updateLoop():
  threadName = threading.current_thread().name
  threadDat = threading.local()
  threadDat.time = time.time()
  while 1:
    if (time.time() - threadDat.time > 0.08):
      threadDat.time = time.time()
      # do the model update

if __name__=='__main__':
  HOST = 'localhost'
  PORT = 9999
  BUFSIZ = 1024
  ADDR = (HOST, PORT)
  serversock = socket(AF_INET, SOCK_STREAM)
  serversock.bind(ADDR)
  serversock.listen(5)

  thread.start_new_thread(updateLoop,())

  while 1:
    print 'waiting for connection...'
    clientsock, addr = serversock.accept()
    clientsock.setblocking(0)
    print '...connected from:', addr
    thread.start_new_thread(handler, (clientsock, addr))
