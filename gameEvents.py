# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:55:40 2020

@author: LethalValdi
"""


import pygame
import random
from bullet import Bullet
from alienSettings import Alien




def checkEvents(mySettings,screen,aliens,playButton,stats,quitButton,score): 
    """Check for events and respond """
    for event in pygame.event.get(): 
        # Quit game if we exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # If we click the mouse we do stuff
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #If game is not started we check if we click on start or quit 
            if(stats.activateGame == False):
                mouseX, mouseY = pygame.mouse.get_pos()
                checkPlayButton(stats, playButton, mouseX, mouseY)
                checkQuitButton(quitButton,mouseX,mouseY)
            else:
            # if game is active we check if we have clicked on an alien and remove it and add a new one and points
                for als in aliens:
                    if als.rect.collidepoint(event.pos):
                        aliens.remove(als)
                        newAlien = Alien(screen,als.idNum)
                        aliens.add(newAlien)
                        stats.currentScore += als.points


def checkPlayButton(stats,playButton,mouseX,mouseY):
    if playButton.rect.collidepoint(mouseX,mouseY):
        stats.activateGame = True
        stats.gameOver = False
        stats.currentScore = 0
#Do same but for quit button, quit game if pushed
def checkQuitButton(quitButton,mouseX,mouseY):
    if quitButton.rect.collidepoint(mouseX,mouseY):
        pygame.quit()
        exit()

        
# Function for using bullets, later not used but kept in for future versions
def updateBullets(bullets,aliens):
    
    bullets.update()
    
    for bullet in bullets.copy():
        if (bullet.rect.x == 1200 or bullet.rect.y == 0 or bullet.rect.y == 800):
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

#Update the screen in th game
def updateScreen(mySettings,screen,aliens,playButton,stats,quitButton,title,score,milliSecs):
    screen.fill(mySettings.bgColor)
    # Game is over we let player know his score and let him play again
    if stats.activateGame == False:
        if stats.gameOver == True:
            score.showScore("Game over, you scored: " + str(stats.currentScore) + " points",150,50,50 )
        else:
            title.drawButton()
            
        playButton.drawButton()
        #Draw aliens and the corresponding score for each alien on start screen to let player know how much each alien is worth
        staticAlien = Alien(screen,-1)
        staticAlien.drawStaticAliens()
        score.showScore(" 1",200,605,80)
        score.showScore(" 3",600,605,80)
        score.showScore(" 5",1000,605,80)
        quitButton.drawButton()
    # If game is active we update the score and the seconds left in game
    else:
        score.showScore(stats.currentScore,1100,700,58)
        score.showScore(milliSecs,550,350,72)
        # We draw the aliens and update their movement
        for als in aliens.sprites():
            arr = [1,2,3,4,5,6,7,8]  #pick random number from 1 to 8 for moevement
            als.drawAlien()
            #als.theArr.append(myNumber)
            #Stupid logic for making aliens not allowed to move back in next movement, need to find better way
            
            # Each alien moves 10 times in same direction and then we update movement, done so aliens move more smoothly
            if(als.myCounter  % 10 == 0):
                als.theNum = random.choice(arr)
            # Update position of alien with random movement created
            als.updatePos(als.theNum)
            als.myCounter+=1
            #print(als.myCounter)
            #print(als.num)
    
    #Bullet stuff not used, maybe used in future versions
  #  for bullet in bullets.sprites():
     #   bullet.drawBullet()
        #als.updatePos()
        
        
                
        
    
            
    

