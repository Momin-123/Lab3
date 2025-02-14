import time

def convert_to_tuple(state):
    return tuple(tuple(state[i:i+3]) for i in range(0, 9, 3))

def convert_to_string(matrix):
    return ''.join(''.join(row) for row in matrix)

def generate_moves(matrix):
    moves = []
    x, y = next((i, j) for i in range(3) for j in range(3) if matrix[i][j] == '0')

    directions = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}

    for direction, (dx, dy) in directions.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_matrix = [list(row) for row in matrix]
            new_matrix[x][y], new_matrix[new_x][new_y] = new_matrix[new_x][new_y], new_matrix[x][y]
            moves.append(tuple(tuple(row) for row in new_matrix))
    
    return moves

def depth_first_search(start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        current, path = stack.pop()
        
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path + [current]

        for move in generate_moves(current):
            if move not in visited:
                stack.append((move, path + [current]))

    return None

def execute():
    start = input("Enter start State: ")
    goal = input("Enter goal State: ")

    start_tuple = convert_to_tuple(start)
    goal_tuple = convert_to_tuple(goal)

    print("-----------------")
    print("DFS Algorithm")
    print("-----------------")

    start_time = time.time()
    solution_path = depth_first_search(start_tuple, goal_tuple)
    end_time = time.time()

    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path) - 1)
        print("No of Nodes Visited:", len(solution_path))
        
        for state in solution_path:
            for row in state:
                print(' '.join(row))
            print("------")
    else:
        print("No solution found.")

if __name__ == "__main__":
    execute()
