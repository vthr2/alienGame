# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:30:29 2020

@author: LethalValdi
"""
import pygame




class Stats():
    def __init__(self,gameSettings):
        self.gameSettings = gameSettings
        self.activateGame = False
        self.userName = False
        self.currentScore = 0
        self.gameOver = False

class Button():
    def __init__(self, gameSettings,screen,msg,xCor,yCor,fontSize):
        """Initialize starting button"""
        self.screen = screen
        self.screenRect = screen.get_rect()
        #Create Button
        self.width, self.height = 200,80
        self.buttonColor = (0,0,0)
        self.textColor = (255,255,255)
        self.fontSize = fontSize
        self.font = pygame.font.SysFont('alienencounters',self.fontSize)
        self.rect = pygame.Rect(600,400, self.width, self.height)
        self.rect.x = xCor
        self.rect.y = yCor
        self.prepMsg(msg,xCor,yCor)
    
    def prepMsg(self,msg,xCor,yCor):
       """Turn messages into image and center the text on the button"""
       self.msgImage = self.font.render(msg,True,self.textColor,self.buttonColor)
       self.msgImageRect = self.msgImage.get_rect()
       self.msgImageRect.x = xCor
       self.msgImageRect.y = yCor

    def drawButton(self):
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage,self.msgImageRect)
        
        