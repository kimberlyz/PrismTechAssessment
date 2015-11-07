from random import randint

class Deck:

    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    cards = []

    def __init__(self):
        # Keeps track of the top card on the deck
        self.next = 0

        # Creates 52 cards and adds them to the cards array
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def Shuffle(self):
        # All cards are now accessible by resetting the top card value to 0
        self.next = 0

        # Uses Durstenfeld's version of the Fisher-Yates shuffle algorithm
        for i in range(len(self.cards) - 1, -1, -1):
            temp = self.cards[i]
            newPlace = randint(0, i)
            self.cards[i] = self.cards[newPlace]
            self.cards[newPlace] = temp

    def GetNextCard(self):
        # If the top card has reached the end of the deck, no more cards can be drawn
        if self.next >= len(self.cards):
            raise StopIteration('There are no more cards in the deck.')
        # Returns the value of the next card
        nextCard = self.cards[self.next]
        self.next += 1
        return nextCard

    #Used to see the order of cards in the deck
    def printout(self):
        for card in self.cards:
            print(card)

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.suit + ': ' + self.rank
