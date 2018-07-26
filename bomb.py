class Bomb:
    def __init__(self):
        bomb_data = self.collect_info()

        self.serial_no = bomb_data[0] # The serial number on the bomb
        self.batteries = bomb_data[1] # The number of batteries contained in the bomb
        self.indicators = bomb_data[2] # A list of all lit indicators on the bomb
        self.ports = bomb_data[3] # All of the ports on the bomb
        self.strikes = 0 # The number of strikes can affect diffusal

    def collect_info(self):
        serial_no = input("What's the serial number on the bomb? ")
        batteries = input("How many batteries are there on the bomb? ")
        indicators = [i.strip() for i in input("Enter a comma-seperated list of lit indicators on the bomb. ").split(',')]
        ports = [i.strip() for i in input("Enter a comma-seperated list of ports on the bomb. ").split(',')]

        return serial_no, batteries, indicators, ports