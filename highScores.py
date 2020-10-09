# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:05:40 2020

@author: LethalValdi
"""
import pygame

class PointSystem():
    def __init__(self,mySettings,screen,stats):
        self.screen = screen
        self.stats = stats
        self.mySettings = mySettings
        self.textColor = (255,255,255)
        
        

    def showScore(self,theScore,xCor,yCor,fontSize):
        self.font = pygame.font.SysFont("alienencounters", fontSize)
        scoreStr = str(theScore)
        self.scoreImage = self.font.render(scoreStr,True, self.textColor,self.mySettings.bgColor)
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.x = xCor
        self.scoreRect.y = yCor
        self.screen.blit(self.scoreImage,self.scoreRect)
            
