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

def deal():
    global deck
    hand = deck[0:5]
    for i in range(5):
        deck.pop(0)
    return(hand)

def get_int(face):
    face_dictionary = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
            'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    return(face_dictionary.get(face))

def get_result_dict(rating):
    rank_dictionary = {10: 'Royal Flush', 9: 'Straight Flush', 8: 'Four of a Kind', 7: 'Full House', 6: 'Flush', 
                       5: 'Straight', 4: 'Three of a Kind', 3: 'Two Pairs', 2: 'One Pair', 1: 'High Card'}
    return(rank_dictionary.get(rating))

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
            pairFace = i[0]
    if count == 1:
        rankList = [True, get_int(pairFace), get_int(pairFace)] #building list of all 5 cards, one pair in index 0 and 1
        faceList.remove(pairFace)
        faceList.remove(pairFace)
        leftoverList = sorted([get_int(faceList[0]), get_int(faceList[1]), get_int(faceList[2])], reverse=True)
        rankList += leftoverList
        return(rankList)
    else:
        return([False])
    
def two_pair(hand):
    cardCombos = []
    count = 0
    pairList = []
    rankList = []
    faceList = list(map(lambda x: x[0], hand))
    for i in range(len(faceList)):
        for j in range(i+1, len(faceList)):
            cardCombos.append((faceList[i], faceList[j]))
    for i in cardCombos:
        if i[0] == i[1]:
            count += 1
            pairList += [i[0], i[1]]
    if count == 2:
        rankList = sorted([get_int(pairList[0]), get_int(pairList[1]), 
                                    get_int(pairList[2]), get_int(pairList[3])], reverse=True)
        for i in range(4):
            faceList.remove(pairList[i])
        rankList.insert(4, get_int(faceList[0]))
        rankList.insert(0, True)
        return(rankList)
    else:
        return([False])

def three_of_a_kind(hand):
    faceList = sorted(map(lambda x: x[0], hand))
    rankList = [True]
    if faceList[0] == faceList[1] == faceList[2] and faceList[3] != faceList[4]: # make sure you don't have a full house
        for i in faceList[0:3]:
            rankList.append(get_int(i))
        leftOverCards = sorted([get_int(faceList[3]), get_int(faceList[4])], reverse=True)
        rankList = rankList + leftOverCards
        return(rankList)
    elif faceList[1] == faceList[2] == faceList[3]:
        for i in faceList[1:4]:
            rankList.append(get_int(i))
        leftOverCards = sorted([get_int(faceList[0]), get_int(faceList[4])], reverse=True)
        rankList = rankList + leftOverCards
        return(rankList)
    elif faceList[2] == faceList[3] == faceList[4] and faceList[0] != faceList[1]:
        for i in faceList[2:5]:
            rankList.append(get_int(i))
        leftOverCards = sorted([get_int(faceList[0]), get_int(faceList[1])], reverse=True)
        rankList = rankList +leftOverCards
        return(rankList)
    else:
        return([False])

def full_house(hand):
    faceList = sorted(list(map(lambda x: x[0], hand)))
    
    if faceList[0] == faceList[1] == faceList[2] and faceList[3] == faceList[4]:
        rankList = [True]
        for i in faceList:
            rankList.append(get_int(i))
        return(rankList)
    elif faceList[0] == faceList[1] and faceList[2] == faceList[3] == faceList[4]:
        rankList =[True]
        for i in faceList[2:5]:
            rankList.append(get_int(i))
        for i in faceList[0:2]:
            rankList.append(get_int(i))
        return(rankList)
    else:
        return([False])

def four_of_a_kind(hand):
    faceList = sorted(list(map(lambda x: x[0], hand)))
    if faceList[0] == faceList[1] == faceList[2] == faceList[3]:
        rankList = [True]
        for i in faceList:
            rankList.append(get_int(i))
        return(rankList)
    elif faceList[1] == faceList[2] == faceList[3] == faceList[4]:
        rankList = [True]
        for i in faceList[1:5]:
            rankList.append(get_int(i))
        rankList.append(get_int(faceList[0]))
        return(rankList)
    else:
        return([False])

def flush(hand):
    suitList = list(map(lambda x: x[1], hand))
    faceList = list(map(lambda x: x[0], hand))
    if suitList[0] == suitList[1] == suitList[2] == suitList[3] == suitList[4]:
        rankList = []
        for i in faceList:
            rankList.append(get_int(i))
        rankList = sorted(rankList, reverse=True)
        rankList.insert(0, True)
        return(rankList)
    else:
        return([False])
    
