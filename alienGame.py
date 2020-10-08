# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:22:23 2020

@author: LethalValdi
"""


import pygame
from gameSettings import GameSettings
from alienSettings import Alien
import gameEvents as ge
from pygame.sprite import Group

def runGame():
    pygame.init()
    mySettings = GameSettings()
    screen = pygame.display.set_mode((mySettings.screenWidth, mySettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    aliens = Group()
    bullets = Group()
    for al in range(10):
        newAlien = Alien(screen,al)
        aliens.add(newAlien)
        
        
    while True:
        ge.checkEvents(mySettings,screen,bullets,aliens)
        ge.updateBullets(bullets,aliens)
        ge.updateScreen(mySettings,screen,aliens,bullets)
        pygame.display.flip()
        clock.tick(60)
        
runGame()


