from collections import deque

def print_matrix(matrix, path=None):
    rows, cols = len(matrix), len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            if (i, j) == (0, 0):  
                print("S ", end="")  
            elif (i, j) == (3, 3):  
                print("E ", end="")  
            elif path and (i, j) in path:  
                print("* ", end="")  
            else:  
                print(". ", end="")  
        print()

def bfs_shortest_path(matrix):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    start, end = (0, 0), (3, 3)  
    
    queue = deque([(start, [])])  
    visited = set([start])  

    while queue:
        (row, col), path_so_far = queue.popleft()

        if (row, col) == end:
            path = path_so_far + [(row, col)]
            print(f"\nShortest Path Length: {len(path) - 1}\n")
            print("Path in Matrix:")
            print_matrix(matrix, path)
            return

        for dr, dc in directions:
            new_pos = (row + dr, col + dc)

            if 0 <= new_pos[0] < len(matrix) and 0 <= new_pos[1] < len(matrix[0]):
                if new_pos not in visited:
                    queue.append((new_pos, path_so_far + [(row, col)]))
                    visited.add(new_pos)

    print("No path found.")

matrix = [[0] * 5 for _ in range(5)]

print("Original Matrix:")
print_matrix(matrix)
bfs_shortest_path(matrix)
