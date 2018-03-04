import random

class Card:
    #suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    #value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value,suit) for suit in suits for value in values]

        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))
        # print(self.cards)
    
    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def count(self):
        return len(self.cards)
    
    def _deal(self, cards_to_deal):
        count = self.count()
        actual_to_remove = min([count, cards_to_deal])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards_dealt = self.cards[-actual_to_remove:]
        self.cards = self.cards[:-actual_to_remove]
        return cards_dealt
            
    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.cards)
        return self.cards
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, num_to_deal):
        return self._deal(num_to_deal)

card1 = Card("A", "Spades")
print(card1)
deck1 = Deck()
print(deck1.count())
# print(deck1)
# deck1._deal(10)
# print(deck1._deal(4))
# print(deck1)
deck1.shuffle()
print(deck1.deal_card())
print(deck1.deal_hand(5))
print(deck1)
