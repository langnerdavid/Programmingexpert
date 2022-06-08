import random

def sort_by_index(item):
    return item[len(item) - 1]


class Deck:
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["D", "H", "C", "S"]

    def __init__(self):
        self.deck = []
        for value in self.values:
            for suit in self.suits:
                self.deck.append(value+suit)

    def shuffle(self):
        return random.shuffle(self.deck)
    
    def deal(self, n):
        deal = self.deck[-n:]
        del self.deck[-n:]
        return deal

    def sort_by_suit(self):
        temp_deck = []
        for i in range(4):
            for item in self.deck:
                if i == 1 and "H" in item:
                    temp_deck.append(item)
                if i == 2 and "D" in item:
                    temp_deck.append(item)
                if i == 3 and "C" in item:
                    temp_deck.append(item)
                if i == 4 and "S" in item:
                    temp_deck.append(item)

        self.deck = temp_deck
        return self.deck

    def contains(self, card):
        if card in self.deck:
            return True

        return False

    def copy(self):
        copied_deck = Deck()
        copied_deck.deck = self.deck[:]
        return copied_deck


    def get_cards(self):
        new_deck = self.deck[:]
        return new_deck

    def __len__(self):
        return len(self.deck)
    

# d = Deck()   
# d.shuffle()
# print(d.deck)
# k = d.deal(5)
# print(k)
# print(d.deck)
# d.sort_by_suit()
# print(d.deck)
deck1 = Deck()
deck2 = deck1.copy()
print(deck1)
print(deck2)