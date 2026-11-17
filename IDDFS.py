
graph = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter start node: ")
goal = input("Enter goal node: ")


def dls(node, goal, limit, path):
    print(node, end=" ")

    if node == goal:
        return path

    if limit == 0:
        return None

    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dls(
                neighbor, goal, limit - 1,
                path + [neighbor]
            )

            if result is not None:
                return result

    return None


found = False

for depth in range(len(graph) + 1):
    print("\nDepth", depth, ":", end=" ")

    result = dls(start, goal, depth, [start])

    if result is not None:
        print("\nPath:", " -> ".join(result))
        print("Depth:", len(result) - 1)
        found = True
        break

if not found:
    print("\nNo path found")
