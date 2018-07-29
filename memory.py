from inflection import ordinalize
from utility import print_and_wait

class Stager:
    # Used to handle which button should be pressed
    def __init__(self, specific_stage_position=None, generic_position=None, specific_stage_label=None, specific_label=None):
        self.specific_stage_position = specific_stage_position # "Press button in same position as in stage _"
        self.generic_position = generic_position # "Push button in _ position"
        self.specific_stage_label = specific_stage_label # "Push button with same label as in stage _"
        self.specific_label = specific_label # "Push button labelled _"

class Memory:
    # Runs the actual memory module solver

    # Stores the position and value of the button pressed at each stage
    memory = {
        # Position, Value
        1: [None, None],
        2: [None, None],
        3: [None, None],
        4: [None, None],
        5: [None, None]
    }

    def start_memory(self, bomb):
        # Goes through each stage, solving the module for the user
        for curr_stage in range (1, 6):
            print(f"\nRound {curr_stage}")
            display = self.get_display()
            self.handle_stages(curr_stage, display)

    def handle_stages(self, curr_stage, display):
        # Tells the user what to do based on the current stage
        curr_instruction = None

        if curr_stage == 1:
            if display == 1: curr_instruction = Stager(generic_position=2)
            elif display == 2: curr_instruction = Stager(generic_position=2)
            elif display == 3: curr_instruction = Stager(generic_position=3)
            elif display == 4: curr_instruction = Stager(generic_position=4)

        elif curr_stage == 2:
            if display == 1: curr_instruction = Stager(specific_label=4)
            elif display == 2: curr_instruction = Stager(specific_stage_position=self.get_info_from_stage(1)[0])
            elif display == 3: curr_instruction = Stager(generic_position=1)
            elif display == 4: curr_instruction = Stager(specific_stage_position=self.get_info_from_stage(1)[0])

        elif curr_stage == 3:
            if display == 1: curr_instruction = Stager(specific_stage_label=self.get_info_from_stage(2)[1])
            elif display == 2: curr_instruction = Stager(specific_stage_label=self.get_info_from_stage(1)[1])
            elif display == 3: curr_instruction = Stager(generic_position=3)
            elif display == 4: curr_instruction = Stager(specific_label=4)

        elif curr_stage == 4:
            if display == 1: curr_instruction = Stager(specific_stage_position=self.get_info_from_stage(1)[0])
            elif display == 2: curr_instruction = Stager(generic_position=1)
            elif display == 3: curr_instruction = Stager(specific_stage_position=self.get_info_from_stage(2)[0])
            elif display == 4: curr_instruction = Stager(specific_stage_position=self.get_info_from_stage(2)[0])

        elif curr_stage == 5:
            if display == 1: curr_instruction = Stager(specific_stage_label=self.get_info_from_stage(1)[1])
            elif display == 2: curr_instruction = Stager(specific_stage_label=self.get_info_from_stage(2)[1])
            elif display == 3: curr_instruction = Stager(specific_stage_label=self.get_info_from_stage(4)[1])
            elif display == 4: curr_instruction = Stager(specific_stage_label=self.get_info_from_stage(3)[1])

        # Process curr_instruction to give directions
        self.print_result(curr_instruction)

        # Collect position and value information for the first 4 stages
        if curr_stage != 5:
            # Get the position of the button pressed
            if curr_instruction.generic_position:
                button_position = curr_instruction.generic_position
            elif curr_instruction.specific_stage_position:
                button_position = curr_instruction.specific_stage_position
            else:
                button_position = self.ask_position(curr_stage)
            
            # Get the value of the button pressed
            if curr_instruction.specific_label:
                button_label = curr_instruction.specific_stage_label
            elif curr_instruction.specific_stage_label:
                button_label = curr_instruction.specific_stage_label
            else:
                button_label = self.ask_button_label(curr_stage)
            
            # Store the current stage's position and label
            self.memory[curr_stage][0] = button_position
            self.memory[curr_stage][1] = button_label

    def get_display(self):
        # Asks for the current number on the display
        valid_response = ["1", "2", "3", "4"]
        display = input("What is the number on the display? ")
        
        if display in valid_response:
            return int(display)
        else:
            print_and_wait("An error occurred, please check your input.")
            return self.get_display()

    def ask_position(self, curr_stage):
        # Asks for the button position that the user pressed
        valid_positions = ["1", "2", "3", "4"]
        position = input("What was the position of the button you pressed? ")

        if position in valid_positions:
            return int(position)
        else:
            print_and_wait("That's an invalid position.")
            return self.ask_position(curr_stage)

    def get_info_from_stage(self, stage):
        # Returns [position, value] of the button that the user presses for a stage
        return [self.memory[stage][0], self.memory[stage][1]]

    def ask_button_label(self, curr_stage):
        # Asks for the button position that the user pressed
        valid_button_labels = ["1", "2", "3", "4"]
        label = input("What was the value of the button you pressed? ")

        if label in valid_button_labels:
            return int(label)
        else:
            print_and_wait("That's an invalid label.")
            return self.ask_button_label(curr_stage)

    def print_result(self, curr_instruction):
        # Based on the instruction, print the correct directions
        if curr_instruction.specific_stage_position:
            print(f"Press the button in the {ordinalize(curr_instruction.specific_stage_position)} position.")
        elif curr_instruction.generic_position:
            print(f"Press the button in the {ordinalize(curr_instruction.generic_position)} position.")
        elif curr_instruction.specific_stage_label:
            print(f"Press the button labeled `{curr_instruction.specific_stage_label}`.")
        else:
            print(f"Press the button labeled `{curr_instruction.specific_label}`.")
        