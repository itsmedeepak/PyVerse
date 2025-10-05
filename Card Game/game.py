from random import shuffle, random


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        return f"{self.values[self.value]} of {self.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = [Card(i, j) for i in range(2, 15) for j in range(4)]
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name, is_ai=False):
        self.wins = 0
        self.card = None
        self.name = name
        self.is_ai = is_ai  # flag for AI player


class Game:
    def __init__(self):
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name (or type 'AI' for computer): ")
        self.deck = Deck()
        self.p1 = Player(name1)
        # if name2 is "AI", create an AI player
        self.p2 = Player(name2, is_ai=(name2.lower() == "ai"))

    def wins(self, winner):
        print(f"{winner} wins this round")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f"{p1n} drew {p1c} | {p2n} drew {p2c}")

    def play_game(self):
        cards = self.deck.cards
        print("\n--- Beginning WAR! ---")
        while len(cards) >= 2:
            # AI player may randomly quit
            if self.p2.is_ai:
                ai_choice = random()  # value between 0 and 1
                if ai_choice < 0.1:   # 10% chance to quit
                    print(f"{self.p2.name} (AI) decided to quit the game!")
                    break
                else:
                    print(f"{self.p2.name} (AI) wants to play this round.")

            # Ask human player to continue
            response = input("Press Enter to play (or 'q' to quit): ")
            if response.lower() == 'q':
                break

            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            self.draw(p1n, p1c, p2n, p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print(f"\n--- War is over. {win} wins! ---")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"


if __name__ == "__main__":
    game = Game()
    game.play_game()
 
