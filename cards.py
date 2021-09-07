# class Card
# holds a card (short word)
# has a method to detect if matches other card
# has a property to determine if has been matched
# has a location property
# has a property to print out card

class Card:
    def __init__(self, word, location):
        self.card = word
        self.location = location
        self.matched = False

    def __eq__(self, other):
        return self.card == other.card

    def __str__(self):
        return self.card


if __name__ == '__main__':
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('hut', 'D4')
