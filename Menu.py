# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:22:03 2021

@author: bunyamin anil
"""

import pygame
from pygame import mixer
pygame.init()



class menu():
    def __init__(self, game):
        self.game = game
        self.mid_w = game.pcw/2
        self.mid_h = game.pch/2
        self.run_display = True
        self.cursor = pygame.Rect(0,0,20,20)
        self.offset = -100    
        
    def draw_cursor(self):
        self.game.draw_text('*', 30, self.cursor.x, self.cursor.y)
        
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()    
        self.game.reset_keys()            
            
        
class mainmenu(menu):
    
    def __init__(self, game):
        menu.__init__(self, game)
        self.state = "start"
        self.startx = self.mid_w
        self.starty = self.mid_h + 30        
        self.optionsx = self.mid_w
        self.optionsy = self.mid_h + 50
        self.creditsx = self.mid_w
        self.creditsy = self.mid_h + 70
        self.quitx = self.mid_w
        self.quity = self.mid_h + 90
        self.cursor.midtop = (self.startx + self.offset, self.starty)
        game.state = 'menu'
        self.bg = pygame.image.load('raindrop_bg.png')
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0,0,0))
            self.game.display.blit(self.bg, ((0,0)))
            self.game.draw_text('Main Menu', 40 , self.game.pcw/ 2, self.game.pch / 2 - 30)
            self.game.draw_text('start game', 20, self.startx, self.starty)
            self.game.draw_text('options', 20, self.optionsx, self.optionsy)
            self.game.draw_text('explanation', 20, self.creditsx, self.creditsy)
            self.game.draw_text('Quit Game', 20, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()

            
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "start":
                self.cursor.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "options"
            elif self.state == "options":
                self.cursor.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "credits"
            elif self.state == "credits":
                self.cursor.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit Game"
            elif self.state == "Quit Game" :
                self.cursor.midtop = (self.startx + self.offset, self.starty)    
                self.state == "start"
            else:
                self.cursor.midtop = (self.startx + self.offset, self.starty)
                self.state = "start"
                
        if self.game.UP_KEY:
            if self.state == "start":
                self.cursor.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit Game"
                
            elif self.state == "Quit Game" :
                self.cursor.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state == "credits"
                
            elif self.state == "credits":
                self.cursor.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "options"    
                                
            elif self.state == "options":
                self.cursor.midtop = (self.startx + self.offset, self.starty)
                self.state = "start"
            else:
                self.cursor.midtop = (self.startx + self.offset, self.starty)
                self.state = "start"
     
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "start":
#                mixer.music.load('kola2.mp3')
#                mixer.music.play(-1)
                self.game.playing = True
            elif self.state == "options":
                self.game.current_menu = self.game.options
            elif self.state == "credits":
                self.game.current_menu = self.game.credits
            elif self.state == "Quit Game" :
                self.game.current_menu = self.game.quit
            
            self.run_display = False
  

          
class options(menu):
    def __init__(self, game):
        menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor.midtop = (self.volx + self.offset, self.voly)
        self.bg = pygame.image.load('raindrop_bg.png')


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0,0,0))
            self.game.display.blit(self.bg, ((0,0)))
            self.game.draw_text('options', 30, self.game.pcw/2, self.game.pch/2-30)
            self.game.draw_text('Volume', 20, self.volx, self.voly)
            self.game.draw_text('Controls', 20, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()
            
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor.midtop = (self.controlsx + self.offset, self.controlsy)
        
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            #volume sg ama controls yapabilirsin
            pass
            
class Credits(menu):
    def __init__(self, game):
        menu.__init__(self, game)
        self.bg = pygame.image.load('raindrop_bg.png')

        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False                
        
            self.game.display.fill((0,0,0))
            self.game.display.blit(self.bg, ((0,0)))
            self.game.draw_text('explanation', 30, self.game.X1/2, self.game.Y1/2-20)
            self.game.draw_text('In this game you have to get to the moon ', 20, self.game.X1/2, self.game.Y1/2+10)
            self.game.draw_text('in order to move on ', 20, self.game.X1/2, self.game.Y1/2+30)
            self.game.draw_text('- WASD to move ', 23, self.game.X1/2 - 100, self.game.Y1/2+80)
            self.game.draw_text('- SPACE to stop sticking on certain tiles ', 23, self.game.X1/2 - 10, self.game.Y1/2+110)
            self.game.draw_text('- LEFT CONTROL to accelerate', 23, self.game.X1/2 - 30, self.game.Y1/2+140)
            self.blit_screen()
            
class Quit(menu):
    def __init__(self, game):
        menu.__init__(self, game)
        self.state = 'no'
        self.yesx, self.yesy = self.mid_w, self.mid_h + 50
        self.nox, self.noy = self.mid_w, self.mid_h + 80
        self.cursor.midtop = (self.yesx + self.offset, self.yesy)
        self.bg = pygame.image.load('raindrop_bg.png')

        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False 
            self.check_input()            
            self.game.display.fill((0,0,0))
            self.game.display.blit(self.bg, ((0,0)))
            self.game.draw_text('Do you want to exit?', 25, self.game.pcw/2, self.game.pch/2)
            self.game.draw_text('yes', 30, self.yesx, self.yesy)
            self.game.draw_text('no', 30, self.nox, self.noy)
            self.draw_cursor()
            self.blit_screen()
            
            
    def check_input(self):
        if self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'yes':
                self.cursor.midtop = (self.nox + self.offset, self.noy)
                self.state = 'no'
                
            elif self.state == 'no':
                self.cursor.midtop = (self.yesx + self.offset, self.yesy)
                self.state = 'yes'
                
        if self.state == 'yes' :
            keys = pygame.key.get_pressed()
                #sol'a kay
            if keys[pygame.K_RETURN]:
                        self.game.running, self.game.playing = False, False
                        self.run_display = False
                        pygame.quit() 
  
