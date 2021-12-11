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

import random
import time
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
# Functions

def user_input():
    print('What do you do:\n\n'
        '1 - Stand your ground and fight\n'
        '2 - Run away to survive another day'
    )
    valid = False
    while not valid:
        user_inp = input('\nEnter 1 or 2:  ')
        if user_inp != '1' and user_inp != '2':
            print('Enter a valid response')
        else:
            valid = True
    return user_inp

def game_input():
    actions = [main, sys.exit, get_highscores]
    print('Would you like to:\n\n'
        '1 - Play again\n'
        '2 - Exit\n'
        '3 - View highscores'
    )
    valid = False
    while not valid:
        action = input('\nEnter 1, 2 or 3:  ')
        if action != '1' and action != '2' and action != '3':
            print('Enter a valid response')
        else:
            valid = True
    actions[int(action) - 1]()

def introduction():
    messages = ["Welcome to Monster Hunter (don't sue me Capcom)", 
                "Navigate the dark passages and make it out safely",
                "BUT WATCH OUT",
                "There are many ferocious monsters standing in your way",
                "Slay all the beasts and you win",
                "Lose 4 times and you die",
                "Good luck warrior!"
            ]

    for i in messages:
        print(i)
        time.sleep(2)    
    
def display_battle(monster):
    messages = ['draws closer', 'has appeared', ' has emerged', 'has materialised out of thin air']
    if monster.monster_rank == 20:
        print('WHY DO I HEAR BOSS MUSIC!?\n')
        print(f'ITS {monster.name.upper()} ({monster.monster_rank})!')
    else:
        message = random.choice(messages)
        print(f'{monster.name} ({monster.monster_rank}) {message}')

def create_player():
    username = input('Enter your username:  ')
    player = Player(username)
    return player

def get_monsters():
    with open('monsters.txt', 'r') as file:
        names = []
        for monster in file:
            monster = monster.rstrip('\n')
            names.append(monster)
    return names

def create_monsters():
    names = get_monsters()
    monsters = []
    for i in range(20):
        name = random.choice(names)
        names.remove(name)
        monster = Monster(name, i + 1)
        monsters.append(monster)
    return monsters

def final_score(score, wins, turns):
    total_score = score + wins + turns
    print(f'\nScore:        {score}\n'
        f'Wins:         {wins}\n'
        f'Turns:        {turns}\n\n'
        f'Final Score:  {total_score}'
    )
    return total_score

def save_score(username, total_score):
    with open('scores.txt', 'a') as file:
        file.write(f'{username}`{total_score}\n')
        
# --------------------------------------------------------------------------------------------------
# Main Code

def main():
    p1 = Player('bob', 0)
    p1.fight(10)

# --------------------------------------------------------------------------------------------------
# Driver Code

if __name__ == '__main__':
    main()
