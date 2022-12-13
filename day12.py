import sys
from pprint import pprint

def is_next_square_viable(map, curr_row, curr_col, next_row, next_col):
    current_value = map[curr_row][curr_col] if map[curr_row][curr_col] != 'S' else 'a'
    next_value = map[next_row][next_col] if map[next_row][next_col] != 'E' else 'z'
    if ord(next_value) - ord(current_value) <= 1:
        return True
    else:
        return False

def get_possible_moves(map, row, col):
    allowed_moves = []
    map_rows = len(map)
    map_cols = len(map[0])
    # Check up
    if row > 0 and is_next_square_viable(map, row, col, row-1, col):
        allowed_moves.append((row-1, col))
    # Check right
    if col < map_cols - 1 and is_next_square_viable(map, row, col, row, col + 1):
        allowed_moves.append((row, col + 1))
    # Check down
    if row < map_rows - 1 and is_next_square_viable(map, row, col, row + 1, col):
        allowed_moves.append((row + 1, col))
    # Check left
    if col > 0 and is_next_square_viable(map, row, col, row, col - 1):
        allowed_moves.append((row, col - 1))
    return allowed_moves


def generate_graph(map):
    connected_edges = {}
    map_rows = len(map)
    map_cols = len(map[0])
    for i in range(map_rows):
        for j in range(map_cols):
            connected_edges[(i, j)] = get_possible_moves(map, i, j)
    return connected_edges

def initialize_distances(map):
    distances = {}
    previous = {}
    map_rows = len(map)
    map_cols = len(map[0])
    for i in range(map_rows):
        for j in range(map_cols):
            distances[(i, j)] = sys.maxsize
            previous[(i, j)] = None
    return distances, previous


def perform_bfs(map, start_idx):
    graph = generate_graph(map)
    distances, previous = initialize_distances(map)
    queue = []
    distances[start_idx] = 0
    for node in graph.keys():
        queue.append(node)
    while len(queue) > 0:
        min_dist_vertex = min(queue, key=distances.get)
        queue.remove(min_dist_vertex)

        for neighbor in graph[min_dist_vertex]:
            if neighbor in queue:
                distance_from_start = distances[min_dist_vertex] + 1
                if distance_from_start < distances[neighbor]:
                    distances[neighbor] = distance_from_start
                    previous[neighbor] = min_dist_vertex
    return distances, previous


def get_shortest_distance_from_each_starting_point(map, possible_starting_points, ending_idx):
    shortest_dist_so_far = sys.maxsize
    for each_starting_point in possible_starting_points:
        distances, _ = perform_bfs(map, each_starting_point)
        if distances[ending_idx] < shortest_dist_so_far:
            shortest_dist_so_far = distances[ending_idx]

    return shortest_dist_so_far

def read_input():
    map = []
    starting_pos = None
    ending_pos = None
    possible_starting_points = []
    with open("input.txt", "r") as input_file:
        for line_num, line in enumerate(input_file):
            line = line.strip()
            line = list(line)
            if 'S' in line:
                starting_index = (line_num, line.index('S'))
                possible_starting_points.append((line_num, line.index('S')))
            if 'E' in line:
                ending_index = (line_num, line.index('E'))
            if 'a' in line:
                possible_starting_points.append((line_num, line.index('a')))
            map.append(line)
    return map, starting_index, ending_index, possible_starting_points


if __name__ == "__main__":
    map, starting_idx, ending_idx , possible_starting_points = read_input()
    distances, prev = perform_bfs(map, starting_idx)
    # pprint(distances)
    pprint(f"Part 1 Answer: {distances[ending_idx]}")
    shortest_dist = get_shortest_distance_from_each_starting_point(map, possible_starting_points, ending_idx)
    pprint(f"Part 2 Answer: {shortest_dist}")