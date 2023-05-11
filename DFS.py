def dfs(x, y, visited, goal, capacity):
    if visited[x][y]:
        return False

    visited[x][y] = True
    if x == goal or y == goal:
        return True

    if dfs(capacity[0], y, visited, goal, capacity):
        return True

    if dfs(x, capacity[1], visited, goal, capacity):
        return True

    if dfs(0, y, visited, goal, capacity):
        return True

    if dfs(x, 0, visited, goal, capacity):
        return True

    if x+y >= capacity[1]:
        if dfs(capacity[1], y-(capacity[1]-x), visited, goal, capacity):
            return True
    else:
        if dfs(x+y, 0, visited, goal, capacity):
            return True

    if x+y >= capacity[0]:
        if dfs(x-(capacity[0]-y), capacity[0], visited, goal, capacity):
            return True
    else:
        if dfs(0, x+y, visited, goal, capacity):
            return True

    return False

def water_jug_problem(x, y, goal, capacity):
    visited = [[False for j in range(y+1)] for i in range(x+1)]
    return dfs(0, 0, visited, goal, [x, y])

water_jug_problem(0, 0, 4, [5, 3])
