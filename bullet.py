# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:13:48 2020

@author: LethalValdi
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,mySettings,screen,num):
        super().__init__()
        self.screen = screen
        self.num = num
        self.rect = pygame.Rect(0,0,mySettings.bulletWidth,mySettings.bulletHeight)
        self.rect.x = (50)
        self.rect.y = (400)
        self.y =float(self.rect.y)
        self.x = float(self.rect.x)
        self.color = mySettings.bulletColor
        self.speedFactor = mySettings.speed
    
    def update(self):
        if(self.num ==1):
            self.x+= self.speedFactor
            self.rect.x = self.x
        elif(self.num ==2):
            self.y -= self.speedFactor
            self.rect.y = self.y
        elif(self.num ==3):
            self.y+= self.speedFactor
            self.rect.y = self.y
        
    
    def drawBullet(self):

        pygame.draw.rect(self.screen,self.color,self.rect)
        
        