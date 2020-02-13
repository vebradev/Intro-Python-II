from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", [Item("stick", "wet, short and not very useful"), Item("rock", "fits perfectly in your palm")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("showel", "rusty, but still does the job")]),

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
    'name_input': "What is your name, young grasshopper?\nName: ",
    'warning_dir': "No such direction from this room."
}
# location = room['outside']

print(messages["welcome"])
name = input(messages["name_input"])

# Make a new player object that is currently in the 'outside' room.

player = Player(name, room['outside'])
status = True if player.name else False

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

commands = ["n", "e", "s", "w", "q", "get", "drop"]

while status:
    print("\n======================================================\n")
    print(f"{player}")
    user_input = input("\nTo change direction, enter: \"n\", \"e\", \"s\", \"w\". \nTo perform action, enter: \"take [item]\" or \"drop [item]\"\nCommand: ")
    
    if len(user_input) == 1:
        direction = user_input[0]
        if direction == "q":
            print("Thanks for playing.")
            status = False
        elif direction in commands[:4]:
            dir_attr = direction + "_to"
            if hasattr(player.location, dir_attr):
                player.location = getattr(player.location, dir_attr)
            else:
                print("Direction does not exist. Look around.")
        else:
            print("Command not found.")
    elif len(user_input) >= 2:
        command = user_input.split()[0]
        print(command)
        pass
    # status = False

# while status:
# print(f"\n{player}")

# action = input("\nWhich direction do you want to move?\nN, E, S, W: ").lower()

# if len(action) == 1:
#     if action[0] == "n":
#         if hasattr(player.location, "n_to"):
#             print(f"{player.name} decided to move North.")
#             player.location = location.n_to
#             location = location.n_to
#         else:
#             print(messages["warning_dir"])
#     elif action[0] == "e":
#         if hasattr(player.location, "e_to"):
#             print(f"{player.name} decided to move East.")
#             player.location = location.e_to
#             location = location.e_to
#         else:
#             print(messages["warning_dir"])
#     elif action[0] == "s":
#         if hasattr(player.location, "s_to"):
#             print(f"{player.name} decided to move South.")
#             player.location = location.s_to
#             location = location.s_to
#         else:
#             print(messages["warning_dir"])
#     elif action[0] == "w":
#         if hasattr(player.location, "w_to"):
#             print(f"{player.name} decided to move West.")
#             player.location = location.w_to
#             location = location.w_to
#         else:
#             print(messages["warning_dir"])
#     elif action[0] == "q":
#         print(f"Thanks for playing {player.name}. Bye for now!")
#         status = False
#     else:
#         print("No such direction.")
# elif len(action) >= 2:
#     commands = action.split()
#     print(f"{commands}")
# else:
#     status = False
