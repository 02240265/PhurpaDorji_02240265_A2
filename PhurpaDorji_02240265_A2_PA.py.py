import random

class ScoreBoard:
    """Class to keep track of scores for each game."""
    def __init__(self):
        self.scores = {
            "Guess Number": 0,
            "Rock Paper Scissors": 0,
            "Trivia": 0
        }

    def update_score(self, game_name, points):
        self.scores[game_name] += points

    def display_scores(self):
        print("\n=== Overall Score ===")
        for game, score in self.scores.items():
            print(f"{game}: {score}")
        print("=====================")


class GuessNumberGame:
    """Guess a number between 1 and 10."""
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def play(self):
        print("\n[Guess Number Game]")
        number = random.randint(1, 10)
        guesses = 0
        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
                guesses += 1
                if guess == number:
                    print("Correct! You guessed it!")
                    break
                else:
                    print("Wrong guess. Try again.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        score = max(0, 10 - guesses)
        self.scoreboard.update_score("Guess Number", score)
        print(f"Score for this game: {score}")


class RockPaperScissorsGame:
    """Play Rock-Paper-Scissors against the computer."""
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def play(self):
        print("\n[Rock Paper Scissors]")
        choices = ['rock', 'paper', 'scissors']
        wins = 0
        for _ in range(3):
            computer = random.choice(choices)
            user = input("Enter rock, paper, or scissors: ").lower()
            if user not in choices:
                print("Invalid input. You lose this round.")
                continue
            print(f"Computer chose: {computer}")
            if user == computer:
                print("It's a tie.")
            elif (user == "rock" and computer == "scissors") or \
                 (user == "paper" and computer == "rock") or \
                 (user == "scissors" and computer == "paper"):
                print("You win this round!")
                wins += 1
            else:
                print("You lose this round.")
        self.scoreboard.update_score("Rock Paper Scissors", wins)
        print(f"Wins this game: {wins}")


class TriviaGame:
    """Play a multiple-choice trivia game."""
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard
        self.questions = {
            "Science": {
                "question": "Which law explkains why we wear seatbelts(inertia)?",
                "options": ["a) Newton second law", "b) Newton first law", "c) newton third law", "d) Hookes law"],
                "answer": "b"
            },
            "CSF": {
                "question": "Which of the following statement is true regarding the data structure of python",
                "options": ["a) python list are same as traditional arrays", "b) sets are immutable", "c) python dictonary stores data in key value pair", "d) tuples are used to store unique values"],
                "answer": "c"
            }
        }

    def play(self):
        print("\n[Trivia Pursuit]")
        correct = 0
        for category, data in self.questions.items():
            print(f"\nCategory: {category}")
            print(data["question"])
            for option in data["options"]:
                print(option)
            answer = input("Enter your answer (a/b/c/d): ").lower()
            if answer == data["answer"]:
                print("Correct!")
                correct += 1
            else:
                print("Wrong!")
        self.scoreboard.update_score("Trivia", correct)
        print(f"Correct answers: {correct}")


class PokemonCardBinder:
    """Manage a Pokemon card binder."""
    def __init__(self):
        self.binder = []

    def manage(self):
        print("\n[Pokemon Card Binder Manager]")
        while True:
            print("\n1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View binder")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter Pokémon name: ")
                self.binder.append(name)
                print(f"{name} added.")
            elif choice == "2":
                self.binder.clear()
                print("Binder has been reset.")
            elif choice == "3":
                if not self.binder:
                    print("Binder is empty.")
                else:
                    print("Binder contents:")
                    for i, name in enumerate(self.binder, 1):
                        print(f"{i}. {name}")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter 1-4.")


class GameApp:
    """Main application controller."""
    def __init__(self):
        self.scoreboard = ScoreBoard()
        self.guess_game = GuessNumberGame(self.scoreboard)
        self.rps_game = RockPaperScissorsGame(self.scoreboard)
        self.trivia_game = TriviaGame(self.scoreboard)
        self.binder = PokemonCardBinder()

    def run(self):
        while True:
            print("\nSelect a function (0-5):")
            print("1. Guess Number Game")
            print("2. Rock Paper Scissors Game")
            print("3. Trivia Pursuit Game")
            print("4. Pokemon Card Binder Manager")
            print("5. Check Current Overall Score")
            print("0. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.guess_game.play()
            elif choice == "2":
                self.rps_game.play()
            elif choice == "3":
                self.trivia_game.play()
            elif choice == "4":
                self.binder.manage()
            elif choice == "5":
                self.scoreboard.display_scores()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please enter a number from 0 to 5.")


if __name__ == "__main__":
    GameApp().run()
