import pygame
import os

def isCollided(foo, bar):
  fooCent = [foo.x + 16, foo.y + 16]
  barCent = [bar.x + 16, bar.y + 16]
  return (pow(pow(fooCent[0]-barCent[0],2)+pow(fooCent[1]-barCent[1],2),0.5) < 30)

## Fast enough, I think.  Call this but don't look at it.
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