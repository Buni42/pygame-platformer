# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:07:35 2021

@author: bunyamin anil
"""

import pygame
import button
#import csv 
import pickle

pygame.init()

# window
Screen_Height = 800
Screen_Width = 1400
Side_Margin = 300
Lower_Margin = 100


# grid vars
max_row = 16
max_col = 28
tile_size = 50
tile_types = 16
level = 0

# vars
screen = pygame.display.set_mode((Screen_Width + Side_Margin, Screen_Height))
pygame.display.set_caption('level editor')

# png's
kirmizi_img = pygame.image.load('Decor_Brick.png')

catapultdown = pygame.transform.rotate(kirmizi_img, 180)      
# catapult tiles left
catapultleft = pygame.transform.rotate(kirmizi_img, 90) 
# catapult tiles right
catapultright = pygame.transform.rotate(kirmizi_img, -90) 

diken_img = pygame.image.load('Spikes.png')
    # down thorn
down_diken_img = pygame.transform.rotate(diken_img, 180)
    # horizontal : left thorn
left_diken_img = pygame.transform.rotate(diken_img, 90)
    # horizontal : left thorn
right_diken_img = pygame.transform.rotate(diken_img, -90)

skose_diken_img = pygame.image.load('skose_diken4.png')
    # left corner thorn
lkose_diken_img = pygame.image.load('lkose_diken3.png')
    # up right corner thorn
upskose_diken_img = pygame.transform.rotate(skose_diken_img, 90)
    # up left corner thorn
uplkose_diken_img = pygame.transform.rotate(lkose_diken_img, -90)

longest_diken = pygame.transform.scale(down_diken_img, (tile_size, int(tile_size * 2 )))
long_diken = pygame.transform.scale(down_diken_img, (tile_size, int(tile_size * 1.65 )))

# walls
stone_img = pygame.image.load('Brick_01.png')
# door / portal
    # looks like the moon
ay_door = pygame.image.load('Moon_asset.png')
empty_it = pygame.image.load('dead.png')


# load and save images
load_img = pygame.image.load('l.png')
save_img = pygame.image.load('s.png')

font = pygame.font.SysFont('modernno20', 20, False, False)

def drawgrid():
    for c in range(max_col + 1):
        pygame.draw.line(screen, (255,255,255), (c * tile_size, 0), (c * tile_size, Screen_Height))
        
    for c in range(max_row + 1):
        pygame.draw.line(screen, (255,255,255), (0, c * tile_size), (Screen_Width, c * tile_size))
        
        
def bg_draw():
    screen.blit(pygame.image.load('sky.png'), (0,0))

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

imgindex = 0 
maximgindex = 15
# store tiles in list
img_list = [
    empty_it,
    stone_img,
    kirmizi_img ,
    diken_img ,
    long_diken,
    ay_door,
    down_diken_img,
    left_diken_img,
    right_diken_img,
    skose_diken_img,
    lkose_diken_img,
    upskose_diken_img,
    uplkose_diken_img,
    catapultdown,
    catapultleft  ,
    longest_diken,
    catapultright ,
]

while imgindex <= maximgindex:
    for i in img_list:
       img_list[imgindex] =  pygame.transform.scale(img_list[imgindex], (tile_size, tile_size))
       imgindex += 1
       
    
#create empty tile list
world_data = []
for row in range(max_row):
	r = [0] * max_col
	world_data.append(r)
    
    
print(world_data)


#function for drawing the world tiles
def draw_world():
	for y, row in enumerate(world_data):
		for x, tile in enumerate(row):
			if tile > 0:
				screen.blit(img_list[tile], (x * tile_size, y * tile_size))


#make a button list
button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
	tile_button = button.Button(Screen_Width + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
	button_list.append(tile_button)
	button_col += 1
	if button_col == 3:
		button_row += 1
		button_col = 0
        
        
save_button = button.Button(1450 , 700, save_img, 1)
load_button = button.Button(1450 + 150, 700, load_img, 1)


run = True
while run:
    bg_draw()
    drawgrid()
    draw_world()
    

    draw_text(f'Level: {level}',font, (255,255,255), 1450, 600)
    draw_text('Press UP or DOWN to change level', font, (255,255,255), 1450, 650)
    
    if save_button.draw(screen):
        pickle_out = open(f'level{level}_data', 'wb')
        pickle.dump(world_data, pickle_out)
        pickle_out.close()
    
    # the csv method --> good if you want to read the file
#        with open(f'level{level}_data.csv', 'w', newline = '') as csvfile:
#            writer = csv.writer(csvfile, delimiter = ',')
#            for row in world_data:
#                writer.writerow(row)
                
        pygame.draw.rect(screen, (0,255,0), save_button.rect, 3) 
            
    if load_button.draw(screen):
        world_data = []
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
        
    # the csv method --> good if you want to read the file
#        with open(f'level{level}_data.csv', newline = '') as csvfile:
#            reader = csv.reader(csvfile, delimiter = ',')
#            for x, row in enumerate(reader):
#                for y, tile in enumerate(row):
#                    world_data[x][y] = int(tile)
                    
        pygame.draw.rect(screen, (0,255,0), load_button.rect, 3)
    
#    choose a tile
    button_count = 0
    for button_count,i in enumerate(button_list):
        if i.draw(screen):
            current_tile = button_count
            #highlight the selected tile
            pygame.draw.rect(screen, (255,0,0), button_list[current_tile].rect, 3)
    

	#get mouse position
    pos = pygame.mouse.get_pos()
    x = pos[0]  // tile_size
    y = pos[1] // tile_size

    #check that the coordinates are within the tile area
    if pos[0] < Screen_Width and pos[1] < Screen_Height:
        #update tile value
        if pygame.mouse.get_pressed()[0] == 1:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile
        if pygame.mouse.get_pressed()[2] == 1:
            world_data[y][x] = 0
    
    for event in pygame.event.get():
    # quit editor by pressing the X
        if event.type == pygame.QUIT:
            run = False
    # change the level you're working on 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            if event.key == pygame.K_DOWN and level > 0:
                level -= 1
    
    pygame.display.update()
    
pygame.quit() 
    