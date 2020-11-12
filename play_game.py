import json
import time
from datetime import datetime 
start_time = datetime.now() 

def main():
    game_choice = int(input("Which game would you like to play? 1. Spooky Mansion or 2. Adventure? or 3. Stroll around Battell \n"))
    if game_choice == 1:
        choice = 'spooky_mansion.json'
    if game_choice == 2:
        choice = 'adventure.json'
    if game_choice == 3:
        choice = 'battell.json'
    with open(choice) as fp:
        game = json.load(fp)
    print_instructions()
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)


def play(rooms):
    current_place = rooms['__metadata__']['start']
    stuff = ['Cell Phone; no signal or battery...','Credit Card','Birthday Cake','Dust']
    visited = {}

    while True:
        print("")
        here = rooms[current_place]
        print(here["description"])
                
        if current_place in visited:
            print("... You've been in this room before.")
        visited[current_place] = True
        
        for i in (here["items"]):
            print("There is a", i,"!!!!!!!!!!")

        if here.get("ends_game", False):
            break

        visible_exits = find_visible_exits(here, stuff)
        for i, exit in enumerate(visible_exits):
            print("  {}. {}".format(i+1, exit['description']))

        action = input("> ").lower().strip()
        print(" ----> you typed: ", action)

        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        
        if action == "help":
            print_instructions()
            continue
        
        if action == "stuff":
            if stuff == []:
                print("You have no items.")
            else:
                print("You have: ",stuff)
            continue
        
        if action == "take":
            print("You grabbed",here["items"])
            stuff.extend(here["items"])
            here["items"].pop()
            continue
                
        if action == "drop":
            a = str(input("Which item would you like to remove? \n"))
            try:
                stuff.remove(a)
                here["items"].append(a)
                print("You dropped",a)
                print("You have",stuff)
            except:
                print("You don't have a",a," \n Try again.")
            continue

        if action == "search":
            for exit in here['exits']:
                if exit.get("hidden", False):
                    exit["hidden"] = False

        try:
            num = int(action) - 1
            selected = visible_exits[num]
            if 'required_key' in selected:
                if selected["required_key"] not in stuff:
                    print("You try to open the door, but it's locked!")
                    continue
                else:
                    print("You unlock the door.")      
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))        
        
    print("")
    print("")
    print("=== GAME OVER ===")
    time_elapsed = datetime.now() - start_time 
    print("You were trapped in this game for {} (hh:mm:ss.ms)".format(time_elapsed))

def find_visible_exits(room,stuff):
    visible = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        visible.append(exit)
    return visible

def no_bridge_to_nowhere(rooms):
    list_of_rooms = []
    for room in rooms:
        list_of_rooms.append(room["name"])
    for room in rooms:
        for i in range(len(room["exits"])):
            if room["exits"][i]["destination"] not in list_of_rooms:
                print("Not in List")
                
def find_non_win_rooms(game): #ATTEMPTED
    keep = []
    for room_name in game.keys():
        if room_name == '__metadata__':
            continue
        if game[room_name].get('ends_game', False):
            continue
        keep.append(room_name)
    return keep

def print_instructions():
    print("")
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' to take a deeper look at a room.")
    print(" - Type 'help' if you need to look at the instructions again.")
    print("=== Instructions ===")
    print("")

if __name__ == '__main__':
    main()