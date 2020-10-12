# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:30:29 2020

@author: LethalValdi
"""
import pygame
from alienSettings import resource_path


class Stats():
    """Function for counting stats, does not do much at movement but plan was to show player how many of each alien he clicked when game is over"""
    def __init__(self,gameSettings):
        self.gameSettings = gameSettings
        self.activateGame = False #We activate game and deactivate game with this boolean
        self.userName = False #Not used
        self.currentScore = 0
        self.gameOver = False 

class Button():
    def __init__(self, gameSettings,screen,msg,xCor,yCor,fontSize):
        """Initialize start and quit button"""
        self.screen = screen
        self.screenRect = screen.get_rect()
        #Create Button and select color, size et cetera
        self.width, self.height = 200,60
        self.buttonColor = (0,0,0)
        self.textColor = (150,0,255)
        self.fontSize = fontSize
        font = resource_path('fonts/alienfont.ttf')
        self.font = pygame.font.Font(font,self.fontSize)
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
        """Draw Button"""
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage,self.msgImageRect)
 
        