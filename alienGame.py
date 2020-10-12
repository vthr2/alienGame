# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:22:23 2020

@author: Valdimar Þór Ragnarsson
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
    #Initialize game
    pygame.init()
    mySettings = GameSettings()
    screen = pygame.display.set_mode((mySettings.screenWidth, mySettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    #Create Group of Aliens, that is many aliens
    aliens = Group()
    #An earlier version had a gun that shoot bullets but not used in final version 
    #bullets = Group()
    stats = Stats(mySettings) 
    score = PointSystem(mySettings,screen,stats)
    #We create 10 aliens to start 
    for al in range(10):
        newAlien = Alien(screen,al)
        aliens.add(newAlien)
    #Add buttons and text that start the game
    playButton = Button(mySettings,screen, "Start",500,350,72)
    #High score button is not used but was a planned feature, the idea was to be able to record high scores in a scoreboard
    #scoreButton = Button(mySettings,screen, "High Scores",400,450,72)
    quitButton = Button(mySettings,screen, "Quit",530,450,72)
    titleText = Button(mySettings,screen, "ALIEN ENCOUNTERS", 100,50,108)
    #You have 60 seconds in each game, every second the counter goes down by 1000 milliseconds
    milliSeconds = 60000 
    #Boolean for using clock.tick() once when game is started, 
    tempBool = False
    #Initialize variable for seconds
    seconds = 0
    #Start game loop
    while True:
        #When startr button is pushed we start counting down seconds starting from 60
        if(stats.activateGame == True):
            if(tempBool == False):
                clock.tick(60) #Before the counter starts we want to call clock.tick so we start counting after start game is played
                tempBool = True
            else:
                milliSeconds -= clock.tick_busy_loop(60) #Calculate the number of milliseconds between each call to clock.tick
                seconds = int(milliSeconds/1000) #Convert milliseconds to seconds
                if(milliSeconds < 1):
                    stats.activateGame = False # When counter hits 0 we end the game and restart the counter for a future game
                    stats.gameOver = True
                    tempBool = False
                    milliSeconds = 60000
        #Check for events for example mouse click 
        ge.checkEvents(mySettings,screen,aliens,playButton,stats,quitButton,score) 
        #Update the screen 
        ge.updateScreen(mySettings,screen,aliens,playButton,stats,quitButton,titleText,score,seconds)
        pygame.display.flip()

runGame()


