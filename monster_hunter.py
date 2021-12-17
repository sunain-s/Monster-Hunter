# OOP Monster Hunter Game

'''
Brief:

    - Monsters and the player must be objects with attributes
    - Program records player name, score, wins and defeats
    - Points scored by defeating a monster
    - Defeated monster's rank is added to player score
    - Win/defeat determined by random numbers
    - Player can withstand 3 defeats, any more results in game over
    - Running away forfeits points equivalent to monster's rank
    - At game over, player score, win total and number of turns displayed
        ==> player final score = score + win total + number of turns

Extensions:

    - Monster names read in from a file
    - Write player name and final score to a file
    - Create high score table using said file
    - 20 monsters total, once defeated can not reappear
'''

# --------------------------------------------------------------------------------------------------
# Imports

import sys
import time
import random
from random import randint

# --------------------------------------------------------------------------------------------------
# Classes

class Player():

    '''
    - Creates player object with a name, score, defeats, wins and turns
    - Handles monster vs player battle including forfeits
    '''

    # creates player object
    def __init__(self, name): 
        self.name = name
        self.score = 0
        self.defeats = 0
        self.wins = 0
        self.turns = 0
        self.i = 0 # monster list iterator

    def fight(self, monster_name, monster_rank, monster_num):
        player_num =  randint(1, 100)
        # if player wins, add a win, add monster rank to score
        if player_num > monster_num: 
            self.wins += 1
            self.score += monster_rank
            print(f'{monster_name} dealt {monster_num} damage to you, but you hit back with {player_num} damage and won!')
            self.i += 1  

        # if player loses, add a loss
        elif player_num < monster_num:
            self.defeats += 1
            print(f'You dealt {player_num} damage to {monster_name} , but they dealt {monster_num} damage to you and beat you :(')
    
        # if draw, repeat
        else:
            self.fight(monster_name, monster_rank, monster_num)
        
        # output updated stats, add a turn
        print(f'Score:        {self.score}\n'
            f'Wins:         {self.wins}\n'
            f'Losses:       {self.defeats}\n'
            )
        self.turns += 1

    def forfeit(self, monster_rank):
        # subtract monster rank, output updated stats, add a turn
        self.score -= monster_rank
        print(f'Score:        {self.score}\n'
            f'Wins:         {self.wins}\n'
            f'Losses:       {self.defeats}\n'
        )
        self.turns += 1

class Monster():

    '''
    - Creates monster with a name and rank
    - Weights monster number according to rank
    '''
     
    # creates monster object
    def __init__(self, name, rank):
        self.name = name
        self.monster_rank = rank

    # weights random number according to monster rank
    def monster_rnd_num(self):
        self.lower_bound = self.monster_rank * 3
        self.monster_num = randint(self.lower_bound, 100)
        return self.monster_num
      
# --------------------------------------------------------------------------------------------------
# Input Functions

def user_input():
    '''
    Input validation and message display for user input during game
    '''

    print('What do you do:\n\n'
        '1 - Stand your ground and fight\n'
        '2 - Run away to survive another day'
    )
    valid = False
    while not valid: # repeats until valid input given
        user_inp = input('\nEnter 1 or 2:  ')
        if user_inp != '1' and user_inp != '2': 
            print('Enter a valid response')
        else:
            valid = True
    return user_inp
    
def game_input():
    '''
    Program options with input validation
    '''

    actions = [main, sys.exit, get_highscores] # function list to be called
    print('Would you like to:\n\n'
        '1 - Play again\n'
        '2 - Exit\n'
        '3 - View highscores'
    )
    valid = False
    while not valid: # repeats until valid input given
        action = input('\nEnter 1, 2 or 3:  ')
        if action != '1' and action != '2' and action != '3':
            print('Enter a valid response')
        else:
            valid = True
    actions[int(action) - 1]() # calls selected function

# --------------------------------------------------------------------------------------------------
# Message Functions

def introduction():
    '''
    Introductory messages at start of game
    '''

    messages = ["Welcome to Monster Hunter (don't sue me Capcom)", 
                "Navigate the dark passages and make it out safely",
                "BUT WATCH OUT",
                "There are many ferocious monsters standing in your way",
                "Slay all the beasts and you win",
                "Lose 4 times and you die",
                "Good luck warrior!"
            ]

    # prints each message with a 2 second gap between them
    for i in messages:
        print(i)
        time.sleep(2)

