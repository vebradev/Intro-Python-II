# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        output = f"{self.name}. {self.description}"
        if self.items:
            output += " " + self.list_items()
            return output
        else:
            return output

    def list_items(self):
        if self.items:
            output = "Items in the room:" if len(
                self.items) > 1 else "One item in the room:"
            for i in self.items:
                if self.items[-1] == i:
                    output += f" {i.name}"
                else:
                    output += f" {i.name},"
            output += "."
            return output
        else:
            "There are no items in this room."

    def get(self, item):
        if self.items == None:
            self.items = []
        self.items.append(item)
        print(f"{item.name} was dropped in {self.name}.")

    def drop(self, item):
        if self.items:
            for i, v in enumerate(self.items):
                if v.name == item.name:
                    self.items.pop(i)
                    return v
        else:
            print(f"No items found in {self.name}")


# a = Room("A ROOM", "Not so big actually", [
#          Item("Axe", "rusty"), Item("Showel", "goldigger")])
# b = Room("B ROOM", "Smaller than A", [Item("Cheese", "smelly")])
# c = Room("C ROOM", "Smallest of em all")

# print(a)
# print(b)
# print(c)

# apple = Item("Apple", "sweeeet")
# cup = Item("Cup", "broken as hell")