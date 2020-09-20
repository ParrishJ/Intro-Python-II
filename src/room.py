# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    
    def __repr__(self):
        return f"You find yourself in a new area: {self.name}. {self.description} In this area, you see a number of items - {'; '.join(map(str, self.items))}"