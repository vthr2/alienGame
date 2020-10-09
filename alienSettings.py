# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:50:45 2020

@author: LethalValdi
"""
import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Model of Alien """
    def __init__(self,screen,idNum):
        super().__init__()
        self.speeds = ['Slow', 'Slow','Slow','Medium' 'Medium' , "Fast"]
        self.colors = ['Green','Green', 'Green', 'Blue', 'Red', "Red"]
        self.names = ['Sylvester', "ET", "T-1000", "T-800", "Johnny", "Dutch", "Komodo Joe", "Space Commander Jack", "Imposter","Menace", "Villain", "Terrestrial", "Destroyer", "Cosmonaut", "Soviet", "KlausTheNaziAlien", "ThirdKind", "Predator", "Titan", "Europa", "Deimos", "PlutoThePlanet", "DrAlien", "NeuralNetAlien", "JohnConnor", "CrystalSkull", "James", "TheGary", "FinalBoss2", "Colonel Cosmos", "Carl", "Justin", "Chris the friendly alien", "Chris the unfriendly alien" , "Furious George", "The Octoalien"]
        self.name = random.choice(self.names)
        self.color = random.choice(self.colors)
        self.idNum = idNum
        self.randomNumY = []
        self.randomNumX = []
        self.screen = screen
        self.clickBool = True
        self.tempArr =[9,9]
        self.myArr = [1,2,3,4]
        self.myCounter = 0
        self.randomArr = []
        self.theArr = []
        self.theNum = 0
        if(self.color == 'Green'):
            self.speed = 4
            self.points = 1
            self.image = pygame.image.load('images/greenalien.png')
        if(self.color == 'Blue'):
            self.speed = 10
            self.points = 5
            self.image = pygame.image.load('images/bluealien.png')
        if(self.color == 'Red'):
            self.speed = 7
            self.points = 3
            self.image = pygame.image.load('images/redalien.png')
        
        for number in range(20):
            self.randomArr.append(number)
        
        for i in range(50,1150):
            self.randomNumX.append(i)
        for i in range(50,800):
            self.randomNumY.append(i)
        self.XPos = random.choice(self.randomNumX)
        self.YPos = random.choice(self.randomNumY)

        self.radius = 80
        
        #Load alien and get its rect
        self.image= pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect()
       
        
        #Set position
        self.rect.x = self.XPos
        self.rect.y = self.YPos
        
    def attack(self):
        print("The Alien "+ self.name.title() + " Color: "+self.color + " speed: "+ self.speed+ " Is now Attacking")

    def dead(self):
        print("The Alien " + self.name.title()+"Is now dead")
    
  
    
    def updateColor(self):
        newCol = input("Enter new color: ")
        
        while newCol.title() not in self.colors:
            print("Only blue, green and red permitted, enter again" )
            newCol = input("Enter new color: ")

        self.color = newCol
        print("New color is " + self.color)

    def printPos(self):
        print("X position is: " + str(self.XPos)+ "Y position is: "+str(self.YPos))
        
    def updatePos(self,ranNum):
        position2(ranNum,self.rect,self.speed)

        #position(ranNum,ranNum2,self.randomMove2,self.rect)
    
    def drawAlien(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        self.updatePos()
                
    def drawStaticAliens(self):
        self.image = pygame.image.load('images/greenalien.png')
        self.image= pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect()
        #Set position
        self.rect.x = 100
        self.rect.y = 600


        self.image3 = pygame.image.load('images/redalien.png')
        self.image3= pygame.transform.scale(self.image3, (self.radius, self.radius))
        self.rect3 = self.image3.get_rect()
        #Set position
        self.rect3.x = 500
        self.rect3.y = 600
        
        
        self.image2 = pygame.image.load('images/bluealien.png')
        self.image2= pygame.transform.scale(self.image2, (self.radius, self.radius))
        self.rect2 = self.image2.get_rect()
        #Set position
        self.rect2.x = 900
        self.rect2.y = 600
        
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.image2,self.rect2)
        self.screen.blit(self.image3,self.rect3)
    
  
        
def position2(ranNum,rect,speed):
    if(ranNum ==1):
            if(rect.x > 1200):
                rect.x = 0
            else:
                rect.x += speed
            
    elif(ranNum == 2):
            if(rect.x < -50):
                rect.x = 1200
            else:
                rect.x -= speed
    elif(ranNum== 3):
            if(rect.y > 800):
                rect.y = 0
            else:
                rect.y += speed
    elif(ranNum== 4):
            if(rect.y < -50):
                rect.y = 800
            else:
                rect.y -= speed
    elif(ranNum== 5):
            if(rect.y > 800):
                rect.y =0
            elif(rect.x > 1200):
                rect.x = 0
            else:
                rect.y += speed
                rect.x += speed
    elif(ranNum== 6):
            if(rect.y > 800): 
                rect.y = 0
            elif(rect.x < -50):
                rect.x = 1200
            else:
                rect.y += speed
                rect.x -= speed
    elif(ranNum== 7):
            if(rect.y <-50):
                rect.y = 800
            elif(rect.x > 1200):
                rect.x = 0
    
            else:
                rect.y -= speed
                rect.x += speed
    elif(ranNum== 8):
            if(rect.y < -50):
                rect.y = 800
            elif(rect.x  <-50):
                rect.x = 1200
            else:
                rect.y -= speed
                rect.x -= speed
                
    else:
            if(rect.y > -50):
                rect.y -= speed
            else:
                rect.y += speed
    

#Calculate proportion of aliens, unfinished and unused, might be used in a later version. Where after a player has finished round
#Statistics could be displayed after finish of game
def countStats(alienArr):
    counter = 0
    counter2= 0
    for number in alienArr:
        if (number.color == 'Green'):
            counter= counter+1
        elif(number.color == 'Red'):
            counter2= counter2+1
            
    numberOfAls = len(alienArr)
    counter3 = numberOfAls-counter-counter2   
    print("Number of Green Aliens: " + str(counter)+ " Proportion of all: "+str((counter/numberOfAls)*100)+"%")
    print("Number of Red Aliens: " + str(counter2)+ " Proportion of all: "+str((counter2/numberOfAls)*100)+"%" )
    print("Number of Blue Aliens: " + str(counter3)+ " Proportion of all: "+str((counter3/numberOfAls)*100)+"%")
