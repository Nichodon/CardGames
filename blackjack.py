from deck import *

d = Deck()

def points() :
    total = 0
    aces = 0
    for i in d.getDealt() :
        val = i.getValue()
        if val > 10 :
            total = total + 10
        elif val > 1 :
            total = total + i.getValue()
        else :
            aces = aces + 1
    for i in xrange(aces) :
        if total + 10 + aces <= 21 :
            total = total + 11
            aces = aces - 1
        else :
            total = total + 1
            aces = aces - 1
    return total

print '\n---BLACKJACK---'
print d.dealCard()
print d.dealCard()
print 'Points: ' + str(points())

if points() < 21 :
    choice = ''
    while choice != 'N' :
        print '---------------'
        choice = raw_input('HIT YOU? Y/N ')
        if choice == 'Y' :
            print d.dealCard()
            print 'Points: ' + str(points())
        elif choice == 'N' :
            break
        else :
            print 'you lost'
            for i in xrange(19) :
                print d.dealCard()
            break
        if points() > 21 :
            break
        choice = ''
    print '---------------\nFinal: ' + str(points())
    if points() > 21 :
        print 'BUST! YOU LOSE! HAHAHA!'
    elif points() == 21 :
        print 'You almost lost there!'
    elif points() <= 11 :
        print 'WHY\'D you do that?!'
    else :
        final = points()
        d.dealCard()
        if points() <= 21 :
            print 'Could\'ve been better!'
        else :
            print 'Smart move! You win!'
else :
    print '---------------\nFinal: 21\nLUCKY! BLACKJACK! WOO!'