from utility import print_and_wait

class Bomb:
    def __init__(self):
        bomb_data = self.collect_info()

        self.serial_no = bomb_data[0] # The serial number on the bomb
        self.num_batteries = bomb_data[1] # The number of batteries contained in the bomb
        self.lit_indicators = bomb_data[2] # A list of all lit indicators on the bomb
        self.ports = bomb_data[3] # All of the ports on the bomb

    def collect_info(self):
        serial_no = self.enter_serial()
        batteries = self.enter_batteries()
        indicators = self.enter_indicators()
        ports = self.enter_ports()

        return serial_no, batteries, indicators, ports

    def enter_serial(self):
        # Asks user for serial number of the bomb
        serial_length = 6
        serial_no = input("What's the serial number on the bomb? ").strip()

        if len(serial_no) != serial_length:
            print_and_wait("Invalid serial number. Please re-enter the serial number.")
            return self.enter_serial()
        else:
            return serial_no

    def last_serial_even(self):
        # Returns True if the last digit of the serial number is even, False otherwise
        try:
            if int(self.serial_no[-1]) % 2 == 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def vowel_in_serial(self):
        for letter in self.serial_no:
            if letter.lower() in "aeiou":
                return True
        return False

    def enter_batteries(self):
        # Asks user how many batteries there are on the bomb
        try:
            num_batteries = int(input("How many batteries are there on the bomb? "))
            return num_batteries
        except ValueError:
            print_and_wait("Invalid number of batteries. Please try again.")
            return self.enter_batteries()

    def get_num_batteries(self):
        # Returns the number of batteries in the bomb
        return self.num_batteries

    def enter_indicators(self):
        # Asks user for lit indicators
        valid_indicators = ["SND", "CLR", "CAR", "IND", "FRQ", "SIG", "NSA", "MSA", "TRN", "BOB", "FRK"]
        indicators = [ind.upper() for ind in input("Enter all lit indicators on the bomb, each seperated by a space: ").strip().split()]

        # Check if user input contains only valid indicators
        for indicator in indicators:
            if indicator.upper() not in valid_indicators:
                print_and_wait("Invalid indicators. Please re-enter the indicators.")
                return self.enter_indicators()
        return indicators
    
    def enter_ports(self):
        # Asks user for the ports on the bomb
        valid_ports = ["dvi-d", "parallel", "ps/2", "rj-45", "serial", "stereo rca"]
        ports = [port.upper() for port in input("Enter all ports on the bomb, seperated by a space: ").strip().split()]

        # Check that all ports entered are valid
        for port in ports:
            if port.lower() not in valid_ports:
                print_and_wait("Invalid port entered. Please re-enter the ports.")
                return self.enter_ports()
        return ports

    def has_parallel_port(self):
        for port in self.ports:
            if port.lower() == "parallel":
                return True
        return False

    def ask_strikes(self):
        # Gets the number of strikes from the user, which affects the solution
        try:
            num_strikes = input("How many strikes does the bomb have right now? ")
            if int(num_strikes) not in range(0, 3):
                raise ValueError("The bomb can only have 0, 1, or 2 strikes before exploding.")
            else:
                return int(num_strikes)
        except ValueError:
            print_and_wait("Invalid number of strikes. Please try again")
            return self.ask_strikes()