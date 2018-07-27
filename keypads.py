from utility import print_list

class Keypads:
    # All the symbols from each column in one list
    all_symbols = [
        "Ping Pong", "Illuminati", "Lambda", "Lightning Bolt", "Cat", "H", "Backwards C", "Dotted E",
        "Pube", "White Star", "Question Mark", "Copyright", "Boobs", "Mirrored K", "Broken 3", "6",
        "Paragraph", "BT", "Psi", "Smiley", "Hashtag", "C", "AE", "Bunny Snake", "Black Star", "N", 
        "Omega"]

    # The symbols broken up into their respective columns
    all_columns = [
        ["Ping Pong", "Illuminati", "Lambda", "Lightning Bolt", "Cat", "H", "Backwards C"], 
        ["Dotted E", "Ping Pong", "Backwards C", "Pube", "White Star", "H", "Question Mark"],
        ["Copyright", "Boobs", "Pube", "Mirrored K", "Broken 3", "Lambda", "White Star"],
        ["6", "Paragraph", "BT", "Cat", "Mirrored K", "Question Mark", "Smiley"],
        ["Psi", "Smiley", "BT", "C", "Paragraph", "Bunny Snake", "Black Star"],
        ["6", "Dotted E", "Hashtag", "AE", "Psi", "N", "Omega"]]

    def start_keypads(self):
        # Get user's symbols
        user_symbols = self.get_user_symbols()
        # Given user's symbols, find the correct column
        correct_column = self.find_correct_column(user_symbols)
        correct_order = []

        # Go through the list and search for the user's symbols
        # in order
        for symbol in correct_column:
            if symbol in user_symbols:
                correct_order.append(symbol)

        print("Click the symbols in the following order:")
        # Return the correct order to click the symbols
        for symbol in correct_order:
            print(symbol)

    def get_user_symbols(self):
        # Asks the user for the symbols on their keypad and returns them as a list
        print("Please enter the symbols that are on your keypad. All of the symbols "\
              "are printed here: \n")
        print_list(self.all_symbols, 5)

        symbol_one = self.get_symbol_input()
        symbol_two = self.get_symbol_input()
        symbol_three = self.get_symbol_input()
        symbol_four = self.get_symbol_input()

        symbol_list = [symbol_one, symbol_two, symbol_three, symbol_four]

        # If no column has all of the user's symbols, make them re-enter them
        if not self.find_correct_column(symbol_list):
            print("\nThere was an error. Ensure your symbols are correct.\n") # Press any button to continue (make user acknowledge error)
            return self.get_user_symbols()

        return symbol_list

    def get_symbol_input(self):
        # Accepts input for a symbol, ensuring it's in the list of all symbols
        lower_list = [x.lower() for x in self.all_symbols]
        symbol = input("Enter one of the four symbols: ")

        # If the symbol is not valid, ask them to re-enter that symbol
        if symbol.lower() not in lower_list:
            print("That is an invalid symbol. Please refer to the symbols above.")
            return self.get_symbol_input()
        else:
            return symbol

    def find_correct_column(self, user_symbols):
        # Checks that all four user symbols exist in one of the columns of symbols
        lower_column = [[x.lower() for x in i] for i in self.all_columns]
        lower_user_symbols = [x.lower() for x in user_symbols]
        correct_column = None

        for column in lower_column:
            # If the set of user symbols is a subset of a column, then all
            # the symbols must exist in that column
            if set(lower_user_symbols).issubset(set(column)):
                correct_column = column

        return correct_column