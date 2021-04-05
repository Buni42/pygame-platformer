# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:46:32 2021

@author: bunyamin anil
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:13:22 2020

@author: bunyamin anil
"""
#from pydub import AudioSegment as ad
import pygame as pg
from pygame import mixer
from Menu import *
import pickle
from os import path


pg.init()

# music 
mixer.music.load('music/More.mp3')
mixer.music.play(-1, 3000)
mixer.music.set_volume(0.85)

# effects
portal_fx = mixer.Sound('music/portal_fx.wav')
last_portal_fx = mixer.Sound('music/ultra_instinct.wav')

pg.display.set_mode((1400, 800))

#lay-out
pg.display.set_caption('to the moon')
icon = pg.image.load('img/Moon_asset_r.png').convert_alpha()
pg.display.set_icon(icon)
bg = pg.image.load('img/sky.png').convert_alpha()
restart_img = pg.image.load('img/restart_icon.png').convert_alpha()
restart_img = pg.transform.scale(restart_img, (120, 125))
restartgame_img = pg.image.load('img/restartgame.png').convert_alpha()
bg2 = pg.image.load('img/WV.png').convert_alpha()
bg2 = pg.transform.scale(bg2, (1400, 800))


# png's for player 
char = pg.image.load('img/karakter.png').convert_alpha()
ghost = pg.image.load('img/dead.png').convert_alpha()


#lists of png for animations     
walkright = [pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha(),pg.image.load('img/StandingRight.png').convert_alpha()]
walkleft = [pg.image.load('img/StandingLeft.png').convert_alpha(), pg.image.load('img/StandingLeft.png').convert_alpha(),pg.image.load('img/StandingLeft.png').convert_alpha(), pg.image.load('img/StandingLeft.png').convert_alpha(), pg.image.load('img/StandingLeft.png').convert_alpha(), pg.image.load('img/StandingLeft.png').convert_alpha(), pg.image.load('img/StandingLeft.png').convert_alpha(), pg.image.load('img/StandingLeft.png').convert_alpha(), pg.image.load('img/StandingLeft.png').convert_alpha(), pg.image.load('img/StandingLeft.png').convert_alpha()]
walkabove = [pg.image.load('img/wb.png').convert_alpha(), pg.image.load('img/wb.png').convert_alpha(),pg.image.load('img/wb.png').convert_alpha(), pg.image.load('img/wb.png').convert_alpha(), pg.image.load('img/wb.png').convert_alpha(), pg.image.load('img/wb.png').convert_alpha(), pg.image.load('img/wb.png').convert_alpha(), pg.image.load('img/wb.png').convert_alpha(), pg.image.load('img/wb.png').convert_alpha(), pg.image.load('img/wb.png').convert_alpha()]
walkdown = [pg.image.load('img/wu.png').convert_alpha(), pg.image.load('img/wu.png').convert_alpha(),pg.image.load('img/wu.png').convert_alpha(), pg.image.load('img/wu.png').convert_alpha(), pg.image.load('img/wu.png').convert_alpha(), pg.image.load('img/wu.png').convert_alpha(), pg.image.load('img/wu.png').convert_alpha(), pg.image.load('img/wu.png').convert_alpha(), pg.image.load('img/wu.png').convert_alpha(), pg.image.load('img/wu.png').convert_alpha()]

accR = [pg.image.load('img/d1.png').convert_alpha(),pg.image.load('img/d2.png').convert_alpha(), pg.image.load('img/d3.png').convert_alpha(), pg.image.load('img/d4.png').convert_alpha(), pg.image.load('img/d5.png').convert_alpha(), pg.image.load('img/d6.png').convert_alpha(),pg.image.load('img/d7.png').convert_alpha(), pg.image.load('img/d8.png').convert_alpha(), pg.image.load('img/d9.png').convert_alpha(), pg.image.load('img/d9.png').convert_alpha(),pg.image.load('img/d1.png').convert_alpha(),pg.image.load('img/d2.png').convert_alpha(), pg.image.load('img/d3.png').convert_alpha(), pg.image.load('img/d4.png').convert_alpha(), pg.image.load('img/d5.png').convert_alpha(), pg.image.load('img/d6.png').convert_alpha(),pg.image.load('img/d7.png').convert_alpha(), pg.image.load('img/d8.png').convert_alpha(), pg.image.load('img/d9.png').convert_alpha(), pg.image.load('img/d9.png').convert_alpha(),pg.image.load('img/d1.png').convert_alpha(),pg.image.load('img/d2.png').convert_alpha(), pg.image.load('img/d3.png').convert_alpha(), pg.image.load('img/d4.png').convert_alpha(), pg.image.load('img/d5.png').convert_alpha(), pg.image.load('img/d6.png').convert_alpha(),pg.image.load('img/d7.png').convert_alpha(), pg.image.load('img/d8.png').convert_alpha(), pg.image.load('img/d9.png').convert_alpha(), pg.image.load('img/d9.png').convert_alpha()]
accL = [pg.image.load('img/d1.png').convert_alpha(),pg.image.load('img/d2.png').convert_alpha(), pg.image.load('img/d3.png').convert_alpha(), pg.image.load('img/d4.png').convert_alpha(), pg.image.load('img/d5.png').convert_alpha(), pg.image.load('img/d6.png').convert_alpha(),pg.image.load('img/d7.png').convert_alpha(), pg.image.load('img/d8.png').convert_alpha(), pg.image.load('img/dr9.png'), pg.image.load('img/dr9.png'),pg.image.load('img/d1.png').convert_alpha(),pg.image.load('img/d2.png').convert_alpha(), pg.image.load('img/d3.png').convert_alpha(), pg.image.load('img/d4.png').convert_alpha(), pg.image.load('img/d5.png').convert_alpha(), pg.image.load('img/d6.png').convert_alpha(),pg.image.load('img/d7.png').convert_alpha(), pg.image.load('img/d8.png').convert_alpha(), pg.image.load('img/dr9.png'), pg.image.load('img/dr9.png'),pg.image.load('img/d1.png').convert_alpha(),pg.image.load('img/d2.png').convert_alpha(), pg.image.load('img/d3.png').convert_alpha(), pg.image.load('img/d4.png').convert_alpha(), pg.image.load('img/d5.png').convert_alpha(), pg.image.load('img/d6.png').convert_alpha(),pg.image.load('img/d7.png').convert_alpha(), pg.image.load('img/d8.png').convert_alpha(), pg.image.load('img/dr9.png'), pg.image.load('img/dr9.png')]
accUP = [pg.image.load('img/da1.png').convert_alpha(),pg.image.load('img/da2.png').convert_alpha(), pg.image.load('img/da3.png').convert_alpha(), pg.image.load('img/da4.png').convert_alpha(), pg.image.load('img/da5.png').convert_alpha(), pg.image.load('img/da6.png').convert_alpha(),pg.image.load('img/da7.png').convert_alpha(), pg.image.load('img/da8.png').convert_alpha(), pg.image.load('img/da9.png').convert_alpha(), pg.image.load('img/da9.png').convert_alpha(),pg.image.load('img/da1.png').convert_alpha(),pg.image.load('img/da2.png').convert_alpha(), pg.image.load('img/da3.png').convert_alpha(), pg.image.load('img/da4.png').convert_alpha(), pg.image.load('img/da5.png').convert_alpha(), pg.image.load('img/da6.png').convert_alpha(),pg.image.load('img/da7.png').convert_alpha(), pg.image.load('img/da8.png').convert_alpha(), pg.image.load('img/da9.png').convert_alpha(), pg.image.load('img/da9.png').convert_alpha(),pg.image.load('img/da1.png').convert_alpha(),pg.image.load('img/da2.png').convert_alpha(), pg.image.load('img/da3.png').convert_alpha(), pg.image.load('img/da4.png').convert_alpha(), pg.image.load('img/da5.png').convert_alpha(), pg.image.load('img/da6.png').convert_alpha(),pg.image.load('img/da7.png').convert_alpha(), pg.image.load('img/da8.png').convert_alpha(), pg.image.load('img/da9.png').convert_alpha(), pg.image.load('img/da9.png').convert_alpha()]
accDOWN = [pg.image.load('img/da1.png').convert_alpha(),pg.image.load('img/da2.png').convert_alpha(), pg.image.load('img/da3.png').convert_alpha(), pg.image.load('img/da4.png').convert_alpha(), pg.image.load('img/da5.png').convert_alpha(), pg.image.load('img/da6.png').convert_alpha(),pg.image.load('img/da7.png').convert_alpha(), pg.image.load('img/da8.png').convert_alpha(), pg.image.load('img/dan9.png').convert_alpha(), pg.image.load('img/dan9.png').convert_alpha(),pg.image.load('img/da1.png').convert_alpha(),pg.image.load('img/da2.png').convert_alpha(), pg.image.load('img/da3.png').convert_alpha(), pg.image.load('img/da4.png').convert_alpha(), pg.image.load('img/da5.png').convert_alpha(), pg.image.load('img/da6.png').convert_alpha(),pg.image.load('img/da7.png').convert_alpha(), pg.image.load('img/da8.png').convert_alpha(), pg.image.load('img/dan9.png').convert_alpha(), pg.image.load('img/dan9.png').convert_alpha(),pg.image.load('img/da1.png').convert_alpha(),pg.image.load('img/da2.png').convert_alpha(), pg.image.load('img/da3.png').convert_alpha(), pg.image.load('img/da4.png').convert_alpha(), pg.image.load('img/da5.png').convert_alpha(), pg.image.load('img/da6.png').convert_alpha(),pg.image.load('img/da7.png').convert_alpha(), pg.image.load('img/da8.png').convert_alpha(), pg.image.load('img/dan9.png').convert_alpha(), pg.image.load('img/dan9.png').convert_alpha()]


# IMPORTANT GAME VARIABLES
#clock for fps and time control
clock = pg.time.Clock()
fps = 60
current_time = 0
game_time = 0

# controls time, if 0 then player starts again (from level 1)
countdown = 120

# game state
game_over = 0

# level control
max_level = 10
level = 1

# score
moon_score = 0


# draws ingame text
def draw_text(text, text_col, size, x, y):
    font = pg.font.SysFont('modernno20', size, False, False) 
    img = font.render(text, True, text_col)
    asil.window.blit(img, (x, y))

#resets level data with pickle
def reset_level(level):
    man.reset(410, 620, 64, 64)    
    if path.exists(f'levels/level{level}_data'):
        pickle_in = open(f'levels/level{level}_data', 'rb')
        World_Data = pickle.load(pickle_in)

    dunya = world(World_Data)
    
    return dunya


font = pg.font.SysFont("Arial", 18)
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pg.Color("green"))
	return fps_text


class game():
    
    def __init__(self):
        self.running, self.playing = True, False
        #keys
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        
        
        #width and height of the monitor
        self.pcw = pg.display.Info().current_w
        self.pch = pg.display.Info().current_h
        self.screen_size = [self.pcw, self.pch]
        
        # width and height of the window if not fullscreen
        self.X1, self.Y1 = 1400, 800
        
        #fullscreen or not
        self.fullscreen = True
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
        global level
        global max_level
        global world_data
        global dunya
        global moon_score
        global game_time
        global current_time
        global countdown
           
        # here is the game(loop)
        while self.playing:
            #fps
           clock.tick(fps)
           game_time = pg.time.get_ticks()
           
           # game countdown
           if level < max_level:
               countdown -= 0.017
           # mission failed so player returns to level 1
           if countdown <= 0:
               level = 1
               world_data = []
               dunya = reset_level(level)
               game_over = 0  
               moon_score = 0
               countdown = 120
               
           self.check_events()
           #stops the infinite loop 
           if self.START_KEY:
                self.playing = False
                game_time = 0
                current_time = 0
   
           #handles the controls and movement of the player/man
           game_over = man.controls(game_over)

           
           # level completed go to the next level
           if game_over == 1:
               level += 1
               countdown += 5
               if level <= max_level:
    #               reset level
                   world_data = []
                   dunya = reset_level(level)
                   game_over = 0

               else:
                   if restart_Gbutton.draw():
        #               restart game 
                       level = 1
                       world_data = []
                       dunya = reset_level(level)
                       game_over = 0  
                       moon_score = 0
                       countdown = 120
                       mixer.music.unpause()
          
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
                    
    #resets key back to false
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    
    # funtion to draw text with for the menu's
    def draw_text(self, text, size, x, y):
        font1 = pg.font.SysFont('modernno20', size, False, False)
        text_surface = font1.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
        


class world():
    def __init__(self, data):
   # load PNG' s for tiles
        
        # catapult tiles up
        self.tile_list_catapultup = []
        kirmizi_img = pg.image.load('img/Decor_Brick.png').convert_alpha()
        
        # catapult tiles down
        self.tile_list_catapultdown = []
        catapultdown = pg.transform.rotate(kirmizi_img, 180)      
        
        # catapult tiles left
        self.tile_list_catapultleft = []
        catapultleft = pg.transform.rotate(kirmizi_img, 90) 
        
        # catapult tiles right
        self.tile_list_catapultright = []
        catapultright = pg.transform.rotate(kirmizi_img, -90) 
        
        # diken / thorn
        self.tile_list_diken = []
            # up (normal) thorn
        diken_img = pg.image.load('img/Spikes.png').convert_alpha()
            # down thorn
        down_diken_img = pg.transform.rotate(diken_img, 180)
            # horizontal : left thorn
        left_diken_img = pg.transform.rotate(diken_img, 90)
            # horizontal : left thorn
        right_diken_img = pg.transform.rotate(diken_img, -90)
            # right corner thorn
        skose_diken_img = pg.image.load('img/skose_diken4.png').convert_alpha()
            # left corner thorn
        lkose_diken_img = pg.image.load('img/lkose_diken3.png').convert_alpha()
            # up right corner thorn
        upskose_diken_img = pg.transform.rotate(skose_diken_img, 90)
            # up left corner thorn
        uplkose_diken_img = pg.transform.rotate(lkose_diken_img, -90)

        
        # walls / stones
        self.tile_list_wall = []
            # red/pink stone
        stone_img = pg.image.load('img/Brick_01.png').convert_alpha()
        
        # spawn 
        self.tile_list_spawn = []
            # looks like the moon
        ay_spawn = pg.image.load('img/Moon_asset.png').convert_alpha()
        
        # gate / portal
        self.tile_list_portal = []
        blackhole = pg.image.load('img/BlackHole.png').convert_alpha()
        moon_portal = pg.image.load('img/Back_moon.png').convert_alpha()
        
        rowP = 0
        for row in data :
            colP = 0
            for tile in row:
                # stones
                if tile == 1:
                    img = pg.transform.scale(stone_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_wall.append(tile)
                    
                  # catapult tiles  
#                  up
                if tile == 2:
                    img = pg.transform.scale(kirmizi_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_catapultup.append(tile)
#                    down
                if tile == 13:
                    img = pg.transform.scale(catapultdown, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_catapultdown.append(tile)
#                    left
                if tile == 14:
                    img = pg.transform.scale(catapultleft, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_catapultleft.append(tile)
                
#                    right
                if tile == 16:
                    img = pg.transform.scale(catapultright, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_catapultright.append(tile)
                
                 # thorns  
                if tile == 3:
                    img = pg.transform.scale(diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)   
                    
                # thorn looking down but a litle longer
                if tile == 4:
                    img = pg.transform.scale(down_diken_img, (asil.tile_size, int(asil.tile_size * 1.65 )))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                    
                 # thorn looking down but a lot longer   
                if tile == 15:
                    img = pg.transform.scale(down_diken_img, (asil.tile_size, int(asil.tile_size * 2 )))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                    
                # thorn looking down
                if tile == 6:
                    img = pg.transform.scale(down_diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                    
                # thorn looking left
                if tile == 7:
                    img = pg.transform.scale(left_diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                    
                # thorn looking right
                if tile == 8:
                    img = pg.transform.scale(right_diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                
                # thorn corner down right
                if tile == 9:
                    img = pg.transform.scale(skose_diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                
                # thorn corner down left
                if tile == 10:
                    img = pg.transform.scale(lkose_diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                
                # thorn corner up right
                if tile == 11:
                    img = pg.transform.scale(upskose_diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                
                # thorn corner up left
                if tile == 12:
                    img = pg.transform.scale(uplkose_diken_img, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_diken.append(tile)
                
                # spawn
                if tile == 5:
                    img = pg.transform.scale(ay_spawn, (100, 100))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_spawn.append(tile)   
                    
                # portal
                if tile == 17:
                    img = pg.transform.scale(blackhole, (asil.tile_size, asil.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_portal.append(tile)
                
                if tile == 18:
                    img = pg.transform.scale(moon_portal, (1200, 1200))
                    img_rect = img.get_rect()
                    img_rect.x = colP * asil.tile_size
                    img_rect.y = rowP * asil.tile_size 
                    tile = (img, img_rect)
                    self.tile_list_portal.append(tile)   
                    
        
                colP += 1
            rowP += 1
            
        
        # draws tiles from the created lists
    def draw(self):
        
        for tile in self.tile_list_catapultup:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
#            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
        for tile in self.tile_list_catapultdown:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
#            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
        for tile in self.tile_list_catapultleft:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
#            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
        for tile in self.tile_list_catapultright:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
#            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
        for tile in self.tile_list_diken:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
#            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
        for tile in self.tile_list_wall:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
#            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
    
        for tile in self.tile_list_spawn:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
#            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
            
        for tile in self.tile_list_portal:
            asil.window.blit(tile[0], tile[1])
            # draws a green rectangle around the tiles
#            pg.draw.rect(asil.window, (0,255,0), tile[1], 2)
           
            

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
#                print('cicked')
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
                screen.blit(pg.image.load('img/StandingRight.png').convert_alpha(), (self.playerx, self.playery))
            if self.left:
                screen.blit(pg.image.load('img/StandingLeft.png').convert_alpha(), (self.playerx, self.playery))
            if self.up:
                screen.blit(pg.image.load('img/wb.png').convert_alpha(), (self.playerx, self.playery))
            if self.down:
                screen.blit(pg.image.load('img/wu.png').convert_alpha(), (self.playerx, self.playery))



# accelerate animation
    def accA(self, screen):
        if self.accP + 1 >= fps:
                   self.accP = 0
                   
        if self.standing == True:
            screen.blit(char, (self.playerx, self.playery))
            
        if self.standing == False:
        
            if self.accright:
                       screen.blit(accR[self.accP//3], (self.playerx, self.playery))
                       self.accP += 1 
                       
            elif self.accleft:
                       screen.blit(accL[self.accP//3], (self.playerx, self.playery))
                       self.accP += 1 
                       
            elif self.accup:
                       screen.blit(accUP[self.accP//3], (self.playerx, self.playery))
                       self.accP += 1 
                       
            elif self.accdown:
                       screen.blit(accDOWN[self.accP//3], (self.playerx, self.playery))
                       self.accP += 1                        
                
        else:
            if self.jump == False:
                
                if self.right:
                    screen.blit(pg.image.load('img/StandingRight.png').convert_alpha(), (self.playerx, self.playery))
                if self.left:
                    screen.blit(pg.image.load('img/StandingLeft.png').convert_alpha(), (self.playerx, self.playery))
                if self.up:
                    screen.blit(pg.image.load('img/wb.png').convert_alpha(), (self.playerx, self.playery))
                if self.down:
                    screen.blit(pg.image.load('img/wu.png').convert_alpha(), (self.playerx, self.playery))
            else:
                screen.blit(pg.image.load('img/karakter.png'), (self.playerx, self.playery))

            
# controls and movement for the player                   
    def controls(self, game_over):
       global moon_score
       if game_over == 0:
            # controls and movement
           keys = pg.key.get_pressed()
           
           # go left
           if keys[pg.K_a]:
               self.playerx -= self.vel
               self.left = True
               self.right = False
               self.accleft = False
               self.accright = False
               self.accdown = False
               self.accup = False
               self.up = False
               self.down = False
               self.standing = False
               
           # go right
           elif keys[pg.K_d]:   
               self.playerx += self.vel 
               self.left = False
               self.right = True
               self.accdown = False
               self.accup = False
               self.accleft = False
               self.accright = False
               self.up = False
               self.down = False
               self.standing = False
               
            # go up   
           elif keys[pg.K_w]:
               self.playery -= self.vel      
               self.left = False
               self.right = False
               self.accdown = False
               self.accup = False
               self.accleft = False
               self.accright = False
               self.up = True
               self.down = False
               self.standing = False
               self.accP = 0
         
           # go down   
           elif keys[pg.K_s]:  
               self.playery += self.vel    
               self.left = False
               self.right = False
               self.accdown = False
               self.accup = False
               self.accleft = False
               self.accright = False
               self.up = False
               self.down = True
               self.standing = False
               self.accP = 0
             
        
            # the player stopped moving
           else:      
               self.standing = True
               self.walkP = 0
               self.accP = 0
        
    
    
# this is to accelerate                    
           if self.accup == False:
               if keys[pg.K_LCTRL] and keys[pg.K_w]:
                   self.left = True
                   self.right = False
                   self.accleft = False
                   self.accright = False
                   self.accdown = False
                   self.accup = True
                   self.up = False
                   self.down = False
                   self.standing = False
                   accny()
                   
           if self.accdown == False :     
               if keys[pg.K_LCTRL] and keys[pg.K_s]:
                   self.left = True
                   self.right = False
                   self.accleft = False
                   self.accright = False
                   self.accdown = True
                   self.accup = False
                   self.up = False
                   self.down = False
                   self.standing = False
                   accy()
                   
           if self.accleft == False  :    
               if keys[pg.K_LCTRL] and keys[pg.K_a]:
                   self.left = True
                   self.right = False
                   self.accleft = True
                   self.accright = False
                   self.accdown = False
                   self.accup = False
                   self.up = False
                   self.down = False
                   self.standing = False
                   accnx()
                   
           if self.accright == False :        
               if keys[pg.K_LCTRL] and keys[pg.K_d]:
                   self.left = True
                   self.right = False
                   self.accleft = False
                   self.accright = True
                   self.accdown = False
                   self.accup = False
                   self.up = False
                   self.down = False
                   self.standing = False
                   accx()


           
# check collision for ;
           # catapult tiles down to up
           self.in_air = True
           for tile in dunya.tile_list_catapultup:
               if tile[1].colliderect(self.hitbox):
                   if self.jumpP == 10:
                       self.playery = tile[1].top - char.get_rect().bottom
                       self.in_air = False
                       
           # catapult tiles up to down
           for tile in dunya.tile_list_catapultdown:
               if tile[1].colliderect(self.hitbox):
                   if self.jumpP == 10:
                       self.playery = tile[1].bottom + char.get_rect().top
                       
            # catapult tiles left to right
           for tile in dunya.tile_list_catapultright:
               if tile[1].colliderect(self.hitbox):
                   if self.jumpP == 10:
                       self.playerx = tile[1].left + char.get_rect().right
                       
                       
            # catapult tiles right to left
           for tile in dunya.tile_list_catapultleft:
               if tile[1].colliderect(self.hitbox):
                   if self.jumpP == 10:
                       self.playerx = tile[1].left - char.get_rect().right
                       
            # thorn
           for tile in dunya.tile_list_diken:
               if tile[1].colliderect(man.playerx + 10, man.playery + 10, 40, 40):
                   game_over -= 1
                   #debugging 
#                   print(game_over)
                   
            # spawn
           for tile in dunya.tile_list_spawn:    
               if tile[1].colliderect(self.hitbox):
                   man.reset(410, 620, 64, 64)
                   dunya.tile_list_spawn.remove(tile)
                   game_over = 0
                   moon_score += 1
                   print(moon_score)
           
            # portal (to the next level)
           for tile in dunya.tile_list_portal:
               if tile[1].colliderect(self.hitbox):
                   # normal portal 
                   if level < max_level:        
                       # play the woosh effect
                       portal_fx.play()
                   
                    # THE moon
                   if level >= max_level:
                       # pause the background music
                       mixer.music.pause()
                       # make it more dramatic
                       pg.time.delay(1000)   
                       # play the dramatic ultra instinct music 
                       last_portal_fx.play() 
                       # wait for the dramatic ultra instinct music to end
                       pg.time.delay(12000)
                  
                    # wait for the woosh effect 
                   pg.time.delay(600)   
                   game_over = 1
                   

            # walls with blowback
           for tile in dunya.tile_list_wall:
               
               # collision for the left side of the tiles i.e to the right
               if tile[1].collidepoint(self.playerx + asil.tile_size, self.playery):
                   self.playerx -= self.blowback
                   
               # collision for the right side of the tiles i.e to the left
               if tile[1].collidepoint(self.playerx - 16, self.playery):
                   self.playerx += self.blowback
                   
               # collision for the below of the tiles i.e up
               if tile[1].collidepoint(self.playerx , self.playery - 16):
                   self.playery += self.blowback
           
               # collision for the above of the tiles i.e down
               if tile[1].collidepoint(self.playerx , self.playery +  asil.tile_size ):
                   self.playery -= self.blowback
               
                
                                          
       return game_over    

# sets the entire data of the player back to default
    def reset(self, playerx, playery, width, height):
        self.playerx = playerx
        self.playery = playery
        self.width = width
        self.height = height   
        self.vel = 7
        self.jump = False
        self.jumpP = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkP = 0
        self.accleft = False
        self.accright = False
        self.accup = False
        self.accdown = False
        self.accP = 0
        self.standing = True
        self.hitbox = (self.playerx + 20, self.playery, 70, 70)
        self.rect = ghost.get_rect()
        self.rect.y = playery
        self.in_air = True
        self.jumpheight = 5
        self.blowback = 50
        
     

# these are the instances of the classes              
asil = game()
man = player(410, 620, 64, 64)         
restart_button = button(asil.X1 // 2 , asil.Y1 // 2, restart_img) 
restart_Gbutton = button(asil.X1 // 2 -100, asil.Y1 // 2-100, restartgame_img)

# load levels in
World_Data = []
if path.exists(f'levels/level{level}_data'):
    pickle_in = open(f'levels/level{level}_data', 'rb')
    World_Data = pickle.load(pickle_in)

dunya = world(World_Data)


if asil.current_menu == asil.main_menu:
    current_time = pg.time.get_ticks()


# accelerate ;
# in x axis
def accx():
    if man.accright == True:
        man.playerx += 10
        
# in y axis
def accy():
    if man.accdown == True:
       man.playery += 10

# in negatif x exis
def accnx():
    if man.accleft == True:
       man.playerx -= 10
       
# in negatif y axis
def accny():
    if man.accup == True:
        man.playery -= 10


# does all the blitting and drawing stuff
def redrawScreen():   
   global game_over
   global world_data
   global dunya
   global moon_score
   global current_time
   global game_time
   global countdown
   
   # blits the background
   asil.window.blit(bg, (0,0))
   
   # draws the tiles
   dunya.draw()
   
   # draws text on the screen
        # keeps count of collected moons
   draw_text('moons : ' + str(moon_score), (255,255,255),asil.tile_size // 2, 25 , 25)
       # keeps track of in-game time
   draw_text('time : ' + str(game_time - current_time), (255,255,255), asil.tile_size // 2, 25 , 75)
       # displays the countdown 
   draw_text('countdown : ' + str(int(countdown)), (255,255,255), asil.tile_size // 2, 25 , 125)
       # displays current level
   draw_text('level : ' + str(level) + '/' + str(max_level), (255,255,255), asil.tile_size // 2, 25 , 175)
   
   # player's hitbox
   man.hitbox = (man.playerx, man.playery, 60, 60)
   # draw player's hitbox
   pg.draw.rect(asil.window, (255,255,255), man.hitbox, 2)
       
      #if player is dead
   if game_over <= -1:
       if restart_button.draw():
           world_data = []
           dunya = reset_level(level)
           game_over = 0
           moon_score = 0

    # player's animatons
   man.walkA(asil.window)
       
   man.accA(asil.window)
   
   man.deadA(asil.window, game_over)
   
    # game completed 
   if level > max_level:
       # call the last scene
        lastscene()
        
   # blits the fps on the screen
   asil.window.blit(update_fps(), (10,0))
   
   #update window
   pg.display.update()


def lastscene():
   asil.window.blit(bg, (0,0))
   
   # draws the moon (tile)
   dunya.draw()

    # draw the end message
   restart_Gbutton.draw()
   draw_text('congratulations, you made it to the moon', (192,192,192), 50, 300, 100)
   
   #update window
   pg.display.update()
   
