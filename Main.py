# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 00:14:59 2021

@author: bunyamin anil
"""
from ziplama import game 
g = game()

while g.running:

    g.current_menu.display_menu()
    g.gameloop()