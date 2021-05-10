#HuntTheWumpus.py
#Written by Pymike
#Started: 5/10/2021
#Description: A Hunt the Wumpus Clone in Python

import random

#initialize variables
arrows = 5
gameover = False
action_count = 0
bat_locations = [0,0]
pit_locations = [0,0]
room = {1: [2,5,8],}
room[2] = [1,3,10]
room[3] = [2,4,12]
room[4] = [3,5,15]
room[5] = [1,4,6]
room[6] = [5,7,15]
room[7] = [6,8,17]
room[8] = [1,7,9]
room[9] = [8,10,18]
room[10] = [2,9,11]
room[11] = [10,12,19]
room[12] = [3,11,13]
room[13] = [12,14,20]
room[14] = [4,13,15]
room[15] = [6,14,16]
room[16] = [15,17,20]
room[17] = [7,16,18]
room[18] = [9,17,19]
room[19] = [11,18,20]
room[20] = [13,16,19]

#Randomize Starting Locations
locations = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(locations)
player_location  = locations[0]
wumpus_location = locations[1]
bat1_location = locations[2]
bat2_location = locations[3]
pit1_location = locations[4]
pit2_location = locations[5]

print('Developer Mode:')
print('Wumpus at ' + str(wumpus_location))
print('Bats at ' + str(bat1_location) + ' & ' + str(bat2_location))
print('Pits at ' + str(pit1_location) + ' & ' + str(pit2_location))
#Game Loop
while gameover == False:
    #Game Screen Output
    print('You have taken ' + str(action_count) + ' actions.')
    print('You are in room ' + str(player_location) + '.')
    if wumpus_location in room[player_location]:
        print('    I smell a Wumpus.')
    if bat1_location in room[player_location]:
        print('    I hear flapping.')
    if bat2_location in room[player_location]:
        print('    I hear flapping.')
    if pit1_location in room[player_location]:
        print('    I feel a draft.')
    if pit2_location in room[player_location]:
        print('    I feel a draft.')
    print('Tunnels lead to ' + str(room[player_location][0]) +
          ', ' + str(room[player_location][1]) +
          ', ' + str(room[player_location][2]))
    #Prompt Player for Action
    action = input('Shoot or Move (S-M)?')
    action = action.lower()
    if action == 's':
        arrow_range = input ('How far? [1-5]')
        arrow_range = int(arrow_range)
        for a in range(arrow_range):
            room_check = input('Which room #: ')
            if int(room_check) == wumpus_location:
                print('You have slain the wumpus. Congratulations!')
                gameover = True
                break
            a += 1
        print('You did not hit anything.')
        if wumpus_location in room[player_location]:
            print('You hear shuffling, and the scent of wumpus grows fainter.')
            new_wumpus_location = random.randint(1,19)
            if new_wumpus_location >= player_location:
                wumpus_location = new_wumpus_location + 1
            else:
                wumpus_location = new_wumpus_location
        arrows -= 1
        print('You have ' + str(arrows) + ' arrows remaining.')
    elif action == 'm':
        move = input('Where to? ')
        #if move not in room[player_location]:
        #    move = inp
        player_location = int(move)

        #Check for hazards
        #I check bats first since they update the player location
        if (player_location == bat1_location) or (player_location == bat2_location):
            print('The bats swarm and carry you to a random location.')
            player_location = random.randint(1,20)
        if player_location == wumpus_location:
            wumpus_reaction = random.randint(1,2)
            if wumpus_reaction == 1:
                print('You have angered the wumpus. It attacks. Game over')
                gameover = True
            else:
                print('You startled the wumpus. It ran away.')
                wumpus_location = random.randint(1,20)
        if (player_location == pit1_location) or (player_location == pit2_location):
            print('You fell into a bottomless pit. Game over.')
            gameover = True
    else:
        print('Incorrect Syntax')

    print('')
    action_count += 1
