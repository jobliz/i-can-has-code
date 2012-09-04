# This code is from http://slnc.me/jugando-con-simulaciones-de-monte-carlo/ (in spanish). From the post for convenience (translated):

"""
Each time you buy a cereal box it comes with a random cart. There are 6 unique cards in total. How many boxes would you have to buy if you want to have them all? This code simulates the purchases until having all the cards, and it repeats the simulation many times to get the average.
"""

import random

num_cards = 6
games_to_play = 100000

class Game(object):
    def __init__(self):
        self.tosses = 0
        self.cards = []

    def pickCard(self):
        self.tosses += 1
        newcard = random.randint(1, num_cards)
        if not newcard in self.cards:
            self.cards.append(newcard)

    def run(self):
        while len(self.cards) < num_cards:
            self.pickCard()
        return self.tosses

if __name__ == '__main__':
    tosses = []
    for i in range(games_to_play):
        g = Game()
        tosses.append(g.run())

    print 'Boxes to buy: %.2f' % (float(sum(tosses)) / len(tosses))
