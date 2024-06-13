import curses
import random

# Constants
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
OBSTACLE = '#'

# Initialize the game screen
def init_screen():
    screen = curses.initscr()
    curses.curs_set(0)
    screen.keypad(1)
    screen.timeout(100)
    return screen

# Generate food at a random position
def generate_food(snake, obstacles, screen, food_char):
    food = None
    while food is None:
        nf = [
            random.randint(1, screen.getmaxyx()[0] - 2),
            random.randint(1, screen.getmaxyx()[1] - 2)
        ]
        food = nf if nf not in snake and nf not in obstacles else None
    screen.addch(food[0], food[1], food_char)
    return food

# Generate obstacles
def generate_obstacles(screen, snake):
    obstacles = []
    num_obstacles = int(0.05 * screen.getmaxyx()[0] * screen.getmaxyx()[1] / 5)
    for _ in range(num_obstacles):
        start = [
            random.randint(1, screen.getmaxyx()[0] - 2),
            random.randint(1, screen.getmaxyx()[1] - 2)
        ]
        if random.choice([True, False]):
            # Horizontal obstacle
            for i in range(5):
                obstacles.append([start[0], start[1] + i])
        else:
            # Vertical obstacle
            for i in range(5):
                obstacles.append([start[0] + i, start[1]])
    for obstacle in obstacles:
        screen.addch(obstacle[0], obstacle[1], OBSTACLE)
    return obstacles

# Main function
def main(screen):
    # Initialize game
    snake = [[4,10], [4,9], [4,8]]
    direction = curses.KEY_RIGHT
    food = generate_food(snake, [], screen, NORMAL_FOOD)
    special_food = generate_food(snake, [], screen, SPECIAL_FOOD)
    obstacles = generate_obstacles(screen, snake)
    score_normal = 0
    score_special = 0
    paused = False

    while True:
        next_key = screen.getch()
        direction = direction if next_key == -1 else next_key

        if next_key == ord(' '):
            paused = not paused
            continue

        if paused:
            continue

        # Calculate new head of the snake
        head = snake[0]
        if direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]

        # Wrap around the screen
        new_head[0] %= screen.getmaxyx()[0]
        new_head[1] %= screen.getmaxyx()[1]

        # Game over conditions
        if new_head in snake or new_head in obstacles:
            msg = f"Game Over! Score: Normal Food: {score_normal}, Special Food: {score_special}"
            screen.addstr(screen.getmaxyx()[0] // 2, screen.getmaxyx()[1] // 2 - len(msg) // 2, msg)
            screen.refresh()
            screen.getch()
            break

        # Check for food
        if new_head == food:
            snake.insert(0, new_head)
            food = generate_food(snake, obstacles, screen, NORMAL_FOOD)
            score_normal += 1
        elif new_head == special_food:
            snake.insert(0, new_head)
            special_food = generate_food(snake, obstacles, screen, SPECIAL_FOOD)
            if len(snake) > 1:
                snake.pop()
            score_special += 1
        else:
            snake.insert(0, new_head)
            snake.pop()

        # Update snake on screen
        screen.clear()
        for segment in snake:
            screen.addch(segment[0], segment[1], 'O')
        screen.addch(food[0], food[1], NORMAL_FOOD)
        screen.addch(special_food[0], special_food[1], SPECIAL_FOOD)
        for obstacle in obstacles:
            screen.addch(obstacle[0], obstacle[1], OBSTACLE)
        screen.refresh()

# Run the game
curses.wrapper(main)
