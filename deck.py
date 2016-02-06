from random import *

sval = ['Diamond', 'Gold', 'Silver', 'Copper']
vval = ['Clown', 'Uno', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Speaker', 'Vice', 'President']
jval = ['Black', 'Red']

class Card :

    suit = 0
    value = 1

    def __init__(self, s, v) :
        self.suit = s
        self.value = v

    def getSuit(self) :
        return self.suit

    def getValue(self) :
        return self.value

    def __str__(self):
        if self.value > 0 :
            return vval[self.value] + ' of ' + sval[self.suit]
        else :
            return jval[self.suit % 2] + ' ' + vval[self.value]

class Deck :
    cards = []
    dealt = []

    def __init__(self) :
        for i in xrange(1, 14, 1) :
            for j in xrange(4) :
                self.cards.append(Card(j, i))

    def dealCard(self) :
        ranc = self.cards[randint(0, len(self.cards) - 1)]
        self.cards.remove(ranc)
        self.dealt.append(ranc)
        return str(ranc)

    def remaining(self) :
        return len(self.card)

    def getDealt(self) :
        return self.dealt