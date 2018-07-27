class WhosOnFirst:
    # What to do based on what word the display is displaying
    display_label_instructions = {
        "yes"      : "What text is on the button on the second row of the first column? ",
        "first"    : "What text is on the button on the first row of the second column? ",
        "display"  : "What text is on the button on the third row of the second column? ",
        "okay"     : "What text is on the button on the first row of the second column? ",
        "says"     : "What text is on the button on the third row of the second column? ",
        "nothing"  : "What text is on the button on the second row of the first column? ",
        "empty"    : "What text is on the button on the third row of the first column? ",
        "blank"    : "What text is on the button on the second row of the second column? ",
        "no"       : "What text is on the button on the third row of the second column? ",
        "led"      : "What text is on the button on the second row of the first column? ",
        "lead"     : "What text is on the button on the third row of the second column? ",
        "read"     : "What text is on the button on the second row of the second column? ",
        "red"      : "What text is on the button on the second row of the second column? ",
        "reed"     : "What text is on the button on the third row of the first column? ",
        "leed"     : "What text is on the button on the third row of the first column? ",
        "hold on"  : "What text is on the button on the third row of the second column? ",
        "you"      : "What text is on the button on the second row of the second column? ",
        "you are"  : "What text is on the button on the third row of the second column? ",
        "your"     : "What text is on the button on the second row of the second column? ",
        "you're"   : "What text is on the button on the second row of the second column? ",
        "ur"       : "What text is on the button on the first row of the first column? ",
        "there"    : "What text is on the button on the third row of the second column? ",
        "they're"  : "What text is on the button on the third row of the first column? ",
        "their"    : "What text is on the button on the second row of the second column? ",
        "they are" : "What text is on the button on the second row of the first column? ",
        "see"      : "What text is on the button on the third row of the second column? ",
        "c"        : "What text is on the button on the first row of the second column? ",
        "cee"      : "What text is on the button on the third row of the second column? "
    }

    # Possible choices based on the corresponding button text
    corresponding_label = {
        "ready" : "YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY, NO, FIRST, UHHH, NOTHING, WAIT",
        "first" : "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST",
        "no" : "BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO, MIDDLE",
        "blank" : "WAIT, RIGHT, OKAY, MIDDLE, BLANK, PRESS, READY, NOTHING, NO, WHAT, LEFT, UHHH, YES, FIRST",
        "nothing" : "UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING, READY",
        "yes" : "OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES, LEFT, BLANK, NO, WAIT",
        "what" : "UHHH, WHAT, LEFT, NOTHING, READY, BLANK, MIDDLE, NO, OKAY, FIRST, WAIT, YES, PRESS, RIGHT",
        "uhhh" : "READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH, MIDDLE, WAIT, FIRST",
        "left" : "RIGHT, LEFT, FIRST, NO, MIDDLE, YES, BLANK, WHAT, UHHH, WAIT, PRESS, READY, OKAY, NOTHING",
        "right" : "YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT, MIDDLE, LEFT, UHHH, BLANK, OKAY, FIRST",
        "middle" : "BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE, RIGHT, FIRST, UHHH, YES",
        "okay" : "MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY, LEFT, READY, BLANK, PRESS, WHAT, RIGHT",
        "wait" : "UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT, NOTHING, READY, RIGHT, MIDDLE",
        "press" : "RIGHT, MIDDLE, YES, READY, PRESS, OKAY, NOTHING, UHHH, BLANK, LEFT, FIRST, WHAT, NO, WAIT",
        "you" : "SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU, UH UH, LIKE, DONE, U",
        "you are" : "YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE",
        "your" : "UH UH, YOU ARE, UH HUH, YOUR, NEXT, UR, SURE, U, YOU'RE, YOU, WHAT?, HOLD, LIKE, DONE",
        "you're" : "YOU, YOU'RE, UR, NEXT, UH UH, YOU ARE, U, YOUR, WHAT?, UH HUH, SURE, DONE, LIKE, HOLD",
        "ur" : "DONE, U, UR, UH HUH, WHAT?, SURE, YOUR, HOLD, YOU'RE, LIKE, NEXT, UH UH, YOU ARE, YOU",
        "u" : "UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U, YOU, LIKE, HOLD, YOU ARE, YOUR",
        "uh huh" : "UH HUH, YOUR, YOU ARE, YOU, DONE, HOLD, UH UH, NEXT, SURE, LIKE, YOU'RE, UR, U, WHAT?",
        "uh uh" : "UR, U, YOU ARE, YOU'RE, NEXT, UH UH, DONE, YOU, UH HUH, LIKE, YOUR, SURE, HOLD, WHAT?",
        "what?" : "YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?, SURE",
        "done" : "SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE",
        "next" : "WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT, LIKE, DONE, YOU ARE, UR, YOU'RE, U, YOU",
        "hold" : "YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD, UH HUH, YOUR, LIKE",
        "sure" : "YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE, U, WHAT?, NEXT, YOUR, UH UH",
        "like" : "YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE, SURE, YOU ARE, YOUR"
    }

    def start_whos_on_first(self, bomb, round_number):
        # Get the display text
        display = input("What word appears on the display? If it's empty, enter `empty`: ").lower()

        # Check that the display is correct (exists)
        if self.display_label_instructions[display]:
            # Get the correct button text
            button_text = input(self.display_label_instructions[display]).lower()

            # Check that the button text is correct (exists)
            if self.corresponding_label[button_text]:
                print("Push the first button on your screen that appears on this list:")
                print(self.corresponding_label[button_text])

                # Do this three times to complete the module
                if round_number < 2:
                    round_number = round_number + 1
                    self.start_whos_on_first(bomb, round_number)
            else:
                # Button text that the user entered doesn't exist, try again
                print("An error occurred. Make sure you type the button text correctly.")
                self.start_whos_on_first(bomb, round_number)
        else:
            # Display text that the user entered doesn't exist, try again
            print("An error occurred. Make sure you type the display correctly.")
            self.start_whos_on_first(bomb, round_number)