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
        return(True)
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
    faceList = list(map(lambda x: x[0], hand))
    cardCombos = []
    count = 0
    for i in range(len(faceList) - 2):
        for j in range(i+1, len(faceList) - 1):
            for k in range(j+1, len(faceList)):
                cardCombos.append((faceList[i], faceList[j], faceList[k]))
    for i in cardCombos:
        if i[0] == i[1] == i[2]:
            count += 1
    if count == 1:
        return(True)
    else:
        return(False)

def four_of_a_kind(hand):
    faceList = list(map(lambda x: x[0], hand))
    cardCombos = []
    for i in range(len(faceList) - 3):
        for j in range(i+1, len(faceList) - 2):
            for k in range(j+1, len(faceList)-1):
                for m in range(k+1, len(faceList)):
                    cardCombos.append((faceList[i], faceList[j], faceList[k], faceList[m]))
    for i in cardCombos:
        if i[0] == i[1] == i[2] == i[3]:
            return(True)
    return(False)

def flush(hand):
    suitList = list(map(lambda x: x[1], hand))
    if suitList[0] == suitList[1] == suitList[2] == suitList[3] == suitList[4]:
        return(True)
    else:
        return(False)
    
def straight(hand):
    suitList = list(map(lambda x: x[1], hand))
    face = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
            'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'] #aces can act as high or low card here
    straightList = []
    for i in range(len(face)-5):
        straightList.append((face[i:i+5]))
    print(straightList)

'''TODO: 
royal flush
straght flush
straight
full house
high card
'''


#deck = initalize_deck()
#hand = deal(deck)
hand = [('Four', 'Hearts'), ('Four', 'Hearts'), ('Four', 'Hearts'), ('Seven', 'Hearts'), ('Four', 'Hearts')]
print(hand)
onePair = one_pair(hand)
print("found one pair?:", onePair)
twoPair = two_pair(hand)
print("found two pairs?: ", twoPair)
threeOfAKind = three_of_a_kind(hand)
print('Found three of a kind?: ', threeOfAKind)
fourOfAKind = four_of_a_kind(hand)
print('Found four of a kind?:', fourOfAKind)
print('fount a flush?:', flush(hand))

'''
for i in range(len(deck)):
    displayString = deck[i][0]+ " of " + deck[i][1]
    if i % 4 != 3:
        print(f'{displayString:<22}', end="")
    else:
        print(deck[i][0], "of", deck[i][1])
'''
