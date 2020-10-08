# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:55:40 2020

@author: LethalValdi
"""

import sys
import time
import pygame
import random
from bullet import Bullet
from alienSettings import Alien






def checkEvents(mySettings,screen,bullets,aliens): 
    #pos = pygame.mouse.get_pos()
    #pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    # Check if the rect collided with the mouse pos
    # and if the left mouse button was pressed.
    # for als in alienArr:
     #   if als.collidepoint(pos) and pressed1:
        #    print("Alien clicked")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:                    
            if event.key == pygame.K_RIGHT:
                newBullet = Bullet(mySettings,screen,1)
                bullets.add(newBullet)
            if event.key == pygame.K_DOWN:
                newBullet = Bullet(mySettings,screen,2)
                bullets.add(newBullet)
            if event.key == pygame.K_UP:
                newBullet = Bullet(mySettings,screen,3)
                bullets.add(newBullet)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for als in aliens:
                #if als.idNum == 5 and als.rect.collidepoint(event.pos):  # event.pos is the mouse position.
                if als.rect.collidepoint(event.pos):
                    print("You killed alien")
                    aliens.remove(als)
                    newAlien = Alien(screen,als.idNum)
                    aliens.add(newAlien)
        
                
def updateBullets(bullets,aliens):
    
    bullets.update()
    
    for bullet in bullets.copy():
        if (bullet.rect.x == 1200 or bullet.rect.y == 0 or bullet.rect.y == 800):
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
                            
                    
def updateScreen(mySettings,screen,aliens,bullets):
    screen.fill(mySettings.bgColor)

    for als in aliens.sprites():
        arr = [1,2,3,4,5,6,7,8]
        als.drawAlien()
        #als.theArr.append(myNumber)
        #Stupid logic for making aliens not allowed to move back in next movement, need to find better way

        if(als.myCounter  % 10 == 0):
            als.theNum = random.choice(arr)
            
        
        als.updatePos(als.theNum)
        als.myCounter+=1
        #print(als.myCounter)
        #print(als.num)
        
    for bullet in bullets.sprites():
        bullet.drawBullet()
        #als.updatePos()
        
        
                
        
    
            
    

