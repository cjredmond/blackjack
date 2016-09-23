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
        print("This is {}'s hand: ".format(self.name))
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

    def show_score(self):
        return "This is {}'s score: {}".format(self.name, self.score)


    def check_bust(self):
        if self.score > 21:
            print("METHOD BUST")
            return True
        else:
            return False

    def hit_or_stand(self):
        if self.score > 21:
            print("Sorry {} but your already bust".format(self.name))
        elif self.score == 21:
            print("{}, you already have 21".format(self.name))
        else:
            decision = input("{}, do you want to (H)it or (S)tand? \n >".format(self.name)).upper()
            if decision == "H":
                return True
            else:
                return False


connor = Player("Connor")
dealer = Player("Dealer")

players = [connor, dealer]
def initialize_game(players):
    for player in players:
        first_card = casino.deal()
        player.add_to_hand(first_card)
        player.count_score(first_card)
        second_card = casino.deal()
        player.add_to_hand(second_card)
        player.count_score(second_card)
        print(player.show())
        print("\n")
    print("\n\n")






def playing_backjack(players):
    initialize_game(players)
    for player in players:
        print(player.show_score())
    print("\n")

    while players[0].check_bust() == False or players[1].check_bust() == False:
                if players[0].check_bust() == False:
                    print(players[0].show_score())

                    choice = players[0].hit_or_stand()
                    if choice == True:
                        new_card = casino.deal()
                        new_card.show()
                        players[0].add_to_hand(new_card)
                        players[0].count_score(new_card)
                        print(players[0].show_score())
                    


                else:
                    pass





                print(players[1].show_score())
                if players[1].check_bust() == False:
                    choice = players[1].hit_or_stand()
                    if choice == True:
                        new_card = casino.deal()
                        new_card.show()
                        players[1].add_to_hand(new_card)
                        players[1].count_score(new_card)
                        print(players[1].show_score())
                else:
                    pass


















playing_backjack(players)
