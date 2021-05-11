#HuntTheWumpus.py
#Written by Pymike
#Started: 5/10/2021
#Description: A Hunt the Wumpus Clone in Python

#Imports
import random

def game_setup():
    #Create a dictionary with all the game values
    game = {'gameover': False, 'arrows': 5, 'player_location': 0, 'wumpus_location': 0,
            'bat1_location': 0, 'bat2_location': 0, 'pit1_location': 0, 'pit2_location': 0,
            1: (2,5,8), 2: (1,3,10), 3: (2,4,12), 4: (3,5,15), 5: (1,4,6), 6: (5,7,15),
            7: (6,8,17), 8: (1,7,9), 9: (8,10,18), 10: (2,9,11), 11: (10,12,19),
            12: (3,11,13), 13: (12,14,20), 14: (4,13,15), 15: (6,14,16), 16: (15,17,20),
            17: (7,16,18), 18: (9,17,19), 19: (11,18,20), 20: (13,16,19)}

    #Randomize Starting Locations
    locations = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    random.shuffle(locations)

    #Assign key locations to their respective game variables
    game['player_location'] = locations[0]
    game['wumpus_location'] = locations[1]
    game['bat1_location'] = locations[2]
    game['bat2_location'] = locations[3]
    game['pit1_location'] = locations[4]
    game['pit2_location'] = locations[5]
    return game
    
def game_screen(game):
    #Prints the room details
    print('You are in room ' + str(game['player_location']) + '.')
    if game['wumpus_location'] in game[game['player_location']]:
        print('    I smell a Wumpus.')
    if game['bat1_location'] in game[game['player_location']]:
        print('    I hear flapping.')
    if game['bat2_location'] in game[game['player_location']]:
        print('    I hear flapping.')
    if game['pit1_location'] in game[game['player_location']]:
        print('    I feel a draft.')
    if game['pit2_location'] in game[game['player_location']]:
        print('    I feel a draft.')
    print('Tunnels lead to ' + str(game[game['player_location']][0]) +
          ', ' + str(game[game['player_location']][1]) +
          ', ' + str(game[game['player_location']][2]))
    
def shoot(game):
    #First Main Action
    #needs to kill the wumpus, scare the wumpus, chance to ricochet and fly through several rooms
    arrow_range = input ('How far? [1-5]')
    arrow_range = int(arrow_range)
    for a in range(arrow_range):
        room_check = input('Which room #: ')
        if int(room_check) == game['wumpus_location']:
            print('You have slain the wumpus. Congratulations!')
            gameover = True
            return
        
        else:
            print('You did not hit anything.')
            if wumpus_location in game[player_location]:
                print('You hear shuffling, and the scent of wumpus grows fainter.')
                new_wumpus_location = random.randint(1,19)
                if new_wumpus_location >= game['player_location']:
                    game['wumpus_location'] = new_wumpus_location + 1
                else:
                    game['wumpus_location'] = new_wumpus_location
                        
        arrows -= 1
        print('You have ' + str(arrows) + ' arrows remaining.')
        a += 1

def move(game):
    #Second Main Action
    #needs to move through the map, and check to see if bad things happen in the next room
    move = input('Where to? ')

    #Validate input to prevent players from moving to locations not currently available
    if int(move) not in game[game['player_location']]:
        print('You bump into the wall. That is not a valid exit!')
        return
    else:
        game['player_location'] = int(move)

    #Check for Hazards
    #Check bats first since they update the player location
    if (game['player_location'] == game['bat1_location']) or (game['player_location'] == game['bat2_location']):
        print('The bats swarm and carry you to a random location.')
        game['player_location'] = random.randint(1,20)
    if game['player_location'] == game['wumpus_location']:
        wumpus_reaction = random.randint(1,2)
        if wumpus_reaction == 1:
            print('You have angered the wumpus. It attacks. Game over')
            game['gameover'] = True
        else:
            print('You startled the wumpus. It ran away.')
            game['wumpus_location'] = random.randint(1,20)
    if (game['player_location'] == game['pit1_location']) or (game['player_location'] == game['pit2_location']):
        print('You fell into a bottomless pit. Game over.')
        game['gameover'] = True
    
def game():
    #Initialize Game
    game = game_setup()

    #Start Game Loop
    while game['gameover'] == False:
        #Print game screen
        game_screen(game)
        
        #Prompt Player for Action
        action = input('Shoot or Move (S-M)?')
        action = action.lower()
        if action == 's':
            #take the shooting action
            shoot(game)
        elif action == 'm':
            #take the moving action
            move(game)
        else:
            print('Incorrect Syntax')

        print('')
    
def main():
    #Calls the main game function
    game()

main()
