from bomb import Bomb
from simple_wires import SimpleWires
from morse_code import MorseCode
from passwords import Passwords
from whos_on_first import WhosOnFirst
from memory import Memory
from keypads import Keypads

def main():
    bomb = Bomb() # Create a new bomb instance, which stores indicator/battery/other info

    # Pick a module
    while True:
        curr_module = input("What module would you like to solve? Your options are:\n\n"\
                            "Simple Wires / Morse Code / Passwords / Who's on First\n"\
                            "Memory / Keypads\n\n")

        if curr_module.lower() == 'simple wires':
            simple_wires = SimpleWires()
            simple_wires.start_simple_wires(bomb)
            
        if curr_module.lower() == 'morse code':
            morse_code = MorseCode()
            morse_code.start_morse_code(bomb)
            
        if curr_module.lower() == 'passwords':
            passwords = Passwords()
            passwords.start_passwords(bomb)

        if curr_module.lower() == 'who\'s on first':
            whos_on_first = WhosOnFirst()
            whos_on_first.start_whos_on_first(bomb, 0)

        if curr_module.lower() == 'memory':
            memory = Memory()
            memory.start_memory(bomb)

        if curr_module.lower() == 'keypads':
            keypads = Keypads()
            keypads.start_keypads()

if __name__ == "__main__":
    main() # Begin!