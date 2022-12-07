class CargoHold:
    def __init__(self, crate_stacks):
        self.all_stacks = []
        for each_stack in crate_stacks:
            self.all_stacks.append(each_stack)

    def __str__(self):
        top_items = ""
        for each_stack in self.all_stacks:
            top_items += each_stack.get_top_item()
        return top_items


class CrateStack:
    def __init__(self, stack_items):
        self.queue = []
        for each_item in stack_items:
            self.queue.append(each_item)

    def get_items_from_queue(self, num_items):
        items_to_return = []
        for _ in range(num_items):
            items_to_return.append(
                self.queue.pop()
            )
        return reversed(items_to_return)

    def add_items_to_queue(self, items_to_add):
        for each_item in items_to_add:
            self.queue.append(each_item)

    def get_top_item(self):
        return self.queue[len(self.queue) - 1]


    def __str__(self):
        return_string = ""
        for each_item in reversed(self.queue):
            return_string += "[" + each_item + "]\n"
        return return_string


one = CrateStack(['L', 'N', 'W', 'T', 'D'])
two = CrateStack(['C', 'P', 'H'])
three = CrateStack(['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J'])
four = CrateStack(['C', 'W', 'S', 'N', 'T', 'Q', 'L'])
five = CrateStack(['P', 'H', 'C', 'N'])
six = CrateStack(['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B'])
seven = CrateStack(['M', 'B', 'R', 'J', 'G', 'S', 'L'])
eight = CrateStack(['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T'])
nine = CrateStack(['W', 'G', 'D', 'N', 'P', 'L'])

cargo_hold = CargoHold(
    crate_stacks=[one, two, three, four, five, six, seven, eight, nine]
)


stack_mapping = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine
}

def parse_move_line(line):
    line = line.replace("move", "").replace("from", "").replace("to", "").split()
    amount_to_move = int(line[0])
    from_stack = int(line[1])
    to_stack = int(line[2])
    return amount_to_move, from_stack, to_stack


with open("input.txt", "r") as input_file:
    for move in input_file:
        move = move.strip()
        amount_to_move, from_stack, to_stack = parse_move_line(move)
        from_stack = stack_mapping.get(from_stack)
        to_stack = stack_mapping.get(to_stack)
        items = from_stack.get_items_from_queue(amount_to_move)
        to_stack.add_items_to_queue(items)

print(cargo_hold)