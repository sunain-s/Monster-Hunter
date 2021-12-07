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
from random import randint

# --------------------------------------------------------------------------------------------------
# Classes

class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.defeats = 0
        self.wins = 0
        self.turns = self.wins + self.defeats

    def fight(self, monster_rank, monster_num):
        player_num =  randint(1, 100)
        if player_num > monster_num:
            self.wins += 1
            self.score += monster_rank
        elif player_num < monster_num:
            self.defeats += 1
        else:
            self.fight(monster_rank)


class Monster():
     
    def __init__(self, name, rank):
        self.name = name
        self.monster_rank = rank

    def monster_rnd_num(self):
        self.lower_bound = self.monster_rank * 4
        self.monster_num = randint(self.lower_bound, 100)
        
        
# --------------------------------------------------------------------------------------------------
# Functions

def input_validation(user_inp):
    if user_inp != '1' and user_inp != '2':
        print('\nEnter a valid response')
    else:
        pass


# --------------------------------------------------------------------------------------------------
# Main Code

def main():
    p1 = Player('bob', 0)
    p1.fight(10)

# --------------------------------------------------------------------------------------------------
# Driver Code

if __name__ == '__main__':
    main()
