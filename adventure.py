import json

GAME = {
    '__metadata__': {
        'title': 'Adventure',
        'start': 'classroom'
    }
}

def create_room(name, description, ends_game=False):

    assert (name not in GAME)
    room = {
        'name': name,
        'description': description,
        'exits': [],
        'items': [],
    }
    
    if ends_game:
        room['ends_game'] = ends_game

    GAME[name] = room
    return room

def create_exit(source, destination, description):
    """
    Rooms are useless if you can't get to them! This function connects source to destination (in one direction only.)

    INPUTS:
     source: which room to put this exit into (or its name)
     destination: where this exit goes (or its name)
     description: how to show this exit to the user (ex: "There is a red door.")
     required_key (optional): string of an item that is needed to open/reveal this door.
     hidden (optional): set this to True if you want this exit to be hidden initially; until the user types 'search' in the source room.
    """
    if isinstance(source, str):
        source = GAME[source]
    if isinstance(destination, dict):
        destination = destination['name']
    exit = {
        'destination': destination,
        'description': description
    }
    source['exits'].append(exit)
    return exit

classroom = create_room("classroom", "You're in a lecture hall, for some reason.")
classroom["items"].append('Professor')
hallway = create_room("hallway", "This is a hallway with many locked doors.")
hallway["items"].append('Mirrors')
staircase = create_room("staircase", "The staircase leads downward.")
staircase["items"].append('Posters')
outside = create_room("outside", "You've escaped! It's cold out.", ends_game=True)
kitchen = create_room("kitchen","You're in the kitchen, for absolutely no reason.")
kitchen["items"].append('Turtles')
dungeon = create_room("dungeon", "You didn't notice the large uncovered manhole and fell to your death. Sorry.", ends_game=True) #I MADE THIS
dungeon["items"].append('Donald Trump')

create_exit(classroom, hallway, "A door leads into the hall.")
create_exit(classroom, dungeon, "You see a light in the distance.")
create_exit(hallway, classroom, "Go back into the lecture hall.")
create_exit('hallway', 'staircase', "A door with the words STAIRS is stuck open.")
create_exit(staircase, hallway, "Nevermind; go back to the hallway.")
create_exit(hallway, kitchen, "There is a door with the words KITCHEN above it.")
create_exit(kitchen, hallway, "Go back to the hallway.")
create_exit(kitchen, classroom, "Go back into the lecture hall.")
create_exit(staircase, outside, "A door at the bottom of the stairs has a red, glowing, EXIT sign.")

with open('adventure.json', 'w') as out:
    json.dump(GAME, out, indent=2)
