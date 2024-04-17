def solution(n, wires):
  graph = [[] for i in range(n+1)]
  for v1, v2 in wires:
    graph[v1].append(v2)
    graph[v2].append(v1)

  def dfs(start, excluded):
    stack = [start]
    visited = set()
    while stack:
      node = stack.pop()
      if node == excluded:
        continue

      visited.add(node)

      for neighbor in graph[node]:
        if neighbor not in visited:
          stack.append(neighbor)

    return len(visited)

  min_diff = float('inf')

  for v1, v2 in wires:
    count1 = dfs(v1, v2)
    count2 = n - count1
    diff = abs(count1 - count2)
    min_diff = min(min_diff, diff)

  return min_diff
