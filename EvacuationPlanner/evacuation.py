from collections import deque

# Initial state: (people_left, people_right, boat_position)
start = (3, 0, 'L')
goal = (0, 3, 'R')

def is_valid(state):
    left, right, _ = state
    return left >= 0 and right >= 0 and (left + right == 3)

def get_next_states(state):
    left, right, boat = state
    moves = []

    if boat == 'L':
        for i in [1, 2]:
            new_state = (left - i, right + i, 'R')
            if is_valid(new_state):
                moves.append(new_state)
    else:
        for i in [1]:
            new_state = (left + i, right - i, 'L')
            if is_valid(new_state):
                moves.append(new_state)

    return moves

def bfs():
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        for next_state in get_next_states(state):
            queue.append((next_state, path))

solution = bfs()

print("Evacuation Steps:")
for step in solution:
    print(step)
