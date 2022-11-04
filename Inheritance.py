class GameObject: # this is now the superclass

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

# create a subclass that inherits from GameObject class
class Enemy(GameObject):

    # implement different initializer function with additional attributes
    def __init__(self, name, x_pos, y_pos, health):
        super().__init__(name, x_pos, y_pos)
        self.health = health
    
