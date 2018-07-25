def check_valid_wires(wires):
    if len(wires) not in range(3, 7):
        return False
    for color in wires:
        if color not in 'yrwbk':
            return False
    return True

def cut_wire(serial_no):
    wires = input("Enter the first letter of the color of each wire. ").lower()

    if not check_valid_wires(wires):
        print("You've entered an invalid list!\n")
        cut_wire(serial_no)

    if len(wires) == 3:
        if not 'r' in wires:
            return "Cut the second wire."
        if wires[-1] == 'w':
            return "Cut the last wire."
        if wires.count('b') > 1:
            return "Cut the last blue wire."
        else:
            return "Cut the last wire."
    if len(wires) == 4:
        if wires.count('r') > 1 and serial_no[-1].isnumeric() and int(serial_no[-1]) % 2 == 1:
            return "Cut the last red wire."
        if wires[-1] == 'y' and wires.count('r') == 0:
            return "Cut the first wire."
        if wires.count('b') == 1:
            return "Cut the first wire."
        if wires.count('y') > 1:
            return "Cut the last wire."
        else:
            return "Cut the second wire."
    if len(wires) == 5:
        if wires[-1] == 'k' and serial_no[-1].isnumeric() and int(serial_no[-1]) % 2 == 1:
            return "Cut the fourth wire."
        if wires.count('r') == 1 and wires.count('y') > 1:
            return "Cut the first wire."
        if wires.count('k') == 0:
            return "Cut the second wire."
        else:
            return "Cut the first wire."
    if len(wires) == 6:
        if wires.count('y') == 0 and serial_no[-1].isnumeric() and int(serial_no[-1]) % 2 == 1:
            return "Cut the third wire."
        if wires.count('y') == 1 and wires.count('w') > 1:
            return "Cut the fourth wire."
        if wires.count('r') == 0:
            return "Cut the last wire."
        else:
            return "Cut the fourth wire."

if __name__ == "__main__":
    print(cut_wire('GJ1RB3'))