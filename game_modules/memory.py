class Memory:
    memory = {
        1 : None,
        2 : None,
        3 : None,
        4 : None,
        5 : None
    }

    def start_memory(self, bomb):
        # Goes through each stage, solving the module for the user
        for curr_stage in range (1, 6):
            display = self.get_display()

            self.handle_stages(curr_stage, display)

    def get_display(self):
        # Asks for the current number on the display
        valid_response = [1, 2, 3, 4]
        display = int(input("\nWhat is the number on the display? "))
        
        if display in valid_response:
            return int(display)
        else:
            print("An error occurred, please check your input.")
            self.get_display()

    def handle_stages(self, curr_stage, display):
        # Tells the user what to do based on the current stage

        # TODO reimplement better
        # Ex. When telling user to push button in position x, don't need to ask
        # for position, we already know it. implement so this can be used
        if curr_stage == 1:
            if display == 1: print("Press the button in the second position.")
            elif display == 2: print("Press the button in the second position.")
            elif display == 3: print("Press the button in the third position.")
            elif display == 4: print("Press the button in the fourth position.")

        elif curr_stage == 2:
            if display == 1: print("Press the button labeled `4`.")
            elif display == 2: print(f"Press the button in position {self.memory[1]}.")
            elif display == 3: print("Press the button in the first position.")
            elif display == 4: print(f"Press the button in position {self.memory[1]}.")

        elif curr_stage == 3:
            if display == 1: print(f"Press the button in position {self.memory[2]}.")
            elif display == 2: print(f"Press the button in position {self.memory[1]}.")
            elif display == 3: print("Press the button in the third position.")
            elif display == 4: print("Press the button labeled `4`.")

        elif curr_stage == 4:
            if display == 1: print(f"Press the button in position {self.memory[1]}.")
            elif display == 2: print("Press the button in the first position.")
            elif display == 3: print(f"Press the button in position {self.memory[2]}.")
            elif display == 4: print(f"Press the button in position {self.memory[2]}.")

        elif curr_stage == 5:
            if display == 1: print(f"Press the button in position {self.memory[1]}.")
            elif display == 2: print(f"Press the button in position {self.memory[2]}.")
            elif display == 3: print(f"Press the button in position {self.memory[4]}.")
            elif display == 4: print(f"Press the button in position {self.memory[3]}.")

        # Stores the position of the button that the user pressed for each stage
        position = self.ask_position(curr_stage)
        self.memory[curr_stage] = position

    def ask_position(self, curr_stage):
        # Asks for the button position that the user pressed
        valid_positions = [1, 2, 3, 4]
        position = int(input("What was the position of the button you pressed? "))

        if position in valid_positions:
            return position
        else:
            print("That's an invalid position.")
            self.ask_position(curr_stage)