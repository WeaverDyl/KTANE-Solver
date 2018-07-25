from constants import collect_info
from simple_wires import start_simple_wires

if __name__ == "__main__":
    bomb_info = collect_info()

    while True:
        curr_module = input("What module would you like to solve? Your options are:\n\n"\
                            "Simple Wires\n\n")
        if curr_module.lower() == 'simple wires':
            print(start_simple_wires(bomb_info))