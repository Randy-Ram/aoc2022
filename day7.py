class File:
    """Model File object as a class
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    """Model Directory
    We also store a pointer to the parent of this directory
    """
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = []
    
    def add_item(self, item):
        self.contents.append(item)

# Globals to keep track of where we have started and where we are
# currently while parsing input
START_DIRECTORY = None
CURRENT_DIRECTORY = None

def handle_cd_command(command, arg):
    """We process the cd command in 3 ways:

    - Is it the first time we're running it
    - Is it a change directory to go back to parent
    - Are we navigating to a new directory
    """
    global START_DIRECTORY
    global CURRENT_DIRECTORY
    if START_DIRECTORY is None:
        start_dir = Directory(name=arg, parent=None)
        START_DIRECTORY = start_dir
        CURRENT_DIRECTORY = start_dir
        return
    elif arg == "..":
        CURRENT_DIRECTORY = CURRENT_DIRECTORY.parent
        return
    else:
        next_directory = Directory(name=arg, parent=CURRENT_DIRECTORY)
        CURRENT_DIRECTORY.add_item(next_directory)
        CURRENT_DIRECTORY = next_directory
        return


def process_commmand(line):
    split_command = line.split(" ")
    command = split_command[1]
    if command == "cd":
        arg = split_command[2]
        handle_cd_command(command, arg)
    elif command == "ls":
        pass


def process_ls(line):
    global CURRENT_DIRECTORY
    split_file = line.split(" ")
    if split_file[0] == "dir":
        # We cd into this directory later so don't do anything here
        # When we cd we will create the Directory object
        pass
    else:
        # If we see a file, add it to the current directory's contents
        size, name = split_file[0], split_file[1]
        f = File(name, size)
        CURRENT_DIRECTORY.add_item(f)
    

def process_line(line):
    if line.startswith('$'):
        process_commmand(line)
    else:
        process_ls(line)


with open("input.txt", "r") as command_history:
    for line in command_history:
        line = line.strip()
        process_line(line)


directory_sizes = []

def get_directory_size(directory):
    """We recursively iterate over Directory structure and
    gets the size of the directory. 
    We store each directory size in a global dict so we can
    use in part 2.

    Args:
        directory (Directory): Directory to iterate over

    Returns:
        int: Size of the current directory
    """
    global TOTAL_SIZE
    directory_size = 0
    for item in directory.contents:
        if isinstance(item, File):
            item_size = int(item.size)
            # print(f"File: {item_size} {item.name}")
            directory_size += item_size
        elif isinstance(item, Directory):
            # print(f"Directory: {item.name}")
            directory_size += get_directory_size(item)
    directory_sizes.append(directory_size)
    return directory_size


# Perform caclculations for part 2
get_directory_size(START_DIRECTORY)
directory_sizes = sorted(directory_sizes)
print(directory_sizes)

FINAL_SPACE_REQUIRED = 70000000
UPGRADE_SPACE_NEEDED = 30000000
max_value = max(directory_sizes)
free_space_now = FINAL_SPACE_REQUIRED - max_value
for val in directory_sizes:
    if free_space_now + val > UPGRADE_SPACE_NEEDED:
        print(val)
        exit()


