
"""
Functions for checking visibility in each of the 4 directions.
Split into 4 functions for readability
"""
def is_left_visible(grid, row_num, col_num):
    for i in range(col_num - 1, -1, -1):
        if grid[row_num][i] < grid[row_num][col_num]:
            continue
        else:
            return False
    return True


def is_top_visible(grid, row_num, col_num):
    for i in range(row_num - 1, -1, -1):
        if grid[i][col_num] < grid[row_num][col_num]:
            continue
        else:
            return False
    return True
    

def is_right_visible(grid, row_num, col_num):
    for i in range(col_num + 1, len(grid[0])):
        if grid[row_num][i] < grid[row_num][col_num]:
            continue
        else:
            return False
    return True


def is_bottom_visible(grid, row_num, col_num):
    for i in range(row_num + 1, len(grid)):
        if grid[i][col_num] < grid[row_num][col_num]:
            continue
        else:
            return False
    return True

# ########################### Part 2 ###########################

"""
Similar to the visibility functions above, we calculate the scenic
scores in each direction. If we see a smaller tree than the one we're
checking, we increment a count and continue checking that direction, otherwise
we increment the count (because we've still seen a tree) and return the count
"""
def left_scenic_score(grid, row_num, col_num):
    score = 0
    for i in range(col_num - 1, -1, -1):
        if grid[row_num][i] < grid[row_num][col_num]:
            score += 1
            continue
        else:
            score += 1
            return score
    return score


def top_scenic_score(grid, row_num, col_num):
    score = 0
    for i in range(row_num - 1, -1, -1):
        if grid[i][col_num] < grid[row_num][col_num]:
            score += 1
            continue
        else:
            score += 1
            return score
    return score
    

def right_scenic_score(grid, row_num, col_num):
    score = 0
    for i in range(col_num + 1, len(grid[0])):
        if grid[row_num][i] < grid[row_num][col_num]:
            score += 1
            continue
        else:
            score += 1
            return score
    return score


def bottom_scenic_score(grid, row_num, col_num):
    score = 0
    for i in range(row_num + 1, len(grid)):
        if grid[i][col_num] < grid[row_num][col_num]:
            score += 1
            continue
        else:
            score += 1
            return score
    return score

# ######################################################

def is_tree_visible(grid, row_num, col_num):
    """
    Helper function to check if a tree is visible or not
    """
    if is_left_visible(grid, row_num, col_num) or \
                is_top_visible(grid, row_num, col_num) or \
                    is_right_visible(grid, row_num, col_num) or \
                        is_bottom_visible(grid, row_num, col_num):
                return True
    else:
        return False


def get_scenic_score(grid, row_num, col_num):
    """
    Helper Function to get the scenic score for a particular tree
    """
    return left_scenic_score(grid, row_num, col_num) * top_scenic_score(grid, row_num, col_num) * right_scenic_score(grid, row_num, col_num) * bottom_scenic_score(grid, row_num, col_num)


def iterate_inner_grid(grid):
    top_scenic_score = 0
    columns = len(grid[0])
    rows = len(grid)
    visible_trees = (columns * 2) + (rows - 2) + (rows - 2)
    print(f"Outer Visibility: {visible_trees}")
    for row_num in range(1, rows - 1):
        for col_num in range(1, columns - 1):
            # if is_tree_visible:
            #     visible_trees += 1
            scenic_score = get_scenic_score(grid, row_num, col_num)
            if scenic_score > top_scenic_score:
                top_scenic_score = scenic_score
    print(top_scenic_score)

def generate_grid():
    """
    Generate a List[List[]] structure, which is essentially a 
    2-D array to represent the grid
    """
    grid = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            grid.append(list(line.strip()))
    return grid

if __name__ == "__main__":
    grid = generate_grid()
    columns = len(grid[0])
    rows = len(grid)
    iterate_inner_grid(grid)
