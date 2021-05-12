#HuntTheWumpus.py
#Written by Py-Mike
#Started: 5/10/2021
#Description: A Hunt the Wumpus Clone in Python

#Imports
import random

def main():
    keep_playing = True
    while keep_playing == True:
        #Calls the main game function
        keep_playing = game()

        #Checks to see if the player quit
        if keep_playing == False:
            break

        #Checks to see if wants to keep playing
        keep_playing = post_game()

def game():
    #Initialize Game
    game = game_setup()

    #Start Game Loop
    while game['gameover'] == False:
        #Print game screen
        game_screen(game)
        
        #Prompt Player for Action
        action = input('Shoot, Move, or Quit (S-M-Q)? ')
        action = action.lower()
        if action == 's':
            #take the shooting action
            shoot(game)
            if game['gameover'] == True:
                break
            else:
                game['gameover'] = arrow_count_check(game['arrows'])
        elif action == 'm':
            #take the moving action
            move(game)
            hazards(game)
        elif action == 'q':
            return False
        else:
            print('Incorrect Syntax')

        print('')

def post_game():
    a = True
    while a == True:
        play_again = input('Would you like to play again?(y/n) ')
        play_again.lower()
        if play_again == 'y':
            return True
        elif play_again == 'n':
            return False
        else:
            continue

def game_setup():
    #Create a dictionary with all the game values
    game = {'gameover': False, 'arrows': 5, 'arrow_location': 0, 'player_location': 0, 'wumpus_location': 0,
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
    arrow_range = 0
    
    arrow_range = input('How far? [1-5]')
    if arrow_range.isdigit():
        if int(arrow_range) not in range(1,6):
            print('Defaulting to max range.')
            arrow_range = 5
    else:
        print('Defaulting to max range.')
        arrow_range = 5
    #Set the arrow starting position to the players current position
    game['arrow_location'] = game['player_location']
    for a in range(int(arrow_range)):
        room_check = input('Which room #: ')
        if not room_check.isdigit():
            print('Not a valid input.')
            return
        if int(room_check) not in game[game['arrow_location']]:
            ricochet = random.randint(1, 20)
            if ricochet > 15:
                print('You fire your arrow into the wall and it ricochets')
                new_location = random.randint(1,4)
                if new_location == 4 and game['player_location'] == game['arrow_location']:
                    print('')
                    print('******* Game Over *******')
                    print('Upon firing randomly into the wall, your arrow flies back at you.')
                    print('Unable to dodge it wounds you greviously. The smell of blood fills the air.')
                    print('The Wumpus Has You.')
                    game['gameover'] = True
                    return
                elif new_location == 4 and game['player_location'] != game['arrow_location']:
                    new_location = random.randint(1,3)
                    game['arrow_location'] = game['player_location'][new_location]
            else:
                print('Your arrow flies into the wall and shatters.')
                game['arrows'] -= 1
                print('You have ' + str(game['arrows']) + ' arrows remaining.')
                return
        else:
            game['arrow_location'] = int(room_check)
            if game['arrow_location'] == game['wumpus_location']:
                print('')
                print('******* Game Over *******')
                print('Years of paitence has brought you to this moment.')
                print('Your arrow flies true. With a mighty roar the Wumpus')
                print('falls lifeless to the floor. But the Wumpus will get')
                print('you next time.')
                print('')
                game['gameover'] = True
                return

            elif game['arrow_location'] == game['player_location'] and a > 0:
                print('')
                print('******* Game Over *******')
                print('Through some unfortunate miracle of chance your arrow flies back')
                print('into the room you are standing in and greviously wounds you. The')
                print('smell of blood fills the air.')
                print('The Wumpus Has You.')
                game['gameover'] = True
                return
            
            elif game['arrow_location'] != game['wumpus_location'] and a != (int(arrow_range)-1):
                print('The crooked arrow continues to fly')
                game['arrow_location'] = int(room_check)

            else:
                print('You did not hit anything.')
                if game['wumpus_location'] in game[game['player_location']]:
                    print('You hear shuffling, and the scent of wumpus grows fainter.')
                    new_wumpus_location = random.randint(1,19)
                    if new_wumpus_location >= game['player_location']:
                        game['wumpus_location'] = new_wumpus_location + 1
                    else:
                        game['wumpus_location'] = new_wumpus_location

        a += 1
                        
    game['arrows'] -= 1
    print('You have ' + str(game['arrows']) + ' arrows remaining.')

def arrow_count_check(arrows):
    if arrows == 0:
        print('')
        print('******* Game Over *******')
        print('Upon firing your last arrow, the hunter becomes the hunted.')
        print('The Wumpus Has You.')
        return True
    else:
        return False

def move(game):
    #Second Main Action
    #needs to move through the map, and check to see if bad things happen in the next room
    move = input('Where to? ')
    if not move.isdigit():
        print('That is not a valid input')
        return

    #Validate input to prevent players from moving to locations not currently available
    if int(move) not in game[game['player_location']]:
        print('You bump into the wall. That is not a valid exit!')
        return
    else:
        game['player_location'] = int(move)

def hazards(game):
    #Check for Hazards
    #Check bats first since they update the player location
    if (game['player_location'] == game['bat1_location']) or (game['player_location'] == game['bat2_location']):
        print('The bats swarm and carry you to a random location.')
        game['player_location'] = random.randint(1,20)
        hazards(game)
        return
    if game['player_location'] == game['wumpus_location']:
        wumpus_reaction = random.randint(1,2)
        if wumpus_reaction == 1:
            print('')
            print('******* Game Over *******')
            print('As you enter the room you realize only too late that it was a trap.')
            print('The Wumpus Has You.')
            game['gameover'] = True
            return
        else:
            print('You startled the wumpus. It ran away.')
            game['wumpus_location'] = random.randint(1,20)
    if (game['player_location'] == game['pit1_location']) or (game['player_location'] == game['pit2_location']):
        print('')
        print('******* Game Over *******')
        print('You boldly enter the room, but where you expected floor there is none.')
        print('The Wumpus Has You.')
        game['gameover'] = True
        return

#Calls the main function to start the game.
main()
