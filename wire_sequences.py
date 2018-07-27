from inflection import ordinalize
from utility import print_and_wait

class WireSet:
    # Contains the current count of each color wire that has been seen
    def __init__(self, red=0, blue=0, black=0):
        self.red = red
        self.blue = blue
        self.black = black

    def modify_wire_number(self, color, modifier):
        #
        current_count = getattr(self, color)
        setattr(self, color, current_count + modifier)

class Wire:
    def __init__(self, color, connected_to, wire_set):
        self.color = color
        self.connected_to = connected_to
        self.curr_color_instance = getattr(wire_set, color)

class WireSequences:
    #
    cut_table = {
        "red" : [["c"], ["b"], ["a"], ["a", "c"], ["b"], ["a", "c"], ["a", "b", "c"], ["a", "b"], ["b"]],
        "blue" : [["b"], ["a", "c"], ["b"], ["a"], ["b"], ["b", "c"], ["c"], ["a", "c"], ["a"]],
        "black" : [["a", "b", "c"], ["a", "c"], ["b"], ["a", "c"], ["b"], ["b", "c"], ["a", "b"], ["c"], ["c"]]
    }

    def start_wire_sequences(self):
        wire_instance = WireSet()

        for _ in range (0, 4):
            self.input_wire_level(wire_instance)
        

    def input_wire_level(self, wire_set):
        number_of_wires = int(input("How many wires are there? "))

        if number_of_wires not in range(1,4):
            print_and_wait("Invalid number of wires. Please try again.")
            self.input_wire_level(wire_set)
        else:
            for i in range(0, number_of_wires):
                wire_color = input(f"What is the color of the {ordinalize(i + 1)} wire? ")
                wire_connection = input(f"What is the {ordinalize(i + 1)} wire connected to? ")
                curr_wire = Wire(wire_color, wire_connection, wire_set)

                print_and_wait(self.get_wires_to_cut(curr_wire, wire_set))
                
                wire_set.modify_wire_number(wire_color, 1)



    def get_wires_to_cut(self, wire, wire_set):
        curr_color_occurrences = getattr(wire_set, wire.color)
        if wire.connected_to in self.cut_table[wire.color][curr_color_occurrences]:
            return "CUT THE WIRE"
        else:
            return "DONT CUT THE WIRE"