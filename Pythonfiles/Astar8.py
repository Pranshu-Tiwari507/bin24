import heapq

goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]          # change this to any valid goal

# position of every tile in the goal: {tile: (row, col)}
goal_pos = {goal[i][j]: (i, j) for i in range(3) for j in range(3)}


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def heuristic(state):
    """Manhattan distance of every tile from its position in the GOAL."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_row, goal_col = goal_pos[value]
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance


def get_neighbors(state):
    neighbors = []
    row, col = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # up, down, left, right

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [r[:] for r in state]
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            neighbors.append(new_state)

    return neighbors


def a_star(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == goal:
            return path + [current]

        current_tuple = tuple(map(tuple, current))
        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(map(tuple, neighbor))

            if neighbor_tuple not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [current]))

    return None


start = [[2, 8, 3],
         [1, 6, 4],
         [7, 0, 5]]

solution = a_star(start)

if solution:
    print("Solution Found!\n")
    for step, state in enumerate(solution):
        print("Step", step)
        for row in state:
            print(row)
        print()
else:
    print("No Solution Found")


# import heapq
#
# goal = [[1, 2, 3],
#         [8, 0, 4],
#         [7, 6, 5]]          # change this to any valid goal
#
# # position of every tile in the goal: {tile: (row, col)}
# goal_pos = {goal[i][j]: (i, j) for i in range(3) for j in range(3)}
#
#
# def find_blank(state):
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == 0:
#                 return i, j
#
#
# def heuristic(state):
#     """Manhattan distance of every tile from its position in the GOAL."""
#     distance = 0
#     for i in range(3):
#         for j in range(3):
#             value = state[i][j]
#             if value != 0:
#                 goal_row, goal_col = goal_pos[value]
#                 distance += abs(i - goal_row) + abs(j - goal_col)
#     return distance
#
#
# def count_inversions(state):
#     flat = [v for row in state for v in row if v != 0]   # flatten, ignore blank
#     inversions = 0
#     for i in range(len(flat)):
#         for j in range(i + 1, len(flat)):
#             if flat[i] > flat[j]:
#                 inversions += 1
#     return inversions
#
#
# def is_solvable(state):
#     """3x3 puzzle: start and goal must have the same inversion parity."""
#     return count_inversions(state) % 2 == count_inversions(goal) % 2
#
#
# def get_neighbors(state):
#     neighbors = []
#     row, col = find_blank(state)
#     moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # up, down, left, right
#
#     for dr, dc in moves:
#         new_row = row + dr
#         new_col = col + dc
#
#         if 0 <= new_row < 3 and 0 <= new_col < 3:
#             new_state = [r[:] for r in state]
#             new_state[row][col], new_state[new_row][new_col] = \
#                 new_state[new_row][new_col], new_state[row][col]
#             neighbors.append(new_state)
#
#     return neighbors
#
#
# def a_star(start):
#     # Solvability check: stop immediately if the puzzle cannot be solved
#     if not is_solvable(start):
#         return None
#
#     pq = []
#     heapq.heappush(pq, (heuristic(start), 0, start, []))
#     visited = set()
#
#     while pq:
#         f, g, current, path = heapq.heappop(pq)
#
#         if current == goal:
#             return path + [current]
#
#         current_tuple = tuple(map(tuple, current))
#         if current_tuple in visited:
#             continue
#         visited.add(current_tuple)
#
#         for neighbor in get_neighbors(current):
#             neighbor_tuple = tuple(map(tuple, neighbor))
#
#             if neighbor_tuple not in visited:
#                 new_g = g + 1
#                 new_f = new_g + heuristic(neighbor)
#                 heapq.heappush(pq, (new_f, new_g, neighbor, path + [current]))
#
#     return None
#
#
# start = [[2, 8, 3],
#          [1, 6, 4],
#          [7, 0, 5]]
#
# if not is_solvable(start):
#     print("This puzzle is unsolvable (parity of start and goal differ).")
# else:
#     solution = a_star(start)
#
#     if solution:
#         print("Solution Found!\n")
#         for step, state in enumerate(solution):
#             print("Step", step)
#             for row in state:
#                 print(row)
#             print()
#     else:
#         print("No Solution Found")