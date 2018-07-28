from utility import print_and_wait

class Button:
    # strip color => release when timer has _ in any position
    strip_release = {
        "blue" : 4,
        "white" : 1,
        "yellow" : 5
        # default : 1
    }

    # The colors that the button can be
    valid_button_colors = ["red", "blue", "white", "yellow"]

    def start_button(self, bomb):
        # Begin the solving!
        batteries = bomb.num_batteries
        indicators = bomb.lit_indicators
        button_color = self.get_button_color()
        button_text = self.get_button_text()

        # Print the directions
        print_and_wait(self.button_sequence(batteries, indicators, button_color, button_text))
        return

    def get_button_color(self):
        # Asks for and returns the color of the button
        button_color = input("What color is the button? ")

        # Check that the button color is valid
        if button_color.lower() in self.valid_button_colors:
            return button_color
        else:
            print_and_wait("Invalid button color. Please try again.")
            return self.get_button_color()

    def get_button_text(self):
        # Asks for and returns the text on the button
        button_text = input("What is the text on the button? ")
        return button_text

    def strip_sequence(self):
        # Asks for and returns the color of the strip next to the button
        strip_color = input("Hold the button down. A strip of color will appear next to the button. What color is it? ")
        return self.releasing_held_button(strip_color)

    def button_sequence(self, num_batteries, lit_indicators, button_color, button_text):
        # Go through the 7 steps of solving the button module
        if button_color.lower() == "blue" and button_text.lower() == "abort": # Step 1
            return f"Release when the countdown timer has a {self.strip_sequence()} in any position."
        elif num_batteries > 1 and button_text.lower() == "detonate": # Step 2
            return "Press and immediately release the button."
        elif button_color.lower() == "white" and "CAR" in lit_indicators:
            return f"Release when the countdown timer has a {self.strip_sequence()} in any position."
        elif num_batteries > 2 and "FRK" in lit_indicators:
            return "Press and immediately release the button."
        elif button_color.lower() == "yellow":
            return f"Release when the countdown timer has a {self.strip_sequence()} in any position."
        elif button_color.lower() == "red" and button_text.lower() == "hold":
            return "Press and immediately release the button."
        else:
            return f"Release when the countdown timer has a {self.strip_sequence()} in any position."

    def releasing_held_button(self, strip_color):
        # Return the number to release on, defaulting to one
        return self.strip_release.get(strip_color, 1)