import random

faceValues = ['ace', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'jack',
              'queen', 'king']

suits = ['clubs', 'diamonds', 'hearts',
         'spades']


def shuffledDeck():
    deck = []
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + ' of ' + suit)
    random.shuffle(deck)
    return deck

def faceValueOf(card):
    return card.split()[0]

def suitOf(card):
    return card.split()[2]

def gameRound(gameDeck):
    result = 0
    for x in range(6):
        if faceValueOf(gameDeck[x]) == "ace":
            result = 1
            return result
    return result

def totalRounds(bankroll):
    wallet = bankroll
    win = 2*wallet
    count = 0
    game = 1
    while game is 1:
        gameDeck = shuffledDeck()
        if gameRound(gameDeck) is 1:
            count += 1
            wallet += 1
        if gameRound(gameDeck) is 0:
            count += 1
            wallet -= 1
        if wallet is 0 or wallet is win:
            game = 0
    return count

