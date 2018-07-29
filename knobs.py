from utility import print_and_wait

class Knobs:
    # Contains the different LED patterns that are valid
    knobs_lookup = {
        "up" : [[[0, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1]], [[1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1]]],
        "down" : [[[0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, 1]], [[1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1]]],
        "left" : [[[0, 0, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1]], [[0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0]]],
        "right" : [[[1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0]], [[1, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0]]]
    }

    def start_knobs(self):
        print("There are two V-shaped rows of LED's. Let `0` indicate an unlit LED, and `1` indicate a lit LED. Seperate each by a space:")
        # Get both columns of LED's
        led_rows = self.get_led_rows()

        # Search for a match and tell user where to move knob
        for direction in self.knobs_lookup:
            for lst in self.knobs_lookup[direction]:
                if led_rows == lst:
                    print_and_wait(f"Move the knob `{direction}` relative to the `UP` label.")
                    return
        # There was no match, so restart!
        print_and_wait("There was no match found. Please re-enter the LED rows.")
        self.start_knobs()

    def get_led_rows(self):
        led_row_1 = input("Enter the first row of LED's: ").strip().split()
        led_row_2 = input("Enter the second row of LED's: ").strip().split()
        
        # Validate that the lists are the correct length
        if self.validate_led_list(led_row_1, led_row_2):
            led_2d_list = [led_row_1, led_row_2]
            # Safe because validate_led_list checks for int elems
            return [[int(element) for element in lst] for lst in led_2d_list]
        else:
            print_and_wait("There was an error with your LED lists. Please try again.")
            return self.get_led_rows()

    def validate_led_list(self, list_1, list_2):
        # Checks to make sure the user's list of LED's is of the right length and content
        if len(list_1) and len(list_2) == 6: # Each row has 6 LED's
            for (elem_1, elem_2) in zip(list_1, list_2):
                try:
                    if int(elem_1) not in [0, 1] or int(elem_2) not in [0, 1]:
                        return False # Elements not valid (element not in {0, 1})
                except ValueError:
                    return False # non-int input
            return True
        return False # Lengths not correct