from utility import print_and_wait

class MorseCode:
    frequencies = {
        "shell": 505,
        "halls": 515,
        "slick": 522,
        "trick": 532,
        "boxes": 535,
        "leaks": 542,
        "strobe": 545,
        "bistro": 552,
        "flick": 555,
        "bombs": 565,
        "break": 572,
        "brick": 575,
        "steak": 582,
        "sting": 592,
        "vector": 595,
        "beats": 600
    }

    morse_code_lookup = {
        '.-'   : 'a',
        '-...' : 'b',
        '-.-.' : 'c',
        '-..'  : 'd',
        '.'    : 'e',
        '..-.' : 'f',
        '--.'  : 'g',
        '....' : 'h',
        '..'   : 'i',
        '.---' : 'j',
        '-.-'  : 'k',
        '.-..' : 'l',
        '--'   : 'm',
        '-.'   : 'n',
        '---'  : 'o',
        '.--.' : 'p',
        '--.-' : 'q',
        '.-.'  : 'r',
        '...'  : 's',
        '-'    : 't',
        '..-'  : 'u',
        '...-' : 'v',
        '.--'  : 'w',
        '-..-' : 'x',
        '-.--' : 'y',
        '--..' : 'z'
    }

    def start_morse_code(self):
        # Input the actual dots and dashes
        morse_code = self.get_morse_code()
        # Convert the morse characters into letters by looking each character up
        word = self.translate_morse_code(morse_code)

        try:
            # Print the resulting frequency if it exists
            print_and_wait(f"Respond at frequency `3.{self.frequencies[word]}`.")
            return
        except KeyError:
            # The user interpreted the morse code incorrectly
            print_and_wait("An error occurred! Please try again.")
            self.start_morse_code()
            
    def get_morse_code(self):
        # Gets and returns the user's morse code interpretation
        morse_code = input("Input each morse code character seperated by a space. ")
        return morse_code

    def translate_morse_code(self, morse_code):
        # Takes the user's morse code and translates it into a word based on the table
        try:
            word_list = [self.morse_code_lookup[x] for x in morse_code.split(' ')]
            return ''.join(word_list)
        except KeyError:
            # The user interpreted the morse code incorrectly
            print_and_wait("An error occurred! Please try again.")
            self.start_morse_code()