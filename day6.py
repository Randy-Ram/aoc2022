from collections import deque


class DataStream:
    def __init__(self):
        self.start_sequence = deque()
        self.message_sequence = deque()
        self.start_marker = 0
        self.message_marker = 0

    def _add_char_to_start_sequence(self, val):
        if len(self.start_sequence) < 4:
            self.start_sequence.append(val)
        else:
            self.start_sequence.popleft()
            self.start_sequence.append(val)
        self.start_marker += 1

    def _add_char_to_message_sequence(self, val):
        if len(self.message_sequence) < 14:
            self.message_sequence.append(val)
        else:
            self.message_sequence.popleft()
            self.message_sequence.append(val)
        self.message_marker += 1

    def add_character_to_datastream(self, val):
        self._add_char_to_start_sequence(val)
        self._add_char_to_message_sequence(val)

    def is_start_of_packet_marker(self):
        print(self.start_sequence)
        return len(set(self.start_sequence)) == 4

    def is_start_of_message_marker(self):
        print(self.start_sequence)
        return len(set(self.message_sequence)) == 14

    def get_start_marker(self):
        return self.start_marker

    def get_message_marker(self):
        return self.message_marker


if __name__ == "__main__":
    d = DataStream()
    with open("input.txt", "r") as data:
        line = data.readline()
        line = line.strip()
        for letter in line:
            d.add_character_to_datastream(letter)
            if d.is_start_of_message_marker():
                print(d.get_message_marker())
                exit()
