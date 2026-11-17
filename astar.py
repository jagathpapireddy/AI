import heapq

graph = {}
heuristic = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    u, v, cost = input("Enter edge (u v cost): ").split()
    cost = int(cost)

    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))

nodes = set(graph.keys())
for edges in graph.values():
    for v, cost in edges:
        nodes.add(v)

for node in nodes:
    heuristic[node] = int(input("Heuristic for " + node + ": "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

pq = [(heuristic[start], 0, start)]
parent = {start: None}
visited = {}

while pq:
    f, g, u = heapq.heappop(pq)

    if u in visited and visited[u] <= g:
        continue
    visited[u] = g

    if u == goal:
        break

    for v, cost in graph.get(u, []):
        new_g = g + cost

        if v not in visited or new_g < visited[v]:
            parent[v] = u
            heapq.heappush(
                pq, (new_g + heuristic[v], new_g, v)
            )

if goal in visited:
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    print("Path:", " -> ".join(path[::-1]))
    print("Cost:", visited[goal])
else:
    print("No path found")