def straight(hand):
    faceList = sorted(list(map(lambda x: x[0], hand)))
    face = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
            'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'] #aces can act as high or low card here
    straightList = []
    for i in range(len(face)-4):
        straightList.append(sorted(face[i:i+5]))
    for i in straightList:
        if i == faceList: #TODO: special case for Aces low
            rankList = []
            for j in faceList:
                rankList.append(get_int(j))
            rankList = sorted(rankList, reverse=True)
            rankList.insert(0, True)
            return(rankList)
    return([False])

def straight_flush(hand):   
    rankList = []
    if straight(hand)[0] == True and flush(hand)[0] == True:
        for i in hand:
            rankList.append(get_int(i[0]))
            rankList = sorted(rankList, reverse=True)
        rankList.insert(0, True)
        return(rankList)
    else:
        return([False])

def royal_flush(hand):
    faceList = sorted(list(map(lambda x: x[0], hand)))
    royalSuits = ['Ace', 'King', 'Queen', 'Jack', 'Ten']
    if (sorted(royalSuits) == sorted(faceList)) and flush(hand)[0] == True:
        rankList = [True, 14, 13, 12, 11, 10]
        return(rankList)
    else:
        return([False])
        
def high_card(hand):
    print()

def rated_hand(hand):
    if royal_flush(hand)[0] == True:
        ratedHand = royal_flush(hand)
        ratedHand[0] = 10
        return(ratedHand)
    elif straight_flush(hand)[0] == True:
        ratedHand = straight_flush(hand)
        ratedHand[0] = 9
        return(ratedHand)
    elif four_of_a_kind(hand)[0] == True:
        ratedHand = four_of_a_kind(hand)
        ratedHand[0] = 8
        return(ratedHand)
    elif full_house(hand)[0] == True:
        ratedHand = full_house(hand)
        ratedHand[0] = 7
        return(ratedHand)
    elif flush(hand)[0] == True:
        ratedHand = flush(hand)
        ratedHand[0] = 6
        return(ratedHand)
    elif straight(hand)[0] == True:
        ratedHand = straight(hand)
        ratedHand[0] = 5
        return(ratedHand)
    elif three_of_a_kind(hand)[0] == True:
        ratedHand = three_of_a_kind(hand)
        ratedHand[0] = 4
        return(ratedHand)
    elif two_pair(hand)[0] == True:
        ratedHand = two_pair(hand)
        ratedHand[0] = 3
        return(ratedHand)
    elif one_pair(hand)[0] == True:
        ratedHand = one_pair(hand)
        ratedHand[0] = 2
        return(ratedHand)
    else: #finding high card   #TODO: this part is broken
        faceList = sorted(list(map(lambda x: x[0], hand)))
        ratedHand = []
        for i in faceList:
            ratedHand.append(get_int(i))
        ratedHand = sorted(ratedHand, reverse=True)
        ratedHand.insert(0, 1)
        return(ratedHand)

def show_results(ratedHand1, ratedHand2, hand1, hand2):
    
    if ratedHand1 > ratedHand2:
        print("hand 1 wins! They have a", get_result_dict(ratedHand1[0]), "\n")
        print("Hand 1 results", hand1, "\n")
        print("Hand 2 results", hand2)
    elif ratedHand1 < ratedHand2:
        print("hand 2 wins! They have a", get_result_dict(ratedHand2[0]), "\n")
        print("Hand 1 results", hand1, "\n")
        print("Hand 2 results", hand2)
    else:
        print("It's a tie! with a ", get_result_dict(ratedHand1[0]), "\n")
        print("Hand 1 results", hand1, "\n")
        print("Hand 2 results", hand2)
    print()

deck = initalize_deck()
hand1 = [('Four', 'Puppy Paws'), ('King', 'Hearts'), ('Queen', 'Puppy Paws'), ('Jack', 'Spades'), ('Ace', 'Hearts')] 
hand2 = [('Eight', 'Puppy Paws'), ('Nine', 'Diamonds'), ('Ace', 'Spades'), ('Four', 'Spades'), ('Queen', 'Diamonds')]

hand1 = deal()
hand2 = deal()
ratedHand1 = rated_hand(hand1)
ratedHand2 = rated_hand(hand2)
show_results(ratedHand1, ratedHand2, hand1, hand2)