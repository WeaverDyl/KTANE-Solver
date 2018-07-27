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

    def start_morse_code(self, bomb):
        # Input the actual dots and dashes
        morse_code = input("Input each morse code character seperated by a space. ")
        # Convert the morse characters into letters by looking each character up
        word = [self.morse_code_lookup[x] for x in morse_code.split(' ')]
        # Combine the list of letters into the word!
        result = ''.join(word)

        try:
            # Print the resulting frequency if it exists
            print(f"Respond at frequency 3.{self.frequencies[result]}")
            return
        except KeyError:
            # The user interpreted the morse code incorrectly
            print("An error occurred! Please try again.")
            self.start_morse_code(bomb)