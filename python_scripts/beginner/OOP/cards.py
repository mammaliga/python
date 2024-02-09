from random import shuffle


class Card:
    suit_allowed = ("Hearts", "Diamonds", "Clubs", "Spades")
    value_allowed = ("A", "2", "3", "4", "5", "6", "7",
                     "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, value):
        if f"{suit[0].upper()}{suit[1:]}" not in Card.suit_allowed or value.upper() not in Card.value_allowed:
            raise ValueError("There is no such suit or deck of cards")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value.upper()} of {self.suit[0].upper()}{self.suit[1:]}"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, value)
                      for suit in Card.suit_allowed
                      for value in Card.value_allowed]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif self.count() < num:
            self.cards.clear()
        else:
            return [self.cards.pop() for card in range(num)]

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        
        shuffle(self.cards)
        return self

    def deal_card(self):
        card = self._deal(1)
        return card[0]

    def deal_hand(self, num):
        cards = self._deal(num)
        return cards

# deck1 = Deck()
# print(deck1.cards)