import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(self.value, self.suit)
#
#     def make_deck():
#         suites = ["diamonds", "hearts", "clubs", "spades"]
#         values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#
#         game_deck = [Card(suite, value) for value in values for suite in suites]
#         return game_deck
#
#     def deal(game_deck):
#         random.shuffle(game_deck)
#         picked = game_deck.pop()
#         return picked
#
#
# game = Card.make_deck()
#
# print(Card.deal(game).show())

class Deck:
    def __init__(self):
        suits = ["diamonds", "hearts","clubs", "spades"]
        values = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

        self.game_deck = [Card(suit, value) for value in values for suit in suits]

    def show_deck(self):
        print(self.game_deck)

    def shuffle_deck(self):
        random.shuffle(self.game_deck)
        return self.game_deck

    def deal(self):
        random.shuffle(self.game_deck)
        picked = self.game_deck.pop()
        return picked

    def show(self):
        print(self.value, self.suit)

casino = Deck()





class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def add_to_hand(self, card):
        self.hand.append(card)
    def show(self):
        for card in self.hand:
            print(card.value, card.suit)

connor = Player("Connor")
dealer = Player("Dealer")
tens = ["K", "Q", "J"]


def playing_backjack():
    casino = Deck()
    turn = 1
    connor_score = 0
    for number in range(8):
        turn = turn * -1
        if turn > 0:
            print("Connor's Hand")

            new_card = casino.deal()
            print(new_card.show())
            if new_card.value in tens:
                connor_score += 10
            elif new_card.value == "A":
                connor_score += 11
            else:
                connor_score += new_card.value
            print(connor_score)


            print("\n \n \n")
        elif turn < 0:
            print("Dealer's Hand")
            dealer.add_to_hand(casino.deal())
            dealer.show()
            print("\n\n\n")

playing_backjack()
