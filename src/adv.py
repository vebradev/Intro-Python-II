from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

messages = {
    'welcome': "\nWelcome to THE ADVENTURE GAME\n",
    'name_input': "What is your name, young grasshopper?\n",
    'dir_input': "\nWhich direction do you want to move?\nN, E, S, W: ",
    'warning_dir': "No such direction from this room."
}

print(messages["welcome"])

name = input(messages["name_input"])

location = room['outside']

status = True


# Make a new player object that is currently in the 'outside' room.

player = Player(name, location)

# Write a loop that:
#
# + Prints the current room name
# + Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while status:
    print(f"\n{player}")

    direction = input(messages["dir_input"]).upper()

    if len(direction) >= 1:
        if direction[0] == "N":
            if hasattr(player.location, "n_to"):
                print(f"{player.name} decided to move North.")
                player.location = location.n_to
                location = location.n_to
            else:
                print(messages["warning_dir"])
        elif direction[0] == "E":
            if hasattr(player.location, "e_to"):
                print(f"{player.name} decided to move East.")
                player.location = location.e_to
                location = location.e_to
            else:
                print(messages["warning_dir"])
        elif direction[0] == "S":
            if hasattr(player.location, "s_to"):
                print(f"{player.name} decided to move South.")
                player.location = location.s_to
                location = location.s_to
            else:
                print(messages["warning_dir"])
        elif direction[0] == "W":
            if hasattr(player.location, "w_to"):
                print(f"{player.name} decided to move West.")
                player.location = location.w_to
                location = location.w_to
            else:
                print(messages["warning_dir"])
        elif direction[0] == "Q":
            print(f"Thanks for playing {player.name}. Bye for now!")
            status = False
        else:
            print("No such direction.")
    else:
        status = False
