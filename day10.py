from typing import List
from collections import deque


# Store global variables to use later
SIGNAL_STRENGTH = 0
X_REGISTER = 1
CRT = [
    ['x' for _ in range(40)] for x in range(6)
]

def crt_render(clock):
    """
    Part2: Takes a clock value and renders the display
    based on the position of the sprite (i.e. the X_REGISTER value)

    Calculate the column and row in the CRT that needs updating based on the
    the clock value then check if the X_REGISTER value falls in the column
    (it's 3px wide so we check left and right of the column)
    """
    global X_REGISTER, CRT
    column = clock if clock < 40 else clock % 40
    row = int(clock/40)
    if X_REGISTER -1 <= column <= X_REGISTER + 1:
        CRT[row][column] = '#'
    else:
        CRT[row][column]= '.'

def check_clock(clock_value: int):
    """
    Part 1: Read clock value and if it's a 
    point of interest, calculate the signal strength
    """
    global X_REGISTER, SIGNAL_STRENGTH
    checkpoints = [20]
    checkpoints += [x for x in range(60, 221, 40)]
    if clock_value in checkpoints:
        SIGNAL_STRENGTH += clock_value * X_REGISTER

def clock_signal(commands: deque):
    """
    The clock signal function ticks a clock 240 times and runs the commands
    based on that.

    Both parts use this function to do the calculations.
    For part2, we re-render the CRT every time the clock updates or when
    the register value changes
    """
    global X_REGISTER
    clock = 0
    while clock < 239:
        command = commands.popleft()
        if command == "noop":
            clock += 1
            # check_clock(clock_value=clock)
            crt_render(clock)
        elif command.startswith("addx"):
            split_command = command.split(" ")
            command = split_command[0]
            value = int(split_command[1])
            crt_render(clock)
            clock += 1
            # check_clock(clock_value=clock)
            crt_render(clock)
            clock += 1
            crt_render(clock)
            X_REGISTER += value
            crt_render(clock)
            # check_clock(clock_value=clock)


def read_input():
    commands = deque()
    with open("input.txt", "r") as input_file:
        for line in input_file:
            commands.append(line.strip())
    return commands

def print_crt():
    """
    Helper method to print CRT output to screen
    """
    global CRT
    for row in CRT:
        row = "".join(row)
        print(row)

if __name__ == "__main__":
    commands = read_input()
    clock_signal(commands)
    # Part 1
    # print(SIGNAL_STRENGTH)
    # for item in CRT:
    #     print(item)
    
    # Part 2
    print_crt()
    