# Write a class to hold player information, e.g. what room they are in
# currently.


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
                    output += f" {i}"
                else:
                    output += f" {i},"
            output += "."
            return output
        return output

    def get(self, item):
        if self.items == None:
            self.items = []
        self.items.append(item)
        print(f"{item} has been added to your inventory.")

    def drop(self, item):
        if self.items:
            if self.items.__contains__(item):
                target = self.items.index(item)
                self.items.pop(target)
                print(f"{item} has been removed from your inventory.")
            else:
                print("No such item in your inventory.")
        else:
            print("Your inventory is empty.")


# p1 = Player("Michael", "Loc 1")
# p1.get("Axe")
# p1.get("Showel")
# print(p1)
# p2 = Player("Michael", "Loc 2", ["Item 1", "Item 2", "Item 3"])
# p3 = Player("Michael", "Loc 3", ["Item 1"])

# print(p1)
# print(p2)
# print(p3)
