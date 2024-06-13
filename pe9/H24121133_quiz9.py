import random
cnt = 0
def generate_maze(N, M):
    """Initialize the maze with empty cells (0)."""
    return {(i, j): 0 for i in range(N) for j in range(M)}

def add_obstacles(maze, min_obstacles, N, M):
    """Add the minimum number of obstacles randomly to the maze."""
    count = 0
    while count < min_obstacles:
        x, y = random.randint(0, N-1), random.randint(0, M-1)
        if x >= N - 1 or y >= M - 1 or x <= 0 or y <= 0:
            continue
        if maze[x][y] == 0:
            maze[x][y] = 1
            count += 1

def set_obstacle(maze, x, y, N, M):
    """Set an obstacle at a given coordinate if it's within bounds and not part of the path."""
    if x >= N or y >= M or x < 0 or y < 0:
        raise ValueError("Coordinates are out of bounds.")
    if maze[x][y] == 2:
        raise ValueError("Cannot place obstacle on the path.")
    maze[x][y] = 1

def remove_obstacle(maze, x, y, N, M):
    """Remove an obstacle at a given coordinate if it's within bounds."""
    if x >= N - 1 or y >= M - 1 or x <= 0 or y <= 0:
        raise ValueError("Coordinates are out of bounds.")
    if maze[x][y] == 1:
        maze[x][y] = 0

def print_maze(maze, N, M):
    """Print the current state of the maze."""
    for i in range(N):
        maze[i][0] = 2
    for i in range(M):
        maze[N - 1][i] = 2
    print('+-' * M,end = '+')
    print('')
    for i in range(N):
        row = ''
        for j in range(M):
            if maze[i][j] == 0:
                row += ' '
            elif maze[i][j] == 1:
                row += 'X'
            elif maze[i][j] == 2:
                row += 'O'
        print('|' + '|'.join(row) + '|')
        print('+-' * M,end = '+')
        print('')

def main():
    try:
        filename = input("Enter file name: ")
        maze_data = []
        cnt = 0
        with open(filename, 'r') as file:
            for row in file:
                if(len(row) < 2):
                    continue
                if(row[0] != '|'):
                    continue
                row = row[2:len(row) - 2]
                maze_data.append(row.split(' | '))
        # Process the lines to extract maze layout
        #real_maze = []
        #for i in range(0,)
        N = len(maze_data)
        M = len(maze_data[0])
        value_map = []
        for i in range(N):
            value_map.append([0] * M)
            for j in range(M):
                if maze_data[i][j] == 'X':
                    value_map[i][j] = 1
                    cnt = cnt + 1
        
        while True:
            print("Enter the minimum number of obstacles(MAX:",N * M - (N + M - 1),end = ' ): ')
            min_obstacles = input()
            if min_obstacles == '':
                min_obstacles = 0
            else:
                min_obstacles = int(min_obstacles)
            
            if 0 <= min_obstacles <= N * M - (N + M - 1):
                break
            else:
                print(f"Please enter a valid number between 0 and {N * M - (N + M - 1)}.")
        
        if(cnt < min_obstacles):
            add_obstacles(value_map, min_obstacles - cnt, N, M)
        
        while True:
            print_maze(value_map, N, M)
            print("Options:")
            print("1. Set obstacle")
            print("2. Remove obstacle")
            print("3. Exit")
            
            option = int(input("Enter your option: "))
            
            if option == 1:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                try:
                    set_obstacle(value_map, x, y, N, M)
                except ValueError as e:
                    print(e)
            elif option == 2:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                try:
                    remove_obstacle(value_map, x, y, N, M)
                except ValueError as e:
                    print(e)
            elif option == 3:
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except IOError:
        print("IOError occurred in main function. File not found. Please enter a valid file name.")
    except ValueError as ve:
        print(f"ValueError occurred in main function. {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
