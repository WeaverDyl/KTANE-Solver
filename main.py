from bomb import Bomb
from simple_wires import SimpleWires

def main():
    bomb = Bomb() # Create a new bomb instance, which stores indicator/battery/other info

    # Pick a module
    while True:
        curr_module = input("What module would you like to solve? Your options are:\n\n"\
                            "Simple Wires\n\n")

        if curr_module.lower() == 'simple wires':
            simple_wires = SimpleWires()
            simple_wires.start_simple_wires(bomb)

if __name__ == "__main__":
    main() # Begin!