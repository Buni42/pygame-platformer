# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:13:22 2020

@author: bunyamin anil
"""
#from pydub import AudioSegment as ad
import pygame as pg
from pygame import mixer
from Menu import *

pg.init()

# music
mixer.music.load('More.mp3')
mixer.music.play(-1)

#lay-out
pg.display.set_caption('ZipZip')
icon = pg.image.load('ZipZip_icon.png')
pg.display.set_icon(icon)
bg = pg.image.load('War4_r.png')
restart_img = pg.image.load('restart_img.png')
restart_img = pg.transform.scale(restart_img, (120, 100))

# png's for player 
char = pg.image.load('karakter.png')
ghost = pg.image.load('dead.png')        


#lists of png for animations     
walkright = [ pg.image.load('StandingRight.png'), pg.image.load('StandingRight.png'), pg.image.load('StandingRight.png'),pg.image.load('StandingRight.png'), pg.image.load('StandingRight.png'), pg.image.load('StandingRight.png'), pg.image.load('StandingRight.png'), pg.image.load('StandingRight.png'), pg.image.load('StandingRight.png'), pg.image.load('StandingRight.png')]
walkleft = [pg.image.load('StandingLeft.png'), pg.image.load('StandingLeft.png'),pg.image.load('StandingLeft.png'), pg.image.load('StandingLeft.png'), pg.image.load('StandingLeft.png'), pg.image.load('StandingLeft.png'), pg.image.load('StandingLeft.png'), pg.image.load('StandingLeft.png'), pg.image.load('StandingLeft.png'), pg.image.load('StandingLeft.png')]
walkabove = [pg.image.load('wb.png'), pg.image.load('wb.png'),pg.image.load('wb.png'), pg.image.load('wb.png'), pg.image.load('wb.png'), pg.image.load('wb.png'), pg.image.load('wb.png'), pg.image.load('wb.png'), pg.image.load('wb.png'), pg.image.load('wb.png')]
walkdown = [pg.image.load('wu.png'), pg.image.load('wu.png'),pg.image.load('wu.png'), pg.image.load('wu.png'), pg.image.load('wu.png'), pg.image.load('wu.png'), pg.image.load('wu.png'), pg.image.load('wu.png'), pg.image.load('wu.png'), pg.image.load('wu.png')]

dashR = [pg.image.load('d1.png'),pg.image.load('d2.png'), pg.image.load('d3.png'), pg.image.load('d4.png'), pg.image.load('d5.png'), pg.image.load('d6.png'),pg.image.load('d7.png'), pg.image.load('d8.png'), pg.image.load('d9.png'), pg.image.load('d9.png'),pg.image.load('d1.png'),pg.image.load('d2.png'), pg.image.load('d3.png'), pg.image.load('d4.png'), pg.image.load('d5.png'), pg.image.load('d6.png'),pg.image.load('d7.png'), pg.image.load('d8.png'), pg.image.load('d9.png'), pg.image.load('d9.png'),pg.image.load('d1.png'),pg.image.load('d2.png'), pg.image.load('d3.png'), pg.image.load('d4.png'), pg.image.load('d5.png'), pg.image.load('d6.png'),pg.image.load('d7.png'), pg.image.load('d8.png'), pg.image.load('d9.png'), pg.image.load('d9.png')]
dashL = [pg.image.load('d1.png'),pg.image.load('d2.png'), pg.image.load('d3.png'), pg.image.load('d4.png'), pg.image.load('d5.png'), pg.image.load('d6.png'),pg.image.load('d7.png'), pg.image.load('d8.png'), pg.image.load('dr9.png'), pg.image.load('dr9.png'),pg.image.load('d1.png'),pg.image.load('d2.png'), pg.image.load('d3.png'), pg.image.load('d4.png'), pg.image.load('d5.png'), pg.image.load('d6.png'),pg.image.load('d7.png'), pg.image.load('d8.png'), pg.image.load('dr9.png'), pg.image.load('dr9.png'),pg.image.load('d1.png'),pg.image.load('d2.png'), pg.image.load('d3.png'), pg.image.load('d4.png'), pg.image.load('d5.png'), pg.image.load('d6.png'),pg.image.load('d7.png'), pg.image.load('d8.png'), pg.image.load('dr9.png'), pg.image.load('dr9.png')]
dashUP = [pg.image.load('da1.png'),pg.image.load('da2.png'), pg.image.load('da3.png'), pg.image.load('da4.png'), pg.image.load('da5.png'), pg.image.load('da6.png'),pg.image.load('da7.png'), pg.image.load('da8.png'), pg.image.load('da9.png'), pg.image.load('da9.png'),pg.image.load('da1.png'),pg.image.load('da2.png'), pg.image.load('da3.png'), pg.image.load('da4.png'), pg.image.load('da5.png'), pg.image.load('da6.png'),pg.image.load('da7.png'), pg.image.load('da8.png'), pg.image.load('da9.png'), pg.image.load('da9.png'),pg.image.load('da1.png'),pg.image.load('da2.png'), pg.image.load('da3.png'), pg.image.load('da4.png'), pg.image.load('da5.png'), pg.image.load('da6.png'),pg.image.load('da7.png'), pg.image.load('da8.png'), pg.image.load('da9.png'), pg.image.load('da9.png')]
dashDOWN = [pg.image.load('da1.png'),pg.image.load('da2.png'), pg.image.load('da3.png'), pg.image.load('da4.png'), pg.image.load('da5.png'), pg.image.load('da6.png'),pg.image.load('da7.png'), pg.image.load('da8.png'), pg.image.load('dan9.png'), pg.image.load('dan9.png'),pg.image.load('da1.png'),pg.image.load('da2.png'), pg.image.load('da3.png'), pg.image.load('da4.png'), pg.image.load('da5.png'), pg.image.load('da6.png'),pg.image.load('da7.png'), pg.image.load('da8.png'), pg.image.load('dan9.png'), pg.image.load('dan9.png'),pg.image.load('da1.png'),pg.image.load('da2.png'), pg.image.load('da3.png'), pg.image.load('da4.png'), pg.image.load('da5.png'), pg.image.load('da6.png'),pg.image.load('da7.png'), pg.image.load('da8.png'), pg.image.load('dan9.png'), pg.image.load('dan9.png')]


#data for tiles and all for level 1
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]

#clock for fps control
clock = pg.time.Clock()
fps = 60
game_over = 0


class game():
    
    def __init__(self):
        self.running, self.playing = True, False
        #keys
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        
        
        #width and height of the monitor
        self.pcw = pg.display.Info().current_w
        self.pch = pg.display.Info().current_h
        self.screen_size = [self.pcw, self.pch]
        
        #fullscreen or 1000 X 800
        self.fullscreen = False
        self.X1, self.Y1 = 1000, 800
        if self.fullscreen == True:
            self.window = pg.display.set_mode(self.screen_size, pg.FULLSCREEN)
        else:
            self.window = pg.display.set_mode((self.X1, self.Y1))
        self.display = pg.Surface((self.pcw, self.pch))
        #size of the tiles and obstacles 
        self.tile_size = 50
        
        #menu classes from Menu.py
        self.main_menu = mainmenu(self)
        self.options = options(self)
        self.credits = Credits(self)
        self.quit = Quit(self)
        self.current_menu = self.main_menu
        
        
    
    def gameloop(self):
        global game_over
        # here is the game(loop)
        while self.playing:
            #fps
           clock.tick(fps)
           self.check_events()
           
           #stops the infinte loop 
           if self.START_KEY:
                self.playing = False
                
           #handles the controls and movement of the player/man
           game_over = man.controls(game_over)
           
           #debugging 
#           print(game_over)
           
           #blits screen and handles the animtions
           redrawScreen()
           
           self.reset_keys()
           
    def check_events(self):
        for event in pg.event.get():
            #exit game by clicking the X
            if event.type == pg.QUIT:
                    self.running, self.playing = False, False
                    self.current_menu.run_display = False
                    pg.quit() 
            # exit with the 'esc' key
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running, self.playing = False, False
                    self.current_menu.run_display = False
                    pg.quit() 
                    
                #defines the 'keys' --> line 64
                if event.key == pg.K_RETURN:
                    self.START_KEY = True
                if event.key == pg.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pg.K_s:
                    self.DOWN_KEY = True
                if event.key == pg.K_w:
                    self.UP_KEY = True       
                    
#            man.controls()
    #resets key back to false
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    
    # funtion to draw text with
    def draw_text(self, text, size, x, y):
        font1 = pg.font.SysFont('modernno20', size, False, False)
        text_surface = font1.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
        


class world():
    def __init__(self, data):
        # normal red tiles 
        self.tile_list = []
        kirmizi_img = pg.image.load('ob0.png')
      
        # diken / thorn
        self.tile_list_diken = []
            # level 1 diken
        diken_img = pg.image.load('diken3.png')
            # level 2 diken
        dikenB_img = pg.image.load('dikenk.png')
        
        # walls / stones
        self.tile_list_wall = []
        stone_img = pg.image.load('stone.png')
        
        rowP = 0
        for row in data :
            colP = 0
            for tile in row:
                if tile == 1:
                    img = pg.transform.scale(stone_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_wall.append(tile)
                    
                if tile == 2:
                    img = pg.transform.scale(kirmizi_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    
                if tile == 3:
                    img = pg.transform.scale(diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)      
                    
                if tile == 4:
                    img = pg.transform.scale(dikenB_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                          
        
                colP += 1
            rowP += 1
            
        
        # draws tiles from the created lists
    def draw(self):
        
        for tile in self.tile_list:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
        for tile in self.tile_list_diken:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
        for tile in self.tile_list_wall:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
           
            

class button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        
    
    def draw(self):
        action = False
        
        #get mouse position
        mpos = pg.mouse.get_pos()
        
        # check mouseover conditions and clicked
        if self.rect.collidepoint(mpos):
            # for debug purposes 
#            print('mouse over')
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                # for debug purposes 
                print('cicked')
                self.clicked = True
        
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        #draw button
        asil.window.blit(self.image, self.rect)
        
        return action
        
        
class player():

    def __init__(self, playerx, playery, width, height):
        self.reset(playerx, playery, width, height)
        
     
# turn into dead body        
    def deadA(self, screen, game_over):

        if game_over <= -1:
            screen.blit(ghost, (self.playerx, self.playery))
            
# walk animation       
    def walkA(self, screen):
        if self.walkP + 1 >= fps:
            self.walkP = 0
        if self.standing == False:         
            if self.left:
                       screen.blit(walkleft[self.walkP//6] ,(self.playerx, self.playery))
                       self.walkP += 1
                       
            elif self.right:
                        screen.blit(walkright[self.walkP//6] ,(self.playerx, self.playery))
                        self.walkP += 1
                        
            elif self.up:
                        screen.blit(walkabove[self.walkP//6] ,(self.playerx, self.playery))
                        self.walkP += 1        
             
            elif self.down:
                        screen.blit(walkdown[self.walkP//6] ,(self.playerx, self.playery))
                        self.walkP += 1
                        
        
        else:
            if self.right:
                screen.blit(pg.image.load('StandingRight.png'), (self.playerx, self.playery))
            if self.left:
                screen.blit(pg.image.load('StandingLeft.png'), (self.playerx, self.playery))
            if self.up:
                screen.blit(pg.image.load('wb.png'), (self.playerx, self.playery))
            if self.down:
                screen.blit(pg.image.load('wu.png'), (self.playerx, self.playery))



# dash animation
    def dashA(self, screen):
        if self.dashP + 1 >= fps:
                   self.dashP = 0
                   
        if self.standing == True:
            screen.blit(char, (self.playerx, self.playery))
            
        if self.standing == False:
        
            if self.dashright:
                       screen.blit(dashR[self.dashP//3], (self.playerx, self.playery))
                       self.dashP += 1 
                       
            elif self.dashleft:
                       screen.blit(dashL[self.dashP//3], (self.playerx, self.playery))
                       self.dashP += 1 
                       
            elif self.dashup:
                       screen.blit(dashUP[self.dashP//3], (self.playerx, self.playery))
                       self.dashP += 1 
                       
            elif self.dashdown:
                       screen.blit(dashDOWN[self.dashP//3], (self.playerx, self.playery))
                       self.dashP += 1                        
                
        else:
            if self.jump == False:
                
                if self.right:
                    screen.blit(pg.image.load('StandingRight.png'), (self.playerx, self.playery))
                if self.left:
                    screen.blit(pg.image.load('StandingLeft.png'), (self.playerx, self.playery))
                if self.up:
                    screen.blit(pg.image.load('wb.png'), (self.playerx, self.playery))
                if self.down:
                    screen.blit(pg.image.load('wu.png'), (self.playerx, self.playery))
            else:
                screen.blit(pg.image.load('karakter.png'), (self.playerx, self.playery))

            
                   
# this could get its own class                  
    def controls(self, game_over):
#       global game_over  ->  bu da olabilir ama ben argument olarak yapmayi tercih ettim.
       
       if game_over >= 0:
           
            # controls and movement
           keys = pg.key.get_pressed()
           
           # go left
           if keys[pg.K_a]:
               man.playerx -= man.vel
               man.left = True
               man.right = False
               man.dashleft = False
               man.dashright = False
               man.dashdown = False
               man.dashup = False
               man.up = False
               man.down = False
               man.standing = False
               
           # go right
           elif keys[pg.K_d]:   
               man.playerx += man.vel 
               man.left = False
               man.right = True
               man.dashdown = False
               man.dashup = False
               man.dashleft = False
               man.dashright = False
               man.up = False
               man.down = False
               man.standing = False
               
            # go up   
           elif keys[pg.K_w]:
               man.playery -= man.vel      
               man.left = False
               man.right = False
               man.dashdown = False
               man.dashup = False
               man.dashleft = False
               man.dashright = False
               man.up = True
               man.down = False
               man.standing = False
               man.dashP = 0
         
           # go down   
           elif keys[pg.K_s]:  
               man.playery += man.vel    
               man.left = False
               man.right = False
               man.dashdown = False
               man.dashup = False
               man.dashleft = False
               man.dashright = False
               man.up = False
               man.down = True
               man.standing = False
               man.dashP = 0
             
        
            # the player stopped moving
           else:      
               man.standing = True
               man.walkP = 0
               man.dashP = 0
        
# this whole chunk of code is to jump but I use it to stop sticking on the floor             
           if not(man.jump):
                   
               if keys[pg.K_SPACE]:
                   man.jump = True
                   man.left = False
                   man.right = False
                   man.walkP = 0
                   man.dashP = 0
                   man.dashleft = False
                   man.dashright = False
                   man.dashdown = False
                   man.dashup = False
                   man.up = False
                   man.down = False
                   
                   
           else:
               if man.jumpP >= -10 and self.in_air == False:
                   neg = 1
                   if man.jumpP < 0:
                       neg = -1
                   man.playery -= (man.jumpP ** 2) * self.jumpheight * neg
                   man.jumpP -= 2
               else:
                   man.jump = False
                   man.jumpP = 10
    
    
# i'd say the name says it all, but this is to accelerate                    
           if man.dashup == False:
               if keys[pg.K_LCTRL] and keys[pg.K_w]:
                   man.left = True
                   man.right = False
                   man.dashleft = False
                   man.dashright = False
                   man.dashdown = False
                   man.dashup = True
                   man.up = False
                   man.down = False
                   man.standing = False
                   dashny()
                   
           if man.dashdown == False :     
               if keys[pg.K_LCTRL] and keys[pg.K_s]:
                   man.left = True
                   man.right = False
                   man.dashleft = False
                   man.dashright = False
                   man.dashdown = True
                   man.dashup = False
                   man.up = False
                   man.down = False
                   man.standing = False
                   dashy()
                   
           if man.dashleft == False  :    
               if keys[pg.K_LCTRL] and keys[pg.K_a]:
                   man.left = True
                   man.right = False
                   man.dashleft = True
                   man.dashright = False
                   man.dashdown = False
                   man.dashup = False
                   man.up = False
                   man.down = False
                   man.standing = False
                   dashnx()
                   
           if man.dashright == False :        
               if keys[pg.K_LCTRL] and keys[pg.K_d]:
                   man.left = True
                   man.right = False
                   man.dashleft = False
                   man.dashright = True
                   man.dashdown = False
                   man.dashup = False
                   man.up = False
                   man.down = False
                   man.standing = False
                   dashx()


           
# check collision for ;
           # normal tiles
           self.in_air = True
           for tile in dunya.tile_list:
               if tile[1].colliderect(self.hitbox):
                   # wallrun gibi bisey
                   if man.jumpP == 10:
                       self.playery = tile[1].top - char.get_rect().bottom
                       self.in_air = False
                       
            # diken
           for tile in dunya.tile_list_diken:
               if tile[1].colliderect(self.hitbox):
                   game_over = game_over - 1
                   #debugging 
                   print(game_over)
             
            # walls
           for tile in dunya.tile_list_wall:
               
               # collision for the left side of the tiles i.e to the right
               if tile[1].collidepoint(self.playerx + asil.tile_size, self.playery):
                   self.reset(self.playerx, self.playery, self.width, self.height)
                   self.playerx -= asil.tile_size
                   
               # collision for the right side of the tiles i.e to the left
               if tile[1].collidepoint(self.playerx - 20, self.playery):
                   self.reset(self.playerx, self.playery, self.width, self.height)
                   self.playerx += asil.tile_size
                   
               # collision for the below of the tiles i.e up
               if tile[1].collidepoint(self.playerx , self.playery - asil.tile_size  //2):
                   self.reset(self.playerx, self.playery, self.width, self.height)
                   self.playery += asil.tile_size
           
               # collision for the above of the tiles i.e down
               if tile[1].collidepoint(self.playerx , self.playery +  asil.tile_size ):
                   self.reset(self.playerx, self.playery, self.width, self.height)
                   self.playery -= asil.tile_size
               
                
               
       return game_over        

# sets the entire data of the player back to default
    def reset(self, playerx, playery, width, height):
        self.playerx = playerx
        self.playery = playery
        self.width = width
        self.height = height   
        self.vel = 10
        self.jump = False
        self.jumpP = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkP = 0
        self.dashleft = False
        self.dashright = False
        self.dashup = False
        self.dashdown = False
        self.dashP = 0
        self.standing = True
        self.hitbox = (self.playerx + 20, self.playery, 70, 70)
        self.rect = ghost.get_rect()
        self.rect.y = playery
        self.in_air = True
        self.jumpheight = 0.1
        
     

# these are the instances of the classes              
asil = game()    
dunya = world(world_data)
man = player(400, 620, 64, 64)         
restart_button = button(asil.X1 // 2 , asil.Y1 // 2, restart_img)         


# code to accelerate in ;
# in x axis
def dashx():
    if man.dashright == True:
        man.playerx += 15
        
# in y axis
def dashy():
    if man.dashdown == True:
       man.playery += 15

# in negatif x exis
def dashnx():
    if man.dashleft == True:
       man.playerx -= 15
       
# in negatif y axis
def dashny():
    if man.dashup == True:
        man.playery -= 15


# does all the blitting and drawing stuff
def redrawScreen():   
   global game_over
   asil.window.blit(bg, (0,0))
   
   dunya.draw()
   
   man.hitbox = (man.playerx -3, man.playery -3, 68, 68)
   pg.draw.rect(asil.window, (255,255,255), man.hitbox, 2)
   
      #if player is dead
   if game_over <= -1:
       if restart_button.draw():
           man.reset(400, 620, 64, 64)
           game_over = 0
   
   man.walkA(asil.window)
       
   man.dashA(asil.window)
   
   man.deadA(asil.window, game_over)

   #update window
   pg.display.update()
   
   
