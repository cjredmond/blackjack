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
        self.money = 100
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
            return True
        else:
            return False

    def hit_or_stand(self):
        if self.score == 21:
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
    def buy_in(self):
        self.money -= 10
        print("{} now has ${}".format(self.name, self.money))
    def win_money(self):
        self.money += 20
    def beat_dealer(self):
        if self.score < 22 and dealer.score > 21:
            return True
        elif self.score < 22 and dealer.score < 22:
            if self.score > dealer.score:
                return True
            else:
                return False
        else:
            return False

class Dealer(Player):
    def hit_or_stand(self):
        if self.score > 16:
            return False
        else:
            return True
    def buy_in(self):
        pass
    def win_money(self):
        pass
    def beat_dealer(self):
        pass
    




connor = Player("Connor")
dealer = Dealer("Dealer")
bill = Player("Bill")
steve = Player("Steve")
nick = Player("Nick")
jack = Player("Jack")

players = [connor, bill, steve, nick, jack, dealer]
def initialize_game(players):
    casino = Deck()
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
        player.show()
        player.buy_in()
    print("\n")

def playing_backjack(players):
    for player in players:
        if player.money == 0:
            players.remove(player)
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

    for player in players:
        if player == connor:
            pass
        else:
            print("It is now {}'s turn".format(player.name))
            while player.check_bust() == False:
                choice = True
                if player.score > 16:
                    choice = False
                if choice == True:
                    new_card = casino.deal()
                    new_card.show()
                    player.add_to_hand(new_card)
                    player.count_score(new_card)
                else:
                    print("{} has chose to stand".format(player.name))
                    break
            if player.check_bust() == True:
                print("{} has busted".format(player.name))
    for player in players:
        player.show()
        print(player.show_score())
    for player in players:
        if player == dealer:
            pass
        else:
            if player.beat_dealer() == True:
                player.win_money()

    play_again = input("Do you want to play again? Y/n:   ").lower()
    if play_again == "y":
        casino.show_deck()
        playing_backjack(players)

playing_backjack(players)
