from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])

class FrenchDeck():
    ranks = [str(i) for i in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, key):
        return self._cards[key]
    
    def __repr__(self):
        return "for fun"
    
if __name__ == "__main__":
    bear_card = Card("7", "diamonds")
    print(bear_card)

    deck = FrenchDeck()
    print(deck)

    print(deck[:11])
    for d in deck: 
        print(d)