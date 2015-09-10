import pygame
import os

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