"""
The Lost Light Festival


How to Play:
1. Run the program in Python.
2. Enter your player name.
3. Choose menu options by typing the number shown.
4. Explore locations, collect items, solve puzzles,
   and help villagers.
5. Recover the magical lantern before sunset to win.

This game includes:
- Functions and a clear main() entry point
- Random and Time libraries
- Inventory system
- Multiple locations and puzzles
- Friendly interactions and story progression
"""

import random
import time


# --------------------------------------------------
# Utility Function
# --------------------------------------------------
def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# --------------------------------------------------
# Player Class
# Stores player information and inventory
# --------------------------------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.friendship = 0
        self.clues = 0
        self.location = "Village Square"

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            slow_print(f"You received: {item}")

    def show_inventory(self):
        if self.inventory:
            slow_print("Inventory:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            slow_print("Your inventory is empty.")


# --------------------------------------------------
# Main Game Class
# Handles gameplay, locations, and progression
# --------------------------------------------------
class Game:
    def __init__(self):
        self.player = None
        self.game_over = False
        self.festival_fixed = False

    def start(self):
        self.show_intro()
        name = input("Enter your adventurer name: ")
        self.player = Player(name)
        slow_print(f"\nWelcome, {name}! Your adventure begins now.\n")

        while not self.game_over:
            self.main_menu()

        # Display the game introduction and story
    def show_intro(self):
        slow_print("=" * 60)
        slow_print("      THE LOST LIGHT FESTIVAL")
        slow_print("=" * 60)
        slow_print(
            "The peaceful town of Everglen is preparing for its yearly "
            "Light Festival, but the magical lantern that powers the event "
            "has disappeared. Without it, the festival cannot begin."
        )
        slow_print(
            "Your mission is to explore the town, solve puzzles, help "
            "villagers, and recover the missing lantern before sunset."
        )
        print()

        # Main menu for player choices
    def main_menu(self):
        slow_print(f"\nCurrent Location: {self.player.location}")
        print("\nWhat would you like to do?")
        print("1. Visit the Library")
        print("2. Explore the Forest")
        print("3. Talk to Villagers")
        print("4. Visit the Market")
        print("5. Check Inventory")
        print("6. Solve the Mystery")
        print("7. Quit Game")

        choice = input("Choose an option: ")

        if choice == "1":
            self.visit_library()
        elif choice == "2":
            self.explore_forest()
        elif choice == "3":
            self.talk_villagers()
        elif choice == "4":
            self.visit_market()
        elif choice == "5":
            self.player.show_inventory()
        elif choice == "6":
            self.solve_mystery()
        elif choice == "7":
            slow_print("Thanks for playing!")
            self.game_over = True
        else:
            slow_print("Invalid choice. Please try again.")

        # Library location and riddle puzzle
    def visit_library(self):
        self.player.location = "Ancient Library"
        slow_print("\nYou enter the dusty library filled with old books.")

        if "Ancient Map" not in self.player.inventory:
            slow_print(
                "A librarian tells you about a hidden trail near the forest."
            )
            answer = input(
                "Solve this riddle to earn the Ancient Map:\n"
                "I have keys but no locks, space but no room. What am I? "
            ).lower()

            if "keyboard" in answer:
                slow_print("Correct! The librarian gives you an Ancient Map.")
                self.player.add_item("Ancient Map")
                self.player.clues += 1
            else:
                slow_print("That answer is incorrect. Try again later.")
        else:
            slow_print("You already explored the library thoroughly.")

        # Forest exploration area
    def explore_forest(self):
        self.player.location = "Whispering Forest"
        slow_print("\nYou walk into the Whispering Forest.")

        if "Ancient Map" in self.player.inventory:
            if "Crystal Key" not in self.player.inventory:
                slow_print(
                    "Using the Ancient Map, you discover a hidden puzzle door."
                )
                self.forest_puzzle()
            else:
                slow_print("The forest feels peaceful now that the puzzle is solved.")
        else:
            slow_print(
                "You get lost among the trees. Maybe you need a map first."
            )

        # Random number guessing puzzle
    def forest_puzzle(self):
        number = random.randint(1, 5)
        slow_print(
            "A glowing tree speaks:\n"
            "'Guess the number I am thinking of between 1 and 5.'"
        )

        try:
            guess = int(input("Your guess: "))

            if guess == number:
                slow_print(
                    "The tree glows brightly and reveals a Crystal Key!"
                )
                self.player.add_item("Crystal Key")
                self.player.clues += 1
            else:
                slow_print(
                    f"The tree whispers, 'Not quite. I was thinking of {number}.'"
                )
        except ValueError:
            slow_print("That is not a valid number.")

        # Friendly villager interactions
    def talk_villagers(self):
        self.player.location = "Village Square"
        slow_print("\nYou spend time speaking with the villagers.")

        villagers = [
            "A baker shares fresh bread with you.",
            "A musician teaches you a calming melody.",
            "A child tells you they saw strange lights near the market.",
            "An artist says kindness is the key to every mystery.",
        ]

        slow_print(random.choice(villagers))

        if self.player.friendship < 3:
            self.player.friendship += 1
            slow_print("Your friendship with the townspeople increases.")
        else:
            slow_print("The villagers already trust you deeply.")

        # Market location where player earns an item
    def visit_market(self):
        self.player.location = "Moonlight Market"
        slow_print("\nYou arrive at the colorful market.")

        if "Lantern Lens" not in self.player.inventory:
            if self.player.friendship >= 2:
                slow_print(
                    "A merchant appreciates your kindness and gives you a Lantern Lens."
                )
                self.player.add_item("Lantern Lens")
                self.player.clues += 1
            else:
                slow_print(
                    "The merchants seem unsure about you. Spend more time helping villagers."
                )
        else:
            slow_print("The market merchants wave at you warmly.")

        # Final challenge to solve the mystery
    def solve_mystery(self):
        slow_print("\nYou gather all the clues you have collected.")

        required_items = ["Ancient Map", "Crystal Key", "Lantern Lens"]

        missing_items = [
            item for item in required_items if item not in self.player.inventory
        ]

        if missing_items:
            slow_print("You are still missing important items:")
            for item in missing_items:
                print(f"- {item}")
            return

        slow_print(
            "With all the clues combined, you discover that the magical lantern "
            "was hidden inside the old town clock tower."
        )

        answer = input(
            "To unlock the tower, answer this final question:\n"
            "What quality helped you most throughout the adventure? "
        ).lower()

        positive_words = [
            "kindness",
            "friendship",
            "teamwork",
            "patience",
            "helpfulness",
            "compassion",
        ]

        if answer in positive_words:
            self.win_game()
        else:
            slow_print(
                "The tower remains silent. Perhaps the answer lies in the spirit of the town."
            )

        # Winning ending sequence
    def win_game(self):
        self.festival_fixed = True
        slow_print("\nThe clock tower doors open slowly.")
        slow_print(
            "Inside, you find the missing magical lantern glowing softly."
        )
        slow_print(
            "You return the lantern to the town square just before sunset."
        )
        slow_print(
            "The villagers cheer as the Light Festival begins with music, "
            "dancing, and glowing lanterns filling the sky."
        )
        slow_print(
            f"Congratulations, {self.player.name}! You saved the festival through kindness and wisdom."
        )
        slow_print("\nTHE END")
        self.game_over = True


# --------------------------------------------------
# Main Function
# --------------------------------------------------
def main():
    game = Game()
    game.start()


# Program entry point
if __name__ == "__main__":
    main()
