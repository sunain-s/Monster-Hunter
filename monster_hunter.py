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
    
    lives = 3
    wins = 0
    defeats = 0
    turns = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def fight(self, monster_rank):
        monster_num, player_num = randint(1, 100), randint(1, 100)
        if player_num > monster_num:
            self.wins += 1
            self.score += monster_rank
        elif player_num < monster_num:
            self.defeats += 1
        else:
            self.fight(monster_rank)



class Monster():
    pass
# --------------------------------------------------------------------------------------------------
# Repeated Functions


# --------------------------------------------------------------------------------------------------
# Main Code

def main():
    pass

# --------------------------------------------------------------------------------------------------
# Driver Code

if __name__ == '__main__':
    main()
