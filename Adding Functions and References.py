class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

    # implement a move function
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

game_object = GameObject("Enemy", 1, 2)
print(game_object.name)
game_object.name = "Enemy 1"
print(game_object.name)

# accessing more properties of the game object
print(game_object.x_pos)
