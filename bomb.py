from utility import print_and_wait

class Bomb:
    def __init__(self):
        bomb_data = self.collect_info()

        self.serial_no = bomb_data[0] # The serial number on the bomb
        self.num_batteries = bomb_data[1] # The number of batteries contained in the bomb
        self.lit_indicators = bomb_data[2] # A list of all lit indicators on the bomb
        self.ports = bomb_data[3] # All of the ports on the bomb
        self.strikes = 0 # The number of strikes can affect diffusal

    def collect_info(self):
        serial_no = self.enter_serial()
        batteries = self.enter_batteries()
        indicators = self.enter_indicators()
        ports = [i.strip() for i in input("Enter a comma-seperated list of ports on the bomb: ").split(',')]

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

    def enter_batteries(self):
        # Asks user how many batteries there are on the bomb
        try:
            num_batteries = int(input("How many batteries are there on the bomb? "))
            return num_batteries
        except ValueError:
            print_and_wait("Invalid number of batteries. Please try again.")
            return self.enter_batteries()

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
        pass

    def set_strikes(self, num_strikes):
        self.strikes = num_strikes