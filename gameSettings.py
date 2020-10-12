# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:50:23 2020

@author: LethalValdi
"""

class GameSettings():
    """Class for game settings,"""
    def __init__(self):
        #Initialize game settings
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (0,0,0)
        #Bullets were not used in final version
        self.bulletSpeed = 2
        self.bulletWidth = 15
        self.bulletHeight = 15
        self.bulletColor = 50,150,50
        self.speed =3
        self.counter = 30

        