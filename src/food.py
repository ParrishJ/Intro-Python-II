from item import Item

class Food(Item):
    def __init__(self, name, description, taste):
        super().__init__(name, description)
        self.taste = taste
    
    def eat(self):
        print(f"You take a bite out of {self.name}. It tasts {self.taste}")

    def __str__(self):
         return f"{self.name}. It looks like {self.description}"