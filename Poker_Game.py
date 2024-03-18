import random

def initalize_deck():
    face = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
            'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suit = ['Hearts', 'Diamonds', 'Spades', 'Puppy Paws']
    deck = []

    for f in face:
        for s in suit:
            deck.append((f, s))
    random.shuffle(deck)
    return(deck)

def deal(deck):
    return(deck[0:5])

def one_pair(hand):
    faceList = list(map(lambda x: x[0], hand))
    for i in range(len(faceList)):
        if faceList[i] in faceList[i + 1:]:
            print(faceList[i], "found")
            return(True)
    return(False)
        
def two_pair(hand):
    faceList = list(map(lambda x: x[0], hand))
    count = 0
    for i in range(len(faceList)):
        if faceList[i] in faceList[i + 1:]:
            print(faceList[i], "found")
            count += 1
    if count == 2:
        return(True)
    else:
        return(False)
    

#deck = initalize_deck()
#hand = deal(deck)
hand = [('Two', 'Hearts')]
print(hand)
onePair = one_pair(hand)
print("found one pair?:", onePair)
two_pair(hand)

'''
for i in range(len(deck)):
    displayString = deck[i][0]+ " of " + deck[i][1]
    if i % 4 != 3:
        print(f'{displayString:<22}', end="")
    else:
        print(deck[i][0], "of", deck[i][1])
'''
