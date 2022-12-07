 
def calculate_range_values(value_range):
    range_split = value_range.split("-")
    value_list = []
    for i in range(int(range_split[0]), int(range_split[1]) + 1):
        value_list.append(i)
    return value_list

def is_any_pair_fully_contained(range_1, range_2):
    if set(range_1).issubset(set(range_2)) or set(range_2).issubset(set(range_1)):
        return True
    return False

def is_there_any_overlap(range1, range2):
    if set(range1).intersection(range2) or set(range2).intersection(range1):
        return True
    return False
 
if __name__ == "__main__":
    fully_connected_pairs = 0
    with open("input.txt", "r") as assignments:
        for assignment in assignments:
            assignment = assignment.strip()
            split_assignment = assignment.split(",")
            assignment_1 = split_assignment[0]
            assignment_2 = split_assignment[1]
            range_1 = calculate_range_values(assignment_1)
            range_2 = calculate_range_values(assignment_2)
            if is_there_any_overlap(range_1, range_2):
                fully_connected_pairs += 1
    print(fully_connected_pairs)
