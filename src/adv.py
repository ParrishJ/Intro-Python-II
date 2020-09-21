from room import Room
from player import Player
from food import Food
import sys

# Items

bread = Food("Stale Bread", "an old, crumbly slice of bread", "Disgusting")

apple = Food("Apple", "a ripe, juicy apple", "Delicious")

candy = Food("Candy", "a small piece of wrapped candy", "Delicious")

oatmeal = Food("Oatmeal", "a bowl of plain, unflavored oat meal", "Bland")

radish = Food("Radish", "a red root vegatable", "Spicy")

stew = Food("Stew", "a warm bowl of stew", "Delicious")

lemon = Food("Lemon", "a ripe, yellow lemon", "Sour")

cheeseburger = Food("Cheeseburger", "a yummy cheeseburger", "Delicious")

melon = Food("Melon", "a ripe, green melon", "Delicious")

pepper = Food("Pepper", "a red pepper", "Spicy")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [candy, oatmeal]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [radish, stew]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [lemon, cheeseburger]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [melon, pepper]),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
JP = Player('JP', 'outside', None)

def navigation():
    JP.set_room(room[JP.current_room])
    print('You find yourself in a new area:', JP.current_room.name)
    print(JP.current_room.description) 
    command_list = str(input("[n] North [e] East [s] South [w] West, [i] Inventory [q] Quit  \n")).split()
    direction = command_list[0]
    while not direction == 'q':
        if direction == 'n':
            try:
                JP.set_room(JP.current_room.n_to)
                print(JP.current_room)
            except:
                print("You cannot move to this area")
        if direction == 'e':
            try:
                JP.set_room(JP.current_room.e_to)
                print(JP.current_room)
            except:
                print("You cannot move to this area")
        if direction == 's':
            try:
                JP.set_room(JP.current_room.s_to)
                print(JP.current_room)
            except:
                print("You cannot move to this area")
        if direction == 'w':
            try:
                JP.set_room(JP.current_room.w_to)
                print(JP.current_room)
            except:
                print("You cannot move to this area")
        if direction == 'i':
           JP.get_inventory() 
        if command_list[0] == 'get':
            pickup_item_str = command_list[1]
            is_in_inventory = False
            for item in JP.current_room.items:
                if pickup_item_str == item.name.lower():
                    is_in_inventory = True
                    JP.get_item(item)
                    JP.current_room.items.remove(item)
            if is_in_inventory == False:
                print('There is no such item to pick up.')
        if command_list[0] == 'drop':
                dropped_item_str = command_list[1]
                is_in_inventory = False
                for item in JP.inventory:
                    if dropped_item_str == item.name.lower():
                        is_in_inventory = True
                        JP.drop_item(item)
                        JP.current_room.items.append(item)
                if is_in_inventory == False:
                    print("There is no such item to drop.")
        command_list = str(input("[n] North [e] East [s] South [w] West, [g] Get, [d] Drop, [i] Inventory, [q] Quit  \n")).split()
        direction = command_list[0]

navigation()