def display_battle(monster):
    '''
    Displays messages to update user on monster being faced
    '''

    messages = ['draws closer', 'has appeared', ' has emerged', 'has materialised out of thin air'] # possible messages
    if monster.monster_rank == 20: # special messages for boss monster
        print('WHY DO I HEAR BOSS MUSIC!?\n')
        print(f'ITS {monster.name.upper()} ({monster.monster_rank})!')
    else:
        message = random.choice(messages)
        print(f'{monster.name} ({monster.monster_rank}) {message}') # outputs monster name, rank and random message)

# --------------------------------------------------------------------------------------------------
# Object Creations Functions    

def create_player():
    '''
    Gets username and creates player object
    '''

    username = input('Enter your username:  ')
    player = Player(username) # creates player object
    return player

def get_monsters():
    '''
    Reads monster names from 'monsters.txt' and makes them usable in the program
    '''

    with open('monsters.txt', 'r') as file:
        names = []
        for monster in file:
            monster = monster.rstrip('\n')
            names.append(monster) # adds monsters names in file to list
    return names

def create_monsters():
    '''
    Creates instances of monster object
    '''

    names = get_monsters() # gets monster names
    monsters = []
    for i in range(20):
        name = random.choice(names) # randomly chooses a monster name
        names.remove(name)
        monster = Monster(name, i + 1) # creates a monster with that name, and a rank
        monsters.append(monster) # stores monster in list
    return monsters

# --------------------------------------------------------------------------------------------------
# Score Functions    

def final_score(score, wins, turns):
    '''
    Outputs players end stats and scores
    '''

    total_score = score + wins + turns
    print(f'\nScore:        {score}\n'
        f'Wins:         {wins}\n'
        f'Turns:        {turns}\n\n'
        f'Final Score:  {total_score}'
    )
    return total_score

def save_score(username, total_score):
    '''
    Saves player username and total_score to 'scores.txt' file
    '''

    with open('scores.txt', 'a') as file:
        file.write(f'{username}`{total_score}\n')

def get_highscores():
    '''
    Reads in scores from 'scores.txt' and makes a top 10 list
    '''

    users = []
    scores = []
    top_users = []
    with open('scores.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n').split('`') # splits into user and score, and removes newline ending
            users.append(line[0])
            scores.append(int(line[1]))
            top_scores = sorted(scores, reverse = True) # sorted scores in descending order

        if len(scores) < 10: 
            for x in range(len(scores)): # iterates until all scores added
                user = users[scores.index(top_scores[x])] # finds corresponding user for top score
                top_users.append(user)
                del users[scores.index(top_scores[x])] # removes user and score from list to prevent doubling up
                scores.remove(top_scores[x])
        else:
            for x in range(10): # iterates to create top 10
                user = users[scores.index(top_scores[x])] # finds corresponding user for top score
                top_users.append(user)
                del users[scores.index(top_scores[x])] # removes user and score from list to prevent doubling up
                scores.remove(top_scores[x])
                
    display_highscores(top_users, top_scores)

def display_highscores(users, scores):
    '''
    Outputs highscores in user friendly format
    '''

    for user in users:
        print(f'{users.index(user) + 1}: {user} -   {scores[users.index(user)]}')
        
# --------------------------------------------------------------------------------------------------
# Main Function

def main():
    '''
    Main function that formulates the program and calls all required functions
    Ran upon file running
    '''

    # Set up and user introduction
    introduction()
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    time.sleep(2)
    monsters = create_monsters()
    player = create_player()

    # Main loop
    while player.defeats < 4 and player.wins < 20 and player.i < 20 :
        
        # Battle and user decision
        monster = monsters[player.i]
        display_battle(monster)
        choice = user_input()
        
        # Fight or Forfeit
        if choice == '1':
            player.fight(monster.name, monster.monster_rank, monster.monster_rnd_num())
        if choice == '2':
            player.forfeit(monster.monster_rank)
    
    # Saving score
    total_score = final_score(player.score, player.wins, player.turns)
    save_score(player.name, total_score)

    # End output message - result dependent
    if player.defeats == 4:
        print('You lost to 4 monsters and died\n💀 R.I.P 💀')
    elif player.wins == 20:
        print('You survived all the monsters and escaped!')
        time.sleep(2)
        print(f'Some might call you, {player.name}, the real monster...')

    # Further options
    game_input()

# --------------------------------------------------------------------------------------------------
# Driver Code

if __name__ == '__main__':
    main()
