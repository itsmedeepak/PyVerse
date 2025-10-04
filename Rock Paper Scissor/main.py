import random


class RockPaperScissors:
    def __init__(self):
        self.user1 = ""
        self.user1_score = 0
        self.user2 = ""
        self.user2_score = 0
        self.rounds = 5

    def my_new_user(self):
        """
        Create 2 users with default 5 rounds.
        Optionally allow changing the number of rounds.
        """
        self.user1, self.user2 = input("Enter Username-").split()

        change = (
            input(
                "Rock Paper Scissor starting...\n"
                "5 rounds are going to be played. Want to change [y/n] - "
            )
            .strip()
            .lower()
        )

        if change not in ["y", "n"]:
            raise ValueError("Invalid decision")

        if change == "y":
            rounds = int(input("Enter number of rounds you want to play- ").strip())
            if isinstance(rounds, int):
                if rounds < 1:
                    raise ValueError("Rounds can't be smaller than 1")
                self.rounds = rounds
            else:
                raise ValueError("Invalid round number")

    def my_action(self):
        """Generate random action from Rock, Paper, Scissor."""
        return random.choice(["Rock", "Paper", "Scissor"])

    def increase_score(self, user):
        """Increase score for the given user (user1 or user2)."""
        if user == "user1":
            self.user1_score += 1
        else:
            self.user2_score += 1

    def evaluate(self, user1_action, user2_action, round_no):
        """
        Evaluate round result based on actions and
        update the scores accordingly.
        """
        print(f"\n**** Round {round_no} starts ****")
        print(f"{self.user1} move {user1_action}," f"{self.user2} move {user2_action}")

        if user1_action == user2_action:
            self.increase_score("user1")
            self.increase_score("user2")
            round_won = "is tied"
        else:
            if user1_action == "Rock":
                if user2_action == "Paper":
                    res = "user2"
                    round_won = f"won by {self.user2}"
                else:
                    res = "user1"
                    round_won = f"won by {self.user1}"

            elif user1_action == "Paper":
                if user2_action == "Scissor":
                    res = "user2"
                    round_won = f"won by {self.user2}"
                else:
                    res = "user1"
                    round_won = f"won by {self.user1}"

            else:
                if user2_action == "Rock":
                    res = "user2"
                    round_won = f"won by {self.user2}"
                else:
                    res = "user1"
                    round_won = f"won by {self.user1}"

            self.increase_score(res)

        print(
            f"This round {round_won}, score: "
            f"{self.user1} {self.user1_score} -"
            f" {self.user2} {self.user2_score}"
        )

    def serve_final_result(self):
        """Display final result after all rounds are completed."""

        print("\n**** Final Result ****")
        if self.user1_score > self.user2_score:

            print(
                f"{self.user1} won this game with score "
                f"{self.user1_score} - {self.user2_score}"
            )

        elif self.user1_score < self.user2_score:

            print(
                f"{self.user2} won this game with score "
                f"{self.user2_score} - {self.user1_score}"
            )

        else:

            print(
                f"This Game ties with score " f"{self.user1_score} - {self.user2_score}"
            )


try:
    game_instance = RockPaperScissors()
    game_instance.my_new_user()
    for i in range(1, game_instance.rounds + 1):
        user1_action = game_instance.my_action()
        user2_action = game_instance.my_action()
        game_instance.evaluate(user1_action, user2_action, i)

    game_instance.serve_final_result()
except Exception as e:
    print(f"Error: {e}")
