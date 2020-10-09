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
from gameStats import Button
from gameStats import Stats
from highScores import PointSystem

def runGame():
    pygame.init()
    mySettings = GameSettings()
    screen = pygame.display.set_mode((mySettings.screenWidth, mySettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    aliens = Group()
    bullets = Group()
    stats = Stats(mySettings)
    score = PointSystem(mySettings,screen,stats)
    for al in range(10):
        newAlien = Alien(screen,al)
        aliens.add(newAlien)
    playButton = Button(mySettings,screen, "Start",500,350,72)
    scoreButton = Button(mySettings,screen, "High Scores",400,450,72)
    titleText = Button(mySettings,screen, "ALIEN ENCOUNTERS", 100,50,108)
    milliSeconds = 60000 
    tempBool = False
    seconds = 0
    while True:
        if(stats.activateGame == True):
            if(tempBool == False):
                clock.tick(60)
                tempBool = True
            else:
                milliSeconds -= clock.tick_busy_loop(60)
                seconds = int(milliSeconds/1000)
                if(milliSeconds < 0):
                    stats.activateGame = False
                    stats.gameOver = True
                    tempBool = False
                    milliSeconds = 60000
                  
        ge.checkEvents(mySettings,screen,bullets,aliens,playButton,stats,scoreButton,score)
        ge.updateBullets(bullets,aliens)
        ge.updateScreen(mySettings,screen,aliens,bullets,playButton,stats,scoreButton,titleText,score,seconds)
        pygame.display.flip()

runGame()


