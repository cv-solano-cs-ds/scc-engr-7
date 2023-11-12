from random import shuffle


class Card:
    """
    Represents a card object
    """

    SUITS = {"spades", "clubs", "hearts", "diamonds"}
    VALS = {
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "queen",
        "king",
        "jack",
        "ace",
    }

    def __init__(self, val: str | int, suit: str):
        """
        Creates a card with the given suit and value.
        """
        self.suit = suit
        self.val = str(val)

    def __str__(self):
        """
        Returns the string representation of a card.
        """
        return self.val + "of" + self.suit


class Deck:
    """
    A deck containing 52 cards.
    """

    def __init__(self):
        """
        Creates a full deck of cards.
        """
        self.hand: list[Card] = []

        for suit in Card.SUITS:
            for val in Card.VALS:
                self.hand.append(Card(val, suit))

    def shuffle(self):
        """
        Shuffles the cards.
        """
        shuffle(self.hand)

    def deal(self):
        """
        Removes and returns the top card or None if the deck is empty.
        """
        if len(self.hand) > 0:
            self.shuffle()
            return self.hand.pop(0)

    def __len__(self):
        """
        Returns the number of cards left in the deck.
        """
        return len(self.hand)

    def __str__(self):
        """
        Returns the string representation of a deck.
        """
        result = ""
        for card in self.hand:
            result += str(card) + "\n"
        return result


class Player:
    """
    This class represents a player in a game of 21.
    """

    def __init__(self, hand: list[Card] | None = None):
        self.hand = hand
        self.calc_score()

    def __str__(self):
        """
        Returns string rep of hand and points.
        """
        rtn = "\tCards: "
        rtn += ", ".join(map(str, self.hand))
        rtn += "\n\tBest score: " + str(self.score)
        return rtn

    def draw_card(self, deck: Deck):
        """
        Draw a card from the deck.
        """
        self.hand.append(deck.deal())
        self.calc_score()

    def calc_score(self):
        """
        Returns the best score given the cards in the Player's hand.
        """

        # This function is almost identical to self.score() in Lab 4
        score_without_aces = 0
        number_of_aces = 0

        # iterate through each card in the set
        for card in self.hand:
            v = card.val

            # check if its an ace
            if v == "ace":
                number_of_aces = number_of_aces + 1
            else:
                # if not, get its value
                if v in {"king", "queen", "jack"}:
                    score_without_aces = score_without_aces + 10
                else:
                    score_without_aces = score_without_aces + int(v)

        # now deal with the aces (if any) and find the best score
        if number_of_aces == 0:
            self.score = score_without_aces

        # 1 ace, either add 10 or 1
        elif number_of_aces == 1:
            if score_without_aces + 10 <= 21:
                self.score = score_without_aces + 10
            else:
                self.score = score_without_aces + 1

        # 2 aces, we either add 20, 11, or 2
        elif number_of_aces == 2:
            if score_without_aces + 20 <= 21:
                self.score = score_without_aces + 20
            elif score_without_aces + 11 <= 21:
                self.score = score_without_aces + 11
            else:
                self.score = score_without_aces + 2

        # 3 aces, either add 21, 12, or 3
        elif number_of_aces == 3:
            if score_without_aces + 21 <= 21:
                self.score = score_without_aces + 21
            elif score_without_aces + 12 <= 21:
                self.score = score_without_aces + 12
            else:
                self.score = score_without_aces + 3

        # 4 aces we can only have 13 or 4
        else:
            if score_without_aces + 13 <= 21:
                self.score = score_without_aces + 10 + 3
            else:
                self.score = score_without_aces + 4


class Dealer(Player):
    """
    Like a Player, but with some restrictions.
    """

    def __init__(self, cards: list[Card]):
        """
        Initial state: show one card only.
        """
        Player.__init__(self, cards)
        self.visible_card = self.hand[0]

    def __str__(self):
        """
        Return the string of the visible card.
        """
        rtn = "\tCards: "
        rtn += ", ".join(map(str, self.hand))
        rtn += "\n\tBest score: " + str(self.score)
        print(rtn)

        return "\tVisible card: " + str(self.visible_card)

    def draw_card(self, deck):
        """
        Draw a card from the deck, only if self.score < 17.
        """
        if self.score < 17:
            self.hand.append(deck.deal())


class TwentyOne:
    """
    A game of twenty one. Consists of a Deck, a Player and a Dealer.
    """

    def __init__(self):
        """
        Initialize the game.

        Create the Deck, create the dealer, create the customer.
        Both the dealer and customer start off with two cards.
        """
        self.deck = Deck()
        self.deck.shuffle()

        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])
        self.customer = Player([self.deck.deal(), self.deck.deal()])

    def play(self):
        """
        Play the game.
        """

        print("Customer:\n", self.customer)
        print("Dealer: \n", self.dealer)

        # Ask customer to draw cards until they decide to stop
        while True:
            user_input = input("Do you want to draw a card? [y/n]:")
            if user_input.strip().lower() == "y":
                self.customer.draw_card(self.deck)
                # Dealer may or may not pick a card
                self.dealer.draw_card(self.deck)
                print("Customer:\n", self.customer)
                print("Dealer:\n", self.dealer)
            else:
                break

            if self.customer.score >= 21:
                break

        # Last chance for dealer to draw a card
        self.dealer.draw_card(self.deck)
        print("\n\n~~~~~~GAME OVER~~~~~~\n")
        print("Customer:\n", self.customer)
        print("Dealer:\n", self.dealer)
        # After card drawing is over, check who won
        if self.customer.score > 21:
            print("Dealer won, you lost :(")
        elif self.dealer.score > 21:
            print("Dealer lost -- you win!")
        elif self.customer.score > self.dealer.score:
            print("You win!")
        else:
            print("Tie")


if __name__ == "__main__":
    p = TwentyOne()
    p.play()
