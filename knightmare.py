#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:40:31 2021

@author: dan
"""

import numpy as np
import random

class Dungeon:
    def __init__(self, dungeon_name):
        self.dungeon_map = np.array([[1, 2, 3],
                                     [4, 5, 6],
                                     [7, 8, 9]])
        self.dungeon_name = dungeon_name
        print (f"Dungeon {dungeon_name} created")
    
class Room:
    def __init__(self, room_num, dungeon, item_list):
        self.room_num = room_num
        self.dungeon = dungeon
        self.item_list = item_list
        
    def display_available_items(self):
        print ("List of items in this room :")
        
        for item in self.item_list:
            print (item)
            
class Dungeoneer:
    def __init__(self, name):
        self.name = name
        self.helmet_of_justice_on = False
        self.pouch = []
        self.current_room = 0
        self.current_dungeon_name = ""
        
    def put_on_helmet_of_justice(self):
        self.helmet_of_justice_on = True
        
    def enter_dungeon(self, dungeon):
        if self.helmet_of_justice_on == True:
            print (f"Entering dungeon {dungeon.dungeon_name}")
            self.current_dungeon_name = dungeon.dungeon_name
            return True
        else:
            print ("Cannot enter dungeon without Helmet of Justice")
            return False
                
    def pick_up_item(self, room):
        room.display_available_items()
        chosen_item = random.choice(room.item_list)
        print (f"Taken the {chosen_item}")
        room.item_list.remove(chosen_item)
        self.pouch.append(chosen_item)
        
    def drop_item(self, item):
        print (f"Attempting to drop {item}")
        
        if item in self.pouch:
            self.pouch.remove(item)
            print (f"You have dropped {item}")
        else:
            print (f"You are not carrying {item}")
        
dans_dungeon = Dungeon("Dan's Dungeon")
hsma_room = Room(8, dans_dungeon, ["Bread", "Apple", "Potion", "Scroll"])
dan_the_dungeoneer = Dungeoneer("Dan")

dan_the_dungeoneer.put_on_helmet_of_justice()
entered_dungeon = dan_the_dungeoneer.enter_dungeon(dans_dungeon)

if entered_dungeon == True:
    dan_the_dungeoneer.pick_up_item(hsma_room)
    dan_the_dungeoneer.pick_up_item(hsma_room)
    print ("Pouch contents : ")
    print (dan_the_dungeoneer.pouch)
    
