class SimpleWires:
    def start_simple_wires(self, bomb):
        self.wires = input("Enter the first letter of the color of each wire. ").lower()

        # Check if the wires are valid, restarting the process if not
        if not self.check_valid_wires(self.wires):
            print("You've entered an invalid list!\n")
            self.start_simple_wires(bomb)

        # Runs the correct function based on the number of wires
        result = {
            3: self.three_wires(bomb, self.wires),
            4: self.four_wires(bomb, self.wires),
            5: self.five_wires(bomb, self.wires),
            6: self.six_wires(bomb, self.wires),
        }[len(self.wires)]

        print(result) # Prints which wire to cut
        return

    def check_valid_wires(self, wires):
        # Each wire module has 3, 4, 5, or 6 wires
        if len(wires) not in range(3, 7):
            return False
        for color in wires:
            # Wires are yellow, red, white, blue, or black (k = black)
            if color not in 'yrwbk':
                return False
        return True

    def three_wires(self, bomb, wires):
        if not 'r' in wires:
            return "Cut the second wire."
        if wires[-1] == 'w':
            return "Cut the last wire."
        if wires.count('b') > 1:
            return "Cut the last blue wire."
        else:
            return "Cut the last wire."

    def four_wires(self, bomb, wires):
        if wires.count('r') > 1 and bomb.serial_no[-1].isnumeric() and int(bomb.serial_no[-1]) % 2 == 1:
            return "Cut the last red wire."
        if wires[-1] == 'y' and wires.count('r') == 0:
            return "Cut the first wire."
        if wires.count('b') == 1:
            return "Cut the first wire."
        if wires.count('y') > 1:
            return "Cut the last wire."
        else:
            return "Cut the second wire."

    def five_wires(self, bomb, wires):
        if wires[-1] == 'k' and bomb.serial_no[-1].isnumeric() and int(bomb.serial_no[-1]) % 2 == 1:
            return "Cut the fourth wire."
        if wires.count('r') == 1 and wires.count('y') > 1:
            return "Cut the first wire."
        if wires.count('k') == 0:
            return "Cut the second wire."
        else:
            return "Cut the first wire."

    def six_wires(self, bomb, wires):
        if wires.count('y') == 0 and bomb.serial_no[-1].isnumeric() and int(bomb.serial_no[-1]) % 2 == 1:
            return "Cut the third wire."
        if wires.count('y') == 1 and wires.count('w') > 1:
            return "Cut the fourth wire."
        if wires.count('r') == 0:
            return "Cut the last wire."
        else:
            return "Cut the fourth wire."
