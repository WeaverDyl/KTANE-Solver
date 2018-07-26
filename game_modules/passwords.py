class Passwords:    
    def start_passwords(self):
        user_characters = input("Enter all letters with no seperation (30 letters total): ")
        # Split the characters up into their seperate columns (each column has 5 characters)
        split_chars = [user_characters[i : i + 6] for i in range(0, len(user_characters), 6)]
        # Find the word based on the columns of letters
        word = self.solve(split_chars) 

        print(f"The word is `{word}`.")
        return

    def solve(self, columns):
        # The potential passwords
        valid_passwords = ['about', 'after', 'again', 'below', 'could',
                           'every', 'first', 'found', 'great', 'house',
                           'large', 'learn', 'never', 'other', 'place',
                           'plant', 'point', 'right', 'small', 'sound',
                           'spell', 'still', 'study', 'their', 'there',
                           'these', 'thing', 'think', 'three', 'water',
                           'where', 'which', 'world', 'would', 'write']

        # For each index, add the possible word if the letter at the current index
        # is in the column at the current index
        for index, letters in enumerate(columns):
            possible_words = [word for word in valid_passwords if word[index] in letters]

        # Go through and check that each letter matches each column, since
        # there is only one solution
        for word in possible_words:
            for index, letter in enumerate(word):
                if letter not in columns[index]:
                    # If the letter is not in the column, remove it and check
                    # the next word
                    possible_words.remove(word)
                    break

        # Return the result
        return possible_words[0]