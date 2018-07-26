from inflection import ordinalize

class Stager:
    def __init__(self, specific_stage_position=0, generic_position=0, specific_stage_label=0, specific_label=0):
        self.specific_stage_position = specific_stage_position
        self.generic_position = generic_position
        self.specific_stage_label = specific_stage_label
        self.specific_label = specific_label

class Memory:

    memory = {
        # Position, Value
        1 : [None, None],
        2 : [None, None],
        3 : [None, None],
        4 : [None, None],
        5 : [None, None]
    }

    def start_memory(self, bomb):
        # Goes through each stage, solving the module for the user
        for curr_stage in range (1, 6):
            display = self.get_display()
            self.handle_stages(curr_stage, display)

    def handle_stages(self, curr_stage, display):
        # Tells the user what to do based on the current stage
        curr_instruction = None

        if curr_stage == 1:
            if display == 1: curr_instruction = Stager(0, 2, 0, 0)
            elif display == 2: curr_instruction = Stager(0, 2, 0, 0)
            elif display == 3: curr_instruction = Stager(0, 3, 0, 0)
            elif display == 4: curr_instruction = Stager(0, 4, 0, 0)

        elif curr_stage == 2:
            if display == 1: curr_instruction = Stager(0, 0, 0, 4)
            elif display == 2: curr_instruction = Stager(self.get_info_from_stage(1)[0], 0, 0, 0)
            elif display == 3: curr_instruction = Stager(0, 1, 0, 0)
            elif display == 4: curr_instruction = Stager(self.get_info_from_stage(1)[0], 0, 0, 0)

        elif curr_stage == 3:
            if display == 1: curr_instruction = Stager(0, 0, self.get_info_from_stage(2)[1], 0)
            elif display == 2: curr_instruction = Stager(0, 0, self.get_info_from_stage(1)[1], 0)
            elif display == 3: curr_instruction = Stager(0, 3, 0, 0)
            elif display == 4: curr_instruction = Stager(0, 0, 0, 4)

        elif curr_stage == 4:
            if display == 1: curr_instruction = Stager(self.get_info_from_stage(1)[0], 0, 0)
            elif display == 2: curr_instruction = Stager(0, 1, 0, 0)
            elif display == 3: curr_instruction = Stager(self.get_info_from_stage(2)[0], 0, 0, 0)
            elif display == 4: curr_instruction = Stager(self.get_info_from_stage(2)[0], 0, 0, 0)

        elif curr_stage == 5:
            if display == 1: curr_instruction = Stager(0, 0, self.get_info_from_stage(1)[1], 0)
            elif display == 2: curr_instruction = Stager(0, 0, self.get_info_from_stage(2)[1], 0)
            elif display == 3: curr_instruction = Stager(0, 0, self.get_info_from_stage(4)[1], 0)
            elif display == 4: curr_instruction = Stager(0, 0, self.get_info_from_stage(3)[1], 0)

        # Process curr_instruction to give directions
        self.process_stage(curr_instruction)

        # Get the position of the button pressed
        if curr_instruction.generic_position:
            button_position = curr_instruction.generic_position
        elif curr_instruction.specific_stage_position:
            button_position = curr_instruction.specific_stage_position
        elif curr_instruction.specific_stage_label:
            button_position = curr_instruction.specific_stage_label
        else:
            button_position = self.ask_position(curr_stage)
        # Get the value of the button pressed
        button_label = self.ask_button_label(curr_stage)
        
        self.memory[curr_stage][0] = button_position
        self.memory[curr_stage][1] = button_label

    def get_display(self):
        # Asks for the current number on the display
        valid_response = ["1", "2", "3", "4"]
        display = input("\nWhat is the number on the display? ")
        
        if display in valid_response:
            return int(display)
        else:
            print("An error occurred, please check your input.")
            return self.get_display()

    def ask_position(self, curr_stage):
        # Asks for the button position that the user pressed
        valid_positions = ["1", "2", "3", "4"]
        position = input("What was the position of the button you pressed? ")

        if position in valid_positions:
            return int(position)
        else:
            print("That's an invalid position.")
            return self.ask_position(curr_stage)

    def get_info_from_stage(self, stage):
        return [self.memory[stage][0], self.memory[stage][1]]

    def ask_button_label(self, curr_stage):
        # Asks for the button position that the user pressed
        valid_button_labels = ["1", "2", "3", "4"]
        label = input("What was the value of the button you pressed? ")

        if label in valid_button_labels:
            return int(label)
        else:
            print("That's an invalid label.")
            return self.ask_button_label(curr_stage)

    def process_stage(self, curr_instruction):
        if curr_instruction.specific_stage_position:
            print(f"Press the button in the {ordinalize(curr_instruction.specific_stage_position)} position.")
        elif curr_instruction.generic_position:
            print(f"Press the button in the {ordinalize(curr_instruction.generic_position)} position.")
        elif curr_instruction.specific_stage_label:
            print(f"Press the button labeled `{curr_instruction.specific_stage_label}`.")
        else:
            print(f"Press the button labeled `{curr_instruction.specific_label}`.")
        