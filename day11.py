from typing import List
from collections import deque
import copy

class Monkey:
    divisor = 1
    part = 2
    def __init__(self, items: deque, divisor: int):
        self.items = items
        self.items_inspected = 0
        Monkey.divisor *= divisor
        self.divisor = divisor

    def operation(self, old, operation_fnc) -> int:
        return operation_fnc(old)

    def who_to_send_item_to(self, item, test_fnc) -> "Monkey":
        self.items_inspected += 1
        return test_fnc(item)

    def receive_item(self, item):
        self.items.append(item)

    def inspect_item(self, operation_fnc, test_fnc):
        if len(self.items) == 0:
            return
        old = self.items.popleft()
        new = operation_fnc(old)
        if Monkey.part == 1:
            new = int(new//3)
        else:
            if new > Monkey.divisor:
                new = new % Monkey.divisor
        monkey_to_toss_item_to = self.who_to_send_item_to(new, test_fnc)
        monkey_to_toss_item_to.receive_item(new)

    def __str__(self):
        return f"{self.items}"

# Monkeys
monkey_0 = Monkey(items=deque([66, 59, 64, 51]), divisor=2)
monkey_1 = Monkey(items=deque([67, 61]), divisor=7)
monkey_2 = Monkey(items=deque([86, 93, 80, 70, 71, 81, 56]), divisor=11)
monkey_3 = Monkey(items=deque([94]), divisor=19)
monkey_4 = Monkey(items=deque([71, 92, 64]), divisor=3)
monkey_5 = Monkey(items=deque([58, 81, 92, 75, 56]), divisor=5)
monkey_6 = Monkey(items=deque([82, 98, 77, 94, 86, 81]), divisor=17)
monkey_7 = Monkey(items=deque([54, 95, 70, 93, 88, 93, 63, 50]), divisor=13)


# Operations
def monkey0_operation(old):
    return old * 3

def monkey1_operation(old):
    return old * 19

def monkey2_operation(old):
    return old + 2

def monkey3_operation(old):
    return old * old

def monkey4_operation(old):
    return old + 8

def monkey5_operation(old):
    return old + 6

def monkey6_operation(old):
    return old + 7

def monkey7_operation(old):
    return old + 4


# Tests
def monkey0_test(new):
    if new % 2 == 0:
        return monkey_1
    else:
        return monkey_4

def monkey1_test(new):
    if new % 7 == 0:
        return monkey_3
    else:
        return monkey_5

def monkey2_test(new):
    if new % 11 == 0:
        return monkey_4
    else:
        return monkey_0

def monkey3_test(new):
    if new % 19 == 0:
        return monkey_7
    else:
        return monkey_6

def monkey4_test(new):
    if new % 3 == 0:
        return monkey_5
    else:
        return monkey_1

def monkey5_test(new):
    if new % 5 == 0:
        return monkey_3
    else:
        return monkey_6

def monkey6_test(new):
    if new % 17 == 0:
        return monkey_7
    else:
        return monkey_2

def monkey7_test(new):
    if new % 13 == 0:
        return monkey_2
    else:
        return monkey_0

mappings = {
    monkey_0: {
        "operation": monkey0_operation,
        "test": monkey0_test
    },
    monkey_1: {
        "operation": monkey1_operation,
        "test": monkey1_test
    },
    monkey_2: {
        "operation": monkey2_operation,
        "test": monkey2_test
    },
    monkey_3: {
        "operation": monkey3_operation,
        "test": monkey3_test
    },
    monkey_4: {
        "operation": monkey4_operation,
        "test": monkey4_test
    },
    monkey_5: {
        "operation": monkey5_operation,
        "test": monkey5_test
    },
    monkey_6: {
        "operation": monkey6_operation,
        "test": monkey6_test
    },
    monkey_7: {
        "operation": monkey7_operation,
        "test": monkey7_test
    }
}

# Monkey List
monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
for i in range(1, 10001):
    for each_monkey in monkeys:
        operation_fnc = mappings.get(each_monkey).get("operation")
        test_fnc = mappings.get(each_monkey).get("test")
        monkey_items = copy.deepcopy(each_monkey.items)
        for each_item in monkey_items:
            each_monkey.inspect_item(operation_fnc=operation_fnc, test_fnc=test_fnc)

    # print(f"Round {i}")
    # for each_monkey in monkeys:
    #     print(each_monkey)
    #     print(each_monkey.items_inspected)
    # print("*" * 75)

inspected_counts = sorted([x.items_inspected for x in monkeys])
print(inspected_counts)
print(f"Monkey Business Level: {inspected_counts[-2] * inspected_counts[-1]}")
