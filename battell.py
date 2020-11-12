import json

GAME = {
    '__metadata__': {
        'title': 'Battell',
        'start': 'entrance',
    }
}

def create_room(name, description, ends_game=False):
    """
    Create a dictionary that represents a room in our game.

    INPUTS:
     name: string used to identify the room; think of this as a variable name.
     description: string used to describe the room to the user.
     ends_game: boolean, True if arriving in this room ends the game.
    
    RETURNS:
     the dictionary describing the room; also adds it to GAME!
    """
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

entrance = create_room("entrance", "You're in Battell entrance. You want to have a good time. Where would you like to go?")
entrance["items"].append('Broom')
basement = create_room("basement", "Yikes, you just inhaled so much mold. This was a mistake.", ends_game=True)
south = create_room("b2s", "You're in B2S... This seems pretty lame. Let's go somewhere else.")
south["items"].append('Garbage')
center = create_room("b2c","You're in B2C... This seems pretty lame. Let's go somewhere else.")
center["items"].append('Exit Sign')
north = create_room("b2n", "Wow, you're in B2N. his place is full of amazing people. Congrats, you've found the party!")
north["items"].append('Cool Kids')
college_street = create_room("College Street", "You're outside! It's -50 degrees celcius. You instantly die from cold shock.", ends_game=True)
kitchen = create_room("kitchen", "Yikes, there's a mouse here. Battell must be full of mice.")
kitchen["items"].append('Burnt Popcorn')
stairs = create_room("staircase", "What a colorful staircase...")
stairs["items"].append('Clock')

create_exit(entrance, stairs, "You go up the staircase to the second floor.")
create_exit(stairs, entrance, "You go back down the stairs.")
create_exit(stairs, north, "You hear some music and laughs. Sounds like a good time.")
create_exit(north, stairs, "You don't want to have a good time. You go back down the stairs")
create_exit(stairs, south, "It's dead silent over there. Spooky stuff.")
create_exit(south, stairs, "You go back to the stairs.")
create_exit(stairs, center, "You see a PubSafe officer walking around.")
create_exit(center, stairs, "You go back to the stairs.")
create_exit(entrance, kitchen, "It smells like burnt popcorn over there. Follow the smell?")
create_exit(kitchen, entrance, "Go back to entrance.")

create_exit(south, center, "You see a strange light over in center.")
create_exit(center, south, "Center is boring. You go back to south.")
create_exit(center, north, "Center is boring. You feel good vibes coming from north. You check it out.")
create_exit(north, center, "North is too fun. You wan't to leave for some reason.")

create_exit(stairs, basement, "You smell something weird and follow the smell.")
create_exit(stairs, college_street, "It's hot in here. You want to leave.")

with open('battell.json', 'w') as out:
    json.dump(GAME, out, indent=2)