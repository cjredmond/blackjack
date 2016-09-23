import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(self.value, self.suit)

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
        self.score = 0
    def add_to_hand(self, card):
        self.hand.append(card)
    def show(self):
        for card in self.hand:
            print(card.value, card.suit)
    def count_score(self, card):
        tens = ["K", "Q", "J"]
        if card.value in tens:
            self.score += 10
        elif card.value == "A":
            choice = input("Do you want 1 or 11 for the ace? \n >")
            if choice == 11:
                self.score += 11
            else:
                self.score += 1
        else:
            self.score += card.value
        return self.score
    def check_bust(self):
        if self.score > 21:
            print("METHOD BUST")
            return True

connor = Player("Connor")
dealer = Player("Dealer")
tens = ["K", "Q", "J"]








def playing_backjack():
    casino = Deck()
    turn = 1
    for number in range(10):
        turn = turn * -1
        if connor.check_bust() == True:
            print("DONE")
            break
        if turn > 0:
            print("Connor's Hand")
            new_card = casino.deal()
            print(new_card.show())
            print(connor.count_score(new_card))

            print("\n \n \n")
        elif turn < 0:
            print("Dealer's Hand")
            dealer.add_to_hand(casino.deal())
            dealer.show()
            print("\n\n\n")

playing_backjack()
