# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move_to(self, direction, current_loc):
        attribute = direction + '_to'

        if hasattr(current_loc, attribute):
            return getattr(current_loc, attribute)
        
        print("You can't go that way\n")

        return current_loc