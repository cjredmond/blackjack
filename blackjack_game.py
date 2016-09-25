import random
import time


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
            #choice = input("Do you want 1 or 11 for the ace? \n >")
            #if choice == "11":
                #self.score += 11
            #else:
                self.score += 1
        else:
            self.score += card.value

    def show_score(self):
        return "This is {}'s score: {}".format(self.name, self.score)


    def check_bust(self):
        if self.score > 21:
            #print("METHOD BUST")
            return True
        else:
            return False

    def hit_or_stand(self):
        if self.score > 21:
            print("Sorry {} but your already bust".format(self.name))
        elif self.score == 21:
            print("{}, you already have 21".format(self.name))
            return False
        else:
            decision = input("{}, do you want to (H)it or (S)tand? \n >".format(self.name)).upper()
            if decision == "H":
                return True
            else:
                return False
    def empty_hand(self):
        self.hand = []


connor = Player("Connor")
dealer = Player("Dealer")

players = [connor, dealer]
def initialize_game(players):
    for player in players:
        player.empty_hand()
        player.score = 0
        first_card = casino.deal()
        player.add_to_hand(first_card)
        player.count_score(first_card)
        second_card = casino.deal()
        player.add_to_hand(second_card)
        player.count_score(second_card)
        print("\n")
    connor.show()
    print("\n")

def compare_scores(players):
    print("{}, your score is {}".format(connor.name, connor.score))
    print("The Dealer's score is {}".format(dealer.score))

    if dealer.score == 21:
        print("The dealer has 21, the Dealer wins")
    elif connor.score == 21 and dealer.score != 21:
        print("You've won with 21!")
    elif connor.score == dealer.score:
        print("Sorry, the dealer wins a tie")
    elif connor.score > 21 and dealer.score > 21:
        print("Both busted")
    else:
        if connor.score < 21 and dealer.score < 21:
            if connor.score > dealer.score:
                print("You beat the dealer")
            else:
                print("The dealer has a better score")



def playing_backjack(players):
    casino = Deck()
    initialize_game(players)
    print(connor.show_score())
    print("\n")
    while connor.check_bust() == False:
        choice = connor.hit_or_stand()
        if choice == True:
            new_card = casino.deal()
            new_card.show()
            connor.add_to_hand(new_card)
            connor.count_score(new_card)
            print(connor.show_score())
        else:
            print("You chose to stand")
            break
    while dealer.check_bust() == False:
        choice = True
        if connor.score <= dealer.score:
            choice = False
        elif connor.score > 21:
            choice = False
        if choice == True:
            print("The dealer chose to hit")
            new_card = casino.deal()
            new_card.show()
            dealer.add_to_hand(new_card)
            dealer.count_score(new_card)
        else:
            break
    dealer.show()
    compare_scores(players)
    play_again = input("Do you want to play again? Y/n:   ").lower()
    if play_again == "y":
        playing_backjack(players)

playing_backjack(players)
