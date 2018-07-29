from utility import print_and_wait

class SimonSays:
    # Use for translating a color when the bomb has vowels in the serial number
    # Blinking color => [no strikes, one strike, two strikes]
    translate_with_vowels = {
        "red": ["blue", "yellow", "green"],
        "blue": ["red", "green", "red"],
        "green": ["yellow", "blue", "yellow"],
        "yellow": ["green", "red", "blue"]
    }

    # Use for translating a color when the bomb has no vowels in the serial number
    # Blinking color => [no strikes, one strike, two strikes]
    translate_without_vowels = {
        "red": ["blue", "red", "yellow"],
        "blue": ["yellow", "blue", "green"],
        "green": ["green", "yellow", "blue"],
        "yellow": ["red", "green", "red"]
    }

    def start_simon_says(self, bomb):
        # Solves and prints the solution to the module
        bomb_contains_vowel = bomb.vowel_in_serial()

        # Perform all 4 rounds
        for curr_round in range(1, 5):
            num_strikes = bomb.ask_strikes() # Number of strikes changes what color to press, ask each time
            print_and_wait(self.solve_simon_says(bomb_contains_vowel, num_strikes, curr_round))
        return

    def solve_simon_says(self, bomb_contains_vowel, num_strikes, curr_round):
        # Translates the user's flashing colors into the correct colors to press
        original_flash_colors = input("Enter the flash of each color, seperated by a space: ").strip().split()
        translated_colors = [] # Stores the correct colors to press in a list

        # Ensure the correct number of colors are entered
        if len(original_flash_colors) != curr_round:
            print_and_wait(f"There should be {curr_round} color(s). Please re-enter the numbers or restart.")
            return self.solve_simon_says(bomb_contains_vowel, num_strikes, curr_round)

        # Go through each color, translating them all
        for color in original_flash_colors:
            try:
                # Check which table should be used to translate the colors
                if bomb_contains_vowel:
                    translated_colors.append(self.translate_with_vowels[color.lower()][num_strikes])
                else:
                    translated_colors.append(self.translate_without_vowels[color.lower()][num_strikes])
            except KeyError:
                print_and_wait("Invalid color detected. Please try again.")
                return self.solve_simon_says(bomb_contains_vowel, num_strikes, curr_round)
        
        # Create a string to return to the user containing the correct colors
        colors_to_press = ", ".join(str(color) for color in translated_colors)
        return f"Press the following buttons in this order: {colors_to_press}"