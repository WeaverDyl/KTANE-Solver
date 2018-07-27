from inflection import ordinalize
from utility import print_and_wait

class WireSet:
    # Contains the current count of each color wire that has been seen
    def __init__(self, red=0, blue=0, black=0):
        self.red = red
        self.blue = blue
        self.black = black

    def modify_wire_number(self, color, modifier):
        # Used to increment the current wire color's count
        current_count = getattr(self, color)
        setattr(self, color, current_count + modifier)

class Wire:
    # Represents a single wire, containing a color and connection
    def __init__(self, color, connected_to, wire_set):
        self.color = color
        self.connected_to = connected_to
        self.curr_color_instance = getattr(wire_set, color)

class WireSequences:
    # The lookup table to determine if the user should cut a wire based on its connection
    cut_table = {
        "red" : [["c"], ["b"], ["a"], ["a", "c"], ["b"], ["a", "c"], ["a", "b", "c"], ["a", "b"], ["b"]],
        "blue" : [["b"], ["a", "c"], ["b"], ["a"], ["b"], ["b", "c"], ["c"], ["a", "c"], ["a"]],
        "black" : [["a", "b", "c"], ["a", "c"], ["b"], ["a", "c"], ["b"], ["b", "c"], ["a", "b"], ["c"], ["c"]]
    }

    def start_wire_sequences(self):
        # Begins the process of starting a new wire sequence module
        wire_instance = WireSet() # Get a new module to start fresh

        print_and_wait("Ready to start. Please always enter wires from top to bottom!")

        # Go through each of the 4 rounds of wires
        for number in range (1, 5):
            print(f"Round {number}")
            self.input_wire_level(wire_instance)
        

    def input_wire_level(self, wire_set):
        # Asks user to input the entire level's wires. There's 4 `levels` per module
        number_of_wires = self.get_num_wires() # Ask the user how many wires there are

        # There are either 1, 2, or 3 wires per level
        if number_of_wires not in range(1,4):
            print_and_wait("Invalid number of wires. Please enter a number between 1 and 3.")
            self.input_wire_level(wire_set) # Ask them again!
        else:
            # For each wire, ask its color and connection
            for number in range(0, number_of_wires):
                wire_color = self.get_wire_color(number + 1)
                wire_connection = self.get_wire_connection(number + 1)
                curr_wire = Wire(wire_color, wire_connection, wire_set)

                # Prints if the wire should be cut or not based on 
                # color/connections/previous colors
                print_and_wait(self.get_wires_to_cut(curr_wire, wire_set))
                
                # Increment the count of the color that we saw
                wire_set.modify_wire_number(wire_color, 1)

    def get_num_wires(self):
        # Asks the user how many wires they see
        try:
            number_of_wires = int(input("How many wires are there? "))
            return number_of_wires
        except ValueError:
            # If they don't enter just a number, ask them again
            print_and_wait("Invalid number of wires. Please try again.")
            return self.get_num_wires()

    def get_wire_color(self, number):
        # Asks for the color of the wire
        valid_colors = ["red", "blue", "black"]
        color = input(f"What is the color of the {ordinalize(number)} wire? ").lower()

        if color not in valid_colors:
            print_and_wait("Invalid wire color. Wires are `red`, `blue`, or `black`. Try again.")
            return self.get_wire_color(number)
        else:
            return color

    def get_wire_connection(self, number):
        # Asks for the letter that the wire is connected to
        valid_connections = ["a", "b", "c"]
        connection = input(f"What is the {ordinalize(number)} wire connected to? ").lower()

        if connection not in valid_connections:
            print_and_wait("Invalid wire connection. Connections are `a`, `b`, or `c`. Try again.")
            return self.get_wire_connection(number)
        else:
            return connection

    def get_wires_to_cut(self, wire, wire_set):
        # Checks the lookup table and the number of wires of the color to see if
        # the wire should be cut
        curr_color_occurrences = getattr(wire_set, wire.color)
        if wire.connected_to in self.cut_table[wire.color][curr_color_occurrences]:
            return "Cut the wire."
        else:
            return "Don't cut the wire."