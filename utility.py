def print_list(lst, per_line):
    # Prints a list where each line is `per_line` elements long
    line_start = line_end = 0
    while line_end < len(lst):
        line_end += per_line
        print(", ".join(lst[line_start:line_end]))
        line_start = line_end
    print()