# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:05:40 2020

@author: LethalValdi
"""
import pygame
from alienSettings import resource_path

class PointSystem():
    """Class for counting points and displaying them"""
    def __init__(self,mySettings,screen,stats):
        self.screen = screen
        self.stats = stats
        self.mySettings = mySettings
        self.textColor = (150,0,255)
        
        
    #Function for showing the score
    def showScore(self,theScore,xCor,yCor,fontSize):
        font = resource_path("fonts/alienfont.ttf")
        self.font = pygame.font.Font(font, fontSize)
        scoreStr = str(theScore)
        self.scoreImage = self.font.render(scoreStr,True, self.textColor,self.mySettings.bgColor)
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.x = xCor
        self.scoreRect.y = yCor
        self.screen.blit(self.scoreImage,self.scoreRect)
