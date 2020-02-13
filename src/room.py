# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        output = f"Room: {self.name}. Description: {self.description}."
        if self.items:
            output += " Items:"
            for i in self.items:
                if self.items[-1] == i:
                    output += f" {i}"
                else:
                    output += f" {i},"
            output += "."
            return output
        else:
            return output


# a = Room("A ROOM", "Not so big actually", ["item", "item2"])
# b = Room("B ROOM", "Smaller than A", ["item"])
# c = Room("C ROOM", "Smallest of em all")

# print(a)
# print(b)
# print(c)