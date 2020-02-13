# Write a class to hold player information, e.g. what room they are in
# currently.


from item import Item


class Player:
    def __init__(self, name, location, items=None):
        self.name = name
        self.location = location
        self.items = items

    def __str__(self):
        output = f"{self.name}, you are located at the {self.location}"
        if self.items:
            output += " Items:" if len(self.items) > 1 else " Item:"
            for i in self.items:
                if self.items[-1] == i:
                    output += f" {i.name}"
                else:
                    output += f" {i.name},"
            output += "."
            return output
        return output

    def get(self, item):
        if self.items == None:
            self.items = []
        self.items.append(item)
        print(f"{item.name} has been added to your inventory.")

    def drop(self, item):
        if self.items:
            target = None
            for i, v in enumerate(self.items):
                if item == v.name:
                    self.items.pop(i)
                    target = v
                    return v
            if target != None:
                print(f"{target.name} removed from inventory.")
            else:
                print(f"No such item {item} in your inventory.")
        else:
            print("Your inventory is empty.")


# p1 = Player("Michael", "Loc 1")
# p1.get(Item("Axe", "rusty"))
# p1.get(Item("Cheese", "smelly"))
# p1.get(Item("Showel", "golden"))
# print(p1)
