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
    cardCombos = []
    count = 0
    faceList = list(map(lambda x: x[0], hand))
    for i in range(len(faceList)):
        for j in range(i+1, len(faceList)):
            cardCombos.append((faceList[i], faceList[j]))
    for i in cardCombos:
        if i[0] == i[1]:
            count += 1
    if count == 1:
        return(True, i[0])
    else:
        return(False)
    
def two_pair(hand):
    cardCombos = []
    count = 0
    faceList = list(map(lambda x: x[0], hand))
    for i in range(len(faceList)):
        for j in range(i+1, len(faceList)):
            cardCombos.append((faceList[i], faceList[j]))
    for i in cardCombos:
        if i[0] == i[1]:
            count += 1
    if count == 2:
        return(True)
    else:
        return(False)

def three_of_a_kind(hand):
    faceList = sorted(map(lambda x: x[0], hand))
    if faceList[0] == faceList[1] == faceList[2] and faceList[3] != faceList[4]: # make sure you don't have a full house
        return(True, faceList[0])
    elif faceList[1] == faceList[2] == faceList[3]:
        return(True, faceList[1])
    elif faceList[2] == faceList[3] == faceList[4] and faceList[1] != faceList[2]:
        return(True, faceList[2])
    else:
        return(False)

def full_house(hand):
    faceList = sorted(list(map(lambda x: x[0], hand)))
    if faceList[0] == faceList[1] == faceList[2] and faceList[3] == faceList[4]:
        return(True)
    elif faceList[0] == faceList[1] and faceList[2] == faceList[3] == faceList[4]:
        return(True)
    else:
        return(False)

def four_of_a_kind(hand):
    faceList = sorted(list(map(lambda x: x[0], hand)))
    if faceList[0] == faceList[1] == faceList[2] == faceList[3]:
        return(True, faceList[0])
    elif faceList[1] == faceList[2] == faceList[3] == faceList[4]:
        return(True, faceList[1])
    else:
        return(False)

def flush(hand):
    suitList = list(map(lambda x: x[1], hand))
    if suitList[0] == suitList[1] == suitList[2] == suitList[3] == suitList[4]:
        return(True)
    else:
        return(False)
    
def straight(hand):
    faceList = sorted(list(map(lambda x: x[0], hand)))
    face = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
            'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'] #aces can act as high or low card here
    straightList = []
    for i in range(len(face)-5):
        straightList.append(sorted(face[i:i+5]))
    for i in straightList:
        if i == faceList:
            return(True)
    return(False)

def straight_flush(hand):
    if straight(hand) == True and flush(hand) == True:
        return(True)
    else:
        return(False)

def royal_flush(hand):
    faceList = sorted(list(map(lambda x: x[0], hand)))
    royalSuits = ['Ace', 'King', 'Queen', 'Jack', 'Ten']
    if (sorted(royalSuits) == sorted(faceList)) and flush(hand) == True:
        return(True)
    else:
        return(False)
        
def high_card(hand):
    print()

'''TODO: 
high card
do flush in ranking with other stuff
'''

#deck = initalize_deck()
#hand = deal(deck)
hand = [('Jack', 'Hearts'), ('Nine', 'Hearts'), ('Jack', 'Diamonds'), ('Ten', 'Hearts'), ('Queen', 'Hearts')]
print(hand)
onePair = one_pair(hand)
print("found one pair?:", onePair)
twoPair = two_pair(hand)
print("found two pairs?: ", twoPair)
threeOfAKind = three_of_a_kind(hand)
print('Found three of a kind?: ', threeOfAKind)
fourOfAKind = four_of_a_kind(hand)
print('Found four of a kind?:', fourOfAKind)
flushResult = flush(hand)
print('fount a flush?:', flushResult)
straightResult = straight(hand)
print('found a straight?', straightResult)
straightFlush = straight_flush(hand)
print('found a straight flush?:', straightFlush)
print('found a royal flush?:', royal_flush(hand))
print('found a full house?:', full_house(hand))


'''
for i in range(len(deck)):
    displayString = deck[i][0]+ " of " + deck[i][1]
    if i % 4 != 3:
        print(f'{displayString:<22}', end="")
    else:
        print(deck[i][0], "of", deck[i][1])
'''
