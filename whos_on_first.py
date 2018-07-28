from utility import print_and_wait

class WhosOnFirst:
    # display word => button position to look up ([column, row])
    display_label_instructions = {
        "yes"      : [0, 1],
        "first"    : [1, 0],
        "display"  : [1, 2],
        "okay"     : [1, 0],
        "says"     : [1, 2],
        "nothing"  : [0, 1],
        "empty"    : [0, 2],
        "blank"    : [1, 1],
        "no"       : [1, 2],
        "led"      : [0, 1],
        "lead"     : [1, 2],
        "read"     : [1, 1],
        "red"      : [1, 1],
        "reed"     : [0, 2],
        "leed"     : [0, 2],
        "hold on"  : [1, 2],
        "you"      : [1, 1],
        "you are"  : [1, 2],
        "your"     : [1, 1],
        "you're"   : [1, 1],
        "ur"       : [0, 0],
        "there"    : [1, 2],
        "they're"  : [0, 2],
        "their"    : [1, 1],
        "they are" : [0, 1],
        "see"      : [1, 2],
        "c"        : [1, 0],
        "cee"      : [1, 2]
    }

    # Possible choices based on the corresponding button text
    corresponding_label = {
        "ready" : ["YES", "OKAY", "WHAT", "MIDDLE", "LEFT", "PRESS", "RIGHT", "BLANK", "READY", "NO", "FIRST", "UHHH", "NOTHING", "WAIT"],
        "first" : ["LEFT", "OKAY", "YES", "MIDDLE", "NO", "RIGHT", "NOTHING", "UHHH", "WAIT", "READY", "BLANK", "WHAT", "PRESS", "FIRST"],
        "no" : ["BLANK", "UHHH", "WAIT", "FIRST", "WHAT", "READY", "RIGHT", "YES", "NOTHING", "LEFT", "PRESS", "OKAY", "NO", "MIDDLE"],
        "blank" : ["WAIT", "RIGHT", "OKAY", "MIDDLE", "BLANK", "PRESS", "READY", "NOTHING", "NO", "WHAT", "LEFT", "UHHH", "YES", "FIRST"],
        "nothing" : ["UHHH", "RIGHT", "OKAY", "MIDDLE", "YES", "BLANK", "NO", "PRESS", "LEFT", "WHAT", "WAIT", "FIRST", "NOTHING", "READY"],
        "yes" : ["OKAY", "RIGHT", "UHHH", "MIDDLE", "FIRST", "WHAT", "PRESS", "READY", "NOTHING", "YES", "LEFT", "BLANK", "NO", "WAIT"],
        "what" : ["UHHH", "WHAT", "LEFT", "NOTHING", "READY", "BLANK", "MIDDLE", "NO", "OKAY", "FIRST", "WAIT", "YES", "PRESS", "RIGHT"],
        "uhhh" : ["READY", "NOTHING", "LEFT", "WHAT", "OKAY", "YES", "RIGHT", "NO", "PRESS", "BLANK", "UHHH", "MIDDLE", "WAIT", "FIRST"],
        "left" : ["RIGHT", "LEFT", "FIRST", "NO", "MIDDLE", "YES", "BLANK", "WHAT", "UHHH", "WAIT", "PRESS", "READY", "OKAY", "NOTHING"],
        "right" : ["YES", "NOTHING", "READY", "PRESS", "NO", "WAIT", "WHAT", "RIGHT", "MIDDLE", "LEFT", "UHHH", "BLANK", "OKAY", "FIRST"],
        "middle" : ["BLANK", "READY", "OKAY", "WHAT", "NOTHING", "PRESS", "NO", "WAIT", "LEFT", "MIDDLE", "RIGHT", "FIRST", "UHHH", "YES"],
        "okay" : ["MIDDLE", "NO", "FIRST", "YES", "UHHH", "NOTHING", "WAIT", "OKAY", "LEFT", "READY", "BLANK", "PRESS", "WHAT", "RIGHT"],
        "wait" : ["UHHH", "NO", "BLANK", "OKAY", "YES", "LEFT", "FIRST", "PRESS", "WHAT", "WAIT", "NOTHING", "READY", "RIGHT", "MIDDLE"],
        "press" : ["RIGHT", "MIDDLE", "YES", "READY", "PRESS", "OKAY", "NOTHING", "UHHH", "BLANK", "LEFT", "FIRST", "WHAT", "NO", "WAIT"],
        "you" : ["SURE", "YOU ARE", "YOUR", "YOU'RE", "NEXT", "UH HUH", "UR", "HOLD", "WHAT?", "YOU", "UH UH", "LIKE", "DONE", "U"],
        "you are" : ["YOUR", "NEXT", "LIKE", "UH HUH", "WHAT?", "DONE", "UH UH", "HOLD", "YOU", "U", "YOU'RE", "SURE", "UR", "YOU ARE"],
        "your" : ["UH UH", "YOU ARE", "UH HUH", "YOUR", "NEXT", "UR", "SURE", "U", "YOU'RE", "YOU", "WHAT?", "HOLD", "LIKE", "DONE"],
        "you're" : ["YOU", "YOU'RE", "UR", "NEXT", "UH UH", "YOU ARE", "U", "YOUR", "WHAT?", "UH HUH", "SURE", "DONE", "LIKE", "HOLD"],
        "ur" : ["DONE", "U", "UR", "UH HUH", "WHAT?", "SURE", "YOUR", "HOLD", "YOU'RE", "LIKE", "NEXT", "UH UH", "YOU ARE", "YOU"],
        "u" : ["UH HUH", "SURE", "NEXT", "WHAT?", "YOU'RE", "UR", "UH UH", "DONE", "U", "YOU", "LIKE", "HOLD", "YOU ARE", "YOUR"],
        "uh huh" : ["UH HUH", "YOUR", "YOU ARE", "YOU", "DONE", "HOLD", "UH UH", "NEXT", "SURE", "LIKE", "YOU'RE", "UR", "U", "WHAT?"],
        "uh uh" : ["UR", "U", "YOU ARE", "YOU'RE", "NEXT", "UH UH", "DONE", "YOU", "UH HUH", "LIKE", "YOUR", "SURE", "HOLD", "WHAT?"],
        "what?" : ["YOU", "HOLD", "YOU'RE", "YOUR", "U", "DONE", "UH UH", "LIKE", "YOU ARE", "UH HUH", "UR", "NEXT", "WHAT?", "SURE"],
        "done" : ["SURE", "UH HUH", "NEXT", "WHAT?", "YOUR", "UR", "YOU'RE", "HOLD", "LIKE", "YOU", "U", "YOU ARE", "UH UH", "DONE"],
        "next" : ["WHAT?", "UH HUH", "UH UH", "YOUR", "HOLD", "SURE", "NEXT", "LIKE", "DONE", "YOU ARE", "UR", "YOU'RE", "U", "YOU"],
        "hold" : ["YOU ARE", "U", "DONE", "UH UH", "YOU", "UR", "SURE", "WHAT?", "YOU'RE", "NEXT", "HOLD", "UH HUH", "YOUR", "LIKE"],
        "sure" : ["YOU ARE", "DONE", "LIKE", "YOU'RE", "YOU", "HOLD", "UH HUH", "UR", "SURE", "U", "WHAT?", "NEXT", "YOUR", "UH UH"],
        "like" : ["YOU'RE", "NEXT", "U", "UR", "HOLD", "DONE", "UH UH", "WHAT?", "UH HUH", "YOU", "LIKE", "SURE", "YOU ARE", "YOUR"]
    }

    def start_whos_on_first(self):
        round_number = 1

        while round_number < 4:
            print(f"Round {round_number}")
            display_word = self.get_display_word() # Get the display text
            user_buttons = self.get_all_buttons() # Get the button texts

            # Solved!
            print_and_wait(self.solve_whos_on_first(display_word, user_buttons), "Press the following button:")
            round_number += 1

    def get_display_word(self):
        display_word = input("What word appears on the display? If it's empty, enter `empty`: ").lower()
        
        # Ensure the display word is valid
        if display_word in self.display_label_instructions:
            return display_word
        else:
            print_and_wait("Invalid display word, please try again.")
            return self.get_display_word()

    def get_all_buttons(self):
        # Get each column of button texts from the user
        first_column = [x for x in input("Enter each button from the first column, seperated by a comma: ").split(",")]
        second_column = [x for x in input("Enter each button from the second column, seperated by a comma: ").split(",")]

        if self.verify_columns(first_column, second_column):
            return [first_column, second_column]
        else:
            # Display text that the user entered doesn't exist, try again
            print_and_wait("An error occurred. Make sure you type the words correctly.")
            return self.get_all_buttons()

    def verify_columns(self, first_column, second_column):
        valid_labels = ["ready", "first", "no", "blank", "nothing", "yes", "what", "uhhh", "left", "right",
                        "middle", "okay", "wait", "press", "you", "you are", "your", "you're", "ur", "u",
                        "uh huh", "uh uh", "what?", "done", "next", "hold", "sure", "like"]

        # Verify column lengths
        if len(first_column) != 3 or len(second_column) != 3:
            return False

        # Verify valid labels for the first column
        for label in first_column:
            if label not in valid_labels:
                return False

        # Verify valid labels for the second column
        for label in second_column:
            if label not in valid_labels:
                return False

        return True


    def get_first_word(self, correct_list, user_buttons):
        # Gets the word that the user should press
        flattened_user_buttons = user_buttons[0] + user_buttons[1] # 2D list => 1D list
        # Returns the button that the user needs to press
        for word in correct_list:
            if word.lower() in flattened_user_buttons:
                return word

    def solve_whos_on_first(self, display_word, user_buttons):
        # Does most of the heavy lifting for solving this module

        # Check that the display is correct (exists)
        if self.display_label_instructions[display_word]:
            # Get the correct button text
            correct_word = self.display_label_instructions[display_word]
            button_text = user_buttons[correct_word[0]][correct_word[1]]
            # Check that the button text is correct (exists)
            if self.corresponding_label[button_text]:
                correct_list = self.corresponding_label[button_text] # Contains the answer that the user would search for
                return self.get_first_word(correct_list, user_buttons) # Return the correct word
            else:
                # Button text that the user entered doesn't exist, try again
                print_and_wait("An error occurred. Make sure you type the button text correctly.")
                self.start_whos_on_first()
        else:
            # Display text that the user entered doesn't exist, try again
            print_and_wait("An error occurred. Make sure you type the display correctly.")
            self.start_whos_on_first()
