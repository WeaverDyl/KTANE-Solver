from utility import print_and_wait

class Wire:
    # An individual wire within the complicated wires module
    def __init__(self, has_red_coloring, has_blue_coloring, has_star, led_on):
        self.has_red_coloring = has_red_coloring
        self.has_blue_coloring = has_blue_coloring
        self.has_star = has_star
        self.led_on = led_on

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class ComplicatedWires:
    # Used for answering questions about wires
    truthy = ["Yes", "yes", "y", "True", "true", "1"]
    falsy = ["No", "no", "n", "False", "false", "0"]

    def lookup(self, wire_obj):
        # Lookup according to manual: "c" => cut the wire, "d" => don't cut the wire
        # "s" => cut if last digit of serial is even, "p" => cut if bomb has parallel port
        # "b" => cut if bomb has two or more batteries
        complicated_lookup = {
            "c": [Wire(False, False, False, False), Wire(False, False, True, False),
                  Wire(True, False, True, False)],
            "d": [Wire(False, False, False, True), Wire(False, True, True, False), 
                  Wire(True, True, True, True)],
            "s": [Wire(True, False, False, False), Wire(False, True, False, False),
                  Wire(True, True, False, False), Wire(True, True, False, True)],
            "p": [Wire(True, True, True, False), Wire(False, True, False, True),
                  Wire(False, True, True, True)],
            "b": [Wire(False, False, True, True), Wire(True, False, True, True),
                  Wire(True, False, False, True)]
        }

        # Check the value of each key for the object. If it exists, return the key, else return None
        for key in complicated_lookup:
            for wire in complicated_lookup[key]:
                if wire == wire_obj:
                    return key
        return None

    
    def start_complicated_wires(self, bomb):
        # Solves the complicated wires module

        # Ask how many wires there are
        wire_count = self.ask_wire_count()
        # Go through process for each wire
        for wire in range(1, wire_count + 1):
            print(f"Wire {wire}:")
            # Get information for each wire
            has_red_coloring = self.ask_red_coloring()
            has_blue_coloring = self.ask_blue_coloring()
            has_star = self.ask_star()
            has_lit_led = self.ask_led()
            complete_wire = Wire(has_red_coloring, has_blue_coloring, has_star, has_lit_led)

            # Figure out what to do with the wire
            instruction = self.lookup(complete_wire)
            if instruction == "c":
                print_and_wait("Cut the wire.")
            elif instruction == "d":
                print_and_wait("Don't cut the wire.")
            elif instruction == "s":
                if bomb.last_serial_even():
                    print_and_wait("Cut the wire.")
                else:
                    print_and_wait("Don't cut the wire.")
            elif instruction == "p":
                if bomb.has_parallel_port():
                    print_and_wait("Cut the wire.")
                else:
                    print_and_wait("Don't cut the wire.")
            elif instruction == "b":
                if bomb.get_num_batteries() >= 2:
                    print_and_wait("Cut the wire.")
                else:
                    print_and_wait("Don't cut the wire.")

    def ask_red_coloring(self):
        # Asks the user if the wire has red coloring
        has_red_coloring = input("Does the wire have red coloring? ")
        if has_red_coloring in self.truthy:
            return True
        elif has_red_coloring in self.falsy:
            return False
        else:
            print_and_wait("Invalid answer. Please try again.")
            return self.ask_red_coloring()

    def ask_blue_coloring(self):
        # Asks the user if the wire has blue coloring
        has_blue_coloring = input("Does the wire have blue coloring? ")
        if has_blue_coloring in self.truthy:
            return True
        elif has_blue_coloring in self.falsy:
            return False
        else:
            print_and_wait("Invalid answer. Please try again.")
            return self.ask_blue_coloring()

    def ask_star(self):
        # Asks the user if the wire has a star
        has_star = input("Does the wire have a star? ")
        if has_star in self.truthy:
            return True
        elif has_star in self.falsy:
            return False
        else:
            print_and_wait("Invalid answer. Please try again.")
            return self.ask_star()

    def ask_led(self):
        # Asks the user if the wire has a lit LED
        has_led = input("Does the wire have a lit LED? ")
        if has_led in self.truthy:
            return True
        elif has_led in self.falsy:
            return False
        else:
            print_and_wait("Invalid answer. Please try again.")
            return self.ask_led()

    def ask_wire_count(self):
        # Asks the user how many wires are in the module
        try:
            wire_count = int(input("How many wires are there? "))
            # There can only be 1,2,3,4,5, or 6 wires
            if wire_count in range(1, 7):
                return wire_count
            else:
                raise ValueError("The wire count must be between 1 and 6 inclusive.")
        except ValueError:
            print_and_wait("Invalid wire count. Please try again")
            return self.ask_wire_count()
