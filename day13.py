from pprint import pprint
from enum import Enum
import itertools
from typing import List
from collections import UserList
from functools import total_ordering


class Result(Enum):
    RIGHT = "right"
    WRONG = "wrong"
    CONTINUE = "continue"


def compare_ints(left_item, right_item):
    if left_item == right_item:
        return Result.CONTINUE
    elif left_item < right_item:
        return Result.RIGHT
    elif left_item > right_item:
        return Result.WRONG


def compare_lists(left: List, right: List):
    """
    Compare 2 lists - we use itertools zip_longest to pad the shortest
    elements with zeros. We then iterate the lists and recursively call
    is_packets_in_right_order to get a Result object
    """
    for left_item, right_item in itertools.zip_longest(left, right):
        if left_item is None:
            return Result.RIGHT
        elif right_item is None:
            return Result.WRONG
        result = is_packets_in_right_order(left_item, right_item)
        if result == Result.CONTINUE:
            continue
        else:
            return result
    return Result.CONTINUE


def compare_mix(left, right):
    """
    Compare items where one of them is a list and the other is an int
    """
    if isinstance(left, int):
        return compare_lists([left], right)
    elif isinstance(right, int):
        return compare_lists(left, [right])
    

def is_packets_in_right_order(left: List, right: List):
    """
    Perform checks on the left and right packets and returns
    a Result based on their ordering.
    """
    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)
    elif isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)
    else:
        return compare_mix(left, right)


@total_ordering
class Signal(UserList):
    """
    Custom class that inherits from UserList to provide some useful functionality,
    specifically, we implement __eq__ to check for the indices of items

    We also implement __lt__ so we can sort Signals in the correct order.
    """
    def __eq__(self, other_list):
        return self.data == other_list.data

    def __lt__(self, other_list):
        return is_packets_in_right_order(self.data, other_list.data) == Result.RIGHT

    def __str__(self):
        print(self.data)


def analyze_all_packets(all_packets_received):
    """
    Part 2

    Take all the packets (lines of input) received and make them into one list.
    We can then use our custom class to sort this list based on the compare methods
    we did in part 1
    """
    signals = list(map(Signal, itertools.chain.from_iterable(all_packets_received)))
    divider1 = Signal([[2]])
    divider2 = Signal([[6]])
    signals.extend([divider1, divider2])
    signals.sort()
    decoder_key = (signals.index(divider1) + 1) * (signals.index(divider2) + 1)
    print(f"Part 2: {decoder_key}")


def read_input():
    packet_pairs = {}
    with open("input.txt", 'r') as input_file:
        curr_index = 1
        for line in input_file:
            if line == "\n":
                curr_index += 1
                continue
            else:
                line = eval(line.strip())
                if not packet_pairs.get(curr_index):
                    packet_pairs[curr_index] = [line]
                else:
                    packet_pairs[curr_index].append(line)
    return packet_pairs


def part1(packet_pairs):
    right_sum = 0
    for key, val in packet_pairs.items():
        res = is_packets_in_right_order(val[0], val[1])
        if res == Result.RIGHT:
            right_sum += key
    print(f"Part 1: {right_sum}")


def part2(packet_pairs):
    packets_received = []
    for key, val in packet_pairs.items():
        packets_received.append((val[0], val[1]))
    analyze_all_packets(packets_received)


if __name__ == "__main__":
    packet_pairs = read_input()
    part1(packet_pairs)
    part2(packet_pairs)

