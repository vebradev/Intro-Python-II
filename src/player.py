# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=None):
        self.name = name
        self.location = location
        self.items = items

    def __str__(self):
        output = f"{self.name}, you entered {self.location}."
        if self.items:
            output += " Items:"
            for i in self.items:
                if self.items[-1] == i:
                    output += f" {i}"
                else:
                    output += f" {i},"
            output += "."
            return output
        return output


# p1 = Player("Michael", "Loc 1")
# p2 = Player("Michael", "Loc 2", ["Item 1", "Item 2", "Item 3"])
# p3 = Player("Michael", "Loc 3", ["Item 1"])

# print(p1)
# print(p2)
# print(p3)