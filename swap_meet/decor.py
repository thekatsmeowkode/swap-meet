from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = None, condition = None, age = None, name = None, width = None, length = None):
        super().__init__(id, condition, age, name = "Decor")
        self.width = width if width else 0
        self.length = length if length else 0
    
    def __str__(self):
        return f"{Item.__str__(self)} It takes up a {self.width} by {self.length} sized space."