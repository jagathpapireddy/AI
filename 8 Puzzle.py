import heapq

def heuristic(s, goal):
    h = 0
    for i in range(9):
        if s[i] != 0:
            j = goal.index(s[i])
            h += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return h


def solve(start, goal):
    pq = [(heuristic(start, goal), 0, start)]
    visited = {start: 0}
    parent = {start: None}

    while pq:
        f, g, s = heapq.heappop(pq)

        if g != visited[s]:
            continue

        if s == goal:
            path = []
            while s is not None:
                path.append(s)
                s = parent[s]
            return path[::-1]

        z = s.index(0)
        r, c = z // 3, z % 3

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                b = list(s)
                b[z], b[nz] = b[nz], b[z]
                ns = tuple(b)
                ng = g + 1

                if ns not in visited or ng < visited[ns]:
                    visited[ns] = ng
                    parent[ns] = s
                    heapq.heappush(
                        pq, (ng + heuristic(ns, goal), ng, ns)
                    )

    return None


# User input
print("Enter start state (9 numbers, 0 represents blank):")
start = tuple(map(int, input().split()))

print("Enter goal state (9 numbers, 0 represents blank):")
goal = tuple(map(int, input().split()))

# Validate input
if (len(start) != 9 or len(goal) != 9
        or sorted(start) != list(range(9))
        or sorted(goal) != list(range(9))):
    print("Invalid input")

else:
    # Check solvability relative to the goal
    goal_order = [x for x in goal if x != 0]
    goal_rank = {x: i for i, x in enumerate(goal_order)}

    arr = [x for x in start if x != 0]
    arr = [goal_rank[x] for x in arr]

    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1

    if inv % 2 != 0:
        print("Puzzle is not solvable")
    else:
        path = solve(start, goal)

        if path:
            for step, s in enumerate(path):
                print("Step", step)
                for i in range(0, 9, 3):
                    print(s[i:i + 3])
                print()

            print("Total moves:", len(path) - 1)
        else:
            print("No solution")
