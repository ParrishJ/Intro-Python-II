# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def set_room(self, new_room):
        self.current_room = new_room

    def get_item(self, new_item):
        self.inventory.append(new_item)
        new_item.on_take()

    def drop_item(self, dropped_item):
        self.inventory.remove(dropped_item)
        dropped_item.on_drop()

    def get_inventory(self):
        print(f"You Hold: {'; '.join(map(str, self.inventory))}.")

    def __repr__(self):
        return f"Name: {self.name}, Current Room: {self.current_room}"