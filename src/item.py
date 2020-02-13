class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

# item = Item("Axe", "rusty old, still sharp though.")
# print(item)
