from utility import print_and_wait

class Maze:
    def start_maze(self):
        # Start solving the module
        print("The top left corner is `0, 0`. The top right corner is `5, 0")
        # Collect information
        indicator_pos = self.get_indicator_pos()
        user_pos = self.get_user_pos()
        goal_pos = self.get_goal_pos()
        maze = self.determine_maze(indicator_pos)

        # Solve the maze
        moves = self.solve_maze(indicator_pos, user_pos, goal_pos, maze)
        print("Solution:")
        for move in moves:
            print(move, end=", ")
        print_and_wait("Done.")

    def get_indicator_pos(self):
        # Gets an indicator position from the user
        valid_indicators = [(0, 1), (5, 2), (4, 1), (1, 3), (3, 3), (5, 3), 
                            (0, 0), (0, 3), (4, 2), (3, 5), (4, 0), (2, 4),
                            (1, 0), (1, 5), (3, 0), (2, 3), (1, 2), (0, 4)]
        try:
            # Get the position of one of the indicators
            indicator_posx = int(input("Enter the X position of one of the indicators: "))
            indicator_posy = int(input("Enter the Y position of one of the indicators: "))
            
            if (indicator_posx, indicator_posy) in valid_indicators:
                return (indicator_posx, indicator_posy)
            else:
                print_and_wait("Invalid indicator position. Please try again.")
                return self.get_indicator_pos()
        except ValueError:
                print_and_wait("Invalid indicator position. Please try again.")
                return self.get_indicator_pos()

    def get_user_pos(self):
        # Get the starting position of the user
        try:
            user_posx = int(input("What is your X position? "))
            user_posy = int(input("What is your Y position? "))

            if user_posx in range(0, 6) and user_posy in range(0, 6):
                return (user_posx, user_posy)
            else:
                print_and_wait("Invalid coordinates. Please try again.")
                return self.get_user_pos()
        except ValueError:
                print_and_wait("Invalid coordinates. Please try again.")
                return self.get_user_pos()

    def get_goal_pos(self):
        # Get the position of the goal (red triangle)
        try:
            goal_posx = int(input("What is the goal's X position? "))
            goal_posy = int(input("What is the goal's Y position? "))

            if goal_posx in range(0, 6) and goal_posy in range(0, 6):
                return (goal_posx, goal_posy)
            else:
                print_and_wait("Invalid coordinates. Please try again.")
                return self.get_goal_pos()
        except ValueError:
            print_and_wait("Invalid coordinates. Please try again.")
            return self.get_goal_pos()

    def solve_maze(self, indicator_pos, user_pos, goal_pos, maze):
        # Solve the maze, returning the directions
        # From https://github.com/masasin/keep_talking_solver
        visited = []
        branches = []
        moves = []
        i, j = user_pos
        while (i, j) != goal_pos:
            visited.append((i, j))
            moves.append((i, j))
            val = maze[j][i]
            n_possible = len(val)
            if "u" in val and (i, j - 1) in visited:
                n_possible -= 1 
            if "d" in val and (i, j + 1) in visited:
                n_possible -= 1
            if "l" in val and (i - 1, j) in visited:
                n_possible -= 1
            if "r" in val and (i + 1, j) in visited:
                n_possible -= 1

            if n_possible > 1:
                branches.append((i, j))

            if "u" in val and (i, j - 1) not in visited:
                j -= 1
            elif "d" in val and (i, j + 1) not in visited:
                j += 1
            elif "l" in val and (i - 1, j) not in visited:
                i -= 1
            elif "r" in val and (i + 1, j) not in visited:
                i += 1
            else:
                i, j = branches.pop()
                moves = moves[:moves.index((i, j))]

        moves.append(goal_pos)
        instructions = []
        for current, move in zip(moves, moves[1:]):
            if move[1] < current[1]:
                instructions.append("up")
            elif move[1] > current[1]:
                instructions.append("down")
            elif move[0] < current[0]:
                instructions.append("left")
            else:
                instructions.append("right")
        return instructions

    def determine_maze(self, indicator):
        # Using one of the white indicators, determines the
        # maze that the user has. Returns none if the indicator
        # doesn't match any coordinates.
        if indicator in [(0, 1), (5, 2)]:
            maze = [
                ["rd", "lr", "ld", "rd", "lr", "l"],
                ["ud", "rd", "ul", "ur", "lr", "ld"],
                ["ud", "ur", "ld", "rd", "lr", "uld"],
                ["ud", "r", "ulr", "lu", "r", "uld"],
                ["urd", "lr", "ld", "rd", "l", "ud"],
                ["ur", "l", "ur", "ul", "r", "ul"]
            ]
        elif indicator in [(4, 1), (1, 3)]:
            maze = [
                ["r", "lrd", "l", "rd", "lrd", "l"],
                ["rd", "ul", "rd", "ul", "ur", "ld"],
                ["ud", "rd", "ul", "rd", "lr", "uld"],
                ["urd", "ul", "rd", "ul", "d", "ud"],
                ["ud", "d", "ud", "rd", "ul", "ud"],
                ["u", "ur", "ul", "ur", "lr", "lu"]
            ]
        elif indicator in [(3, 3), (5, 3)]:
            maze = [
                ["dr", "lr", "ld", "d", "dr", "dl"],
                ["u", "d", "ud", "ur", "lu", "ud"],
                ["dr", "uld", "ud", "rd", "ld", "ud"],
                ["ud", "ud", "ud", "ud", "ud", "ud"],
                ["ud", "ur", "ul", "ud", "ud", "ud"],
                ["ur", "lr", "lr", "ul", "ur", "ul"]
            ]
        elif indicator in [(0, 0), (0, 3)]:
            maze = [
                ["rd", "ld", "r", "lr", "lr", "ld"],
                ["ud", "ud", "dr", "lr", "lr", "uld"],
                ["ud", "ur", "lu", "rd", "l", "ud"],
                ["ud", "r", "lr", "lru", "lr", "lud"],
                ["udr", "lr", "lr", "lr", "ld", "ud"],
                ["ur", "lr", "l", "r", "ul", "u"]
            ]
        elif indicator in [(4, 2), (3, 5)]:
            maze = [
                ["r", "lr", "lr", "lr", "lrd", "ld"],
                ["rd", "lr", "lr", "lrd", "lu", "u"],
                ["udr", "ld", "r", "ul", "rd", "ld"],
                ["ud", "ur", "lr", "ld", "u", "ud"],
                ["ud", "rd", "lr", "ulr", "l", "ud"],
                ["u", "ur", "lr", "lr", "lr", "lu"]
            ]
        elif indicator in [(4, 0), (2, 4)]:
            maze = [
                ["d", "dr", "ld", "r", "ldr", "ld"],
                ["ud", "ud", "ud", "rd", "ul", "ud"],
                ["udr", "ul", "u", "ud", "rd", "ul"],
                ["ur", "ld", "dr", "udl", "ud", "d"],
                ["rd", "ul", "u", "ud", "ur", "uld"],
                ["ur", "lr", "lr", "ul", "r", "ul"]
            ]
        elif indicator in [(1, 0), (1, 5)]:
            maze = [
                ["dr", "lr", "lr", "ld", "dr", "ld"],
                ["ud", "rd", "l", "ur", "lu", "ud"],
                ["ur", "ul", "rd", "l", "rd", "ul"],
                ["dr", "ld", "udr", "lr", "ul", "d"],
                ["ud", "u", "ur", "lr", "ld", "ud"],
                ["ur", "lr", "lr", "lr", "ulr", "ul"]
            ]
        elif indicator in [(3, 0), (2, 3)]:
            maze = [
                ["d", "dr", "lr", "ld", "dr", "ld"],
                ["udr", "ulr", "l", "ur", "ul", "ud"],
                ["ud", "dr", "lr", "lr", "ld", "ud"],
                ["ud", "ur", "ld", "r", "ulr", "ul"],
                ["ud", "d", "ur", "lr", "lr", "l"],
                ["ur", "ulr", "lr", "lr", "lr", "l"]
            ]
        elif indicator in [(1, 2), (0, 4)]:
            maze = [
                ["d", "dr", "lr", "lr", "ldr", "ld"],
                ["ud", "ud", "rd", "l", "ud", "ud"],
                ["udr", "ulr", "ul", "rd", "ul", "ud"],
                ["ud", "d", "dr", "ul", "r", "uld"],
                ["ud", "ud", "ud", "dr", "dl", "u"],
                ["ur", "ul", "ur", "ul", "ur", "l"]
            ]
        if maze is None:
            print_and_wait("Unexpected error, maze not found. Restarting module")
            self.start_maze()
        else:
            return maze