import pygame
import os

class Entity:
  def __init__(self,x,y,Id,ws):
    self.x = x
    self.y = y
    self.id = Id
    self.ws = ws

class Rock(Entity):
  def __init__(self,x,y,Id,ws):
    Entity.init(self,x,y,Id,ws)
    self.sprite = pygame.image.load(os.path.join('Assets','rock.png'))
