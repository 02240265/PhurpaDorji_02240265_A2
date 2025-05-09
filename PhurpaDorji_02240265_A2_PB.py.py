import math

class PokemonCard:
    def __init__(self, pokedex_number):
        self.pokedex_number = pokedex_number
        self.page = self.calculate_page()
        self.row, self.col = self.calculate_position()

    def calculate_page(self):
        # Each page can hold 64 cards. Pages start at 1.
        return (self.pokedex_number - 1) // 64 + 1

    def calculate_position(self):
        # Grid: 8 rows x 8 columns. Index starts at 1.
        index_on_page = (self.pokedex_number - 1) % 64
        row = index_on_page // 8 + 1
        col = index_on_page % 8 + 1
        return row, col


class Binder:
    def __init__(self):
        # Dictionary to map Pokedex number -> PokemonCard
        self.cards = {}
        self.max_pokedex = 1025

    def add_card(self, pokedex_number):
        if not (1 <= pokedex_number <= self.max_pokedex):
            return "Invalid Pokedex number. Must be between 1 and 1025."
        if pokedex_number in self.cards:
            card = self.cards[pokedex_number]
            return (f"Page: {card.page}\n"
                    f"Position: Row {card.row}, Column {card.col}\n"
                    f"Status: Pokedex #{pokedex_number} already exists in binder")

        card = PokemonCard(pokedex_number)
        self.cards[pokedex_number] = card
        return (f"Page: {card.page}\n"
                f"Position: Row {card.row}, Column {card.col}\n"
                f"Status: Added Pokedex #{pokedex_number} to binder")

    def view_contents(self):
        if not self.cards:
            return ("Current Binder Contents:\n------------------------\n"
                    "The binder is empty.\n"
                    "Total cards in binder: 0\n% completion: 0%")
        
        output = ["Current Binder Contents:", "------------------------"]
        for number in sorted(self.cards):
            card = self.cards[number]
            output.append(f"Pokedex #{number}:\nPage: {card.page}\nPosition: Row {card.row}, Column {card.col}")
        total = len(self.cards)
        percent = round((total / self.max_pokedex) * 100, 1)
        output.append("------------------------")
        output.append(f"Total cards in binder: {total}\n% completion: {percent}%")
        if total == self.max_pokedex:
            output.append("You have caught them all!!")
        return "\n".join(output)

    def reset_binder(self, confirmation):
        if confirmation.upper() == "CONFIRM":
            self.cards.clear()
            return "The binder reset was successful! All cards have been removed."
        elif confirmation.upper() == "EXIT":
            return "Reset cancelled. Returning to Main Menu."
        else:
            return "Invalid input. Type 'CONFIRM' to reset or 'EXIT' to cancel."

    def get_total_cards(self):
        return len(self.cards)


class CardBinderApp:
    def __init__(self):
        self.binder = Binder()

    def run(self):
        print("Welcome to Pokemon Card Binder Manager!")
        while True:
            print("""
Main Menu:
1. Add Pokemon card
2. Reset binder
3. View current placements
4. Exit""")
            choice = input("Select option: ").strip()

            if choice == '1':
                try:
                    number = int(input("Enter Pokedex number: ").strip())
                    result = self.binder.add_card(number)
                    print("\n" + result)
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            elif choice == '2':
                print("WARNING: This will delete ALL Pokemon cards from the binder.\n"
                      "This action cannot be undone.")
                confirm = input("Type 'CONFIRM' to reset or 'EXIT' to return to the Main Menu: ").strip()
                result = self.binder.reset_binder(confirm)
                print(result)

            elif choice == '3':
                print("\n" + self.binder.view_contents())

            elif choice == '4':
                print("Thank you for using Pokemon Card Binder Manager!")
                break

            else:
                print("Invalid option. Please select from the menu.")


# Entry point
if __name__ == "__main__":
    app = CardBinderApp()
    app.run()
