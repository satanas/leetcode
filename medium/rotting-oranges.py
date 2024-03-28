def min_minutes_to_rot(grid):
    rotten_oranges = []
    fresh_oranges = 0
    total_rot = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rotten_oranges.append((i, j))
            elif grid[i][j] == 1:
                fresh_oranges += 1

    if fresh_oranges == 0:
        print("No fresh oranges.")
        return 0
    if len(rotten_oranges) == 0:
        print("No rotten oranges.")
        return -1
    
    visited = []
    queue = []
    for r in rotten_oranges:
        visited.append((r[0], r[1]))
        queue.append((r[0] - 1, r[1], 0))
        queue.append((r[0] + 1, r[1], 0))
        queue.append((r[0], r[1] - 1, 0))
        queue.append((r[0], r[1] + 1, 0))
    print("Added surrounding of rotten oranges to the queue=%s and to visited=%s" % (queue, visited))

    while len(queue) > 0:
        x, y, curr_min = queue.pop(0)
        if (x, y) in visited:
            print("Grid[%s,%s]=%s already visited" % (x, y, grid[x][y]))
            continue
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
            continue

        print("Processing grid[%s,%s]=%s - curr_min=%s" % (x, y, grid[x][y], curr_min))
        visited.append((x, y))
        if grid[x][y] == 0:
            continue
        if grid[x][y] == 1:
            grid[x][y] = 2
            total_rot += 1
            queue.append((x - 1, y, curr_min + 1))
            queue.append((x + 1, y, curr_min + 1))
            queue.append((x, y - 1, curr_min + 1))
            queue.append((x, y + 1, curr_min + 1))

    if total_rot < fresh_oranges:
        return -1
   
    return curr_min

# def recursive_traversal(x, y, grid, visited, curr_min):
#     if grid[x][y] == 0 or (x, y) in visited:
#         return curr_min
    
#     print("Processing grid[%s,%s]=%s with curr_min=%s and visited=%s" % (x, y, grid[x][y], curr_min, visited))
#     visited.append((x, y))

#     if grid[x][y] == 1:
#         grid[x][y] = 2
#         curr_min += 1
    
#     results = []
#     if x - 1 >= 0:
#         results.append(recursive_traversal(x - 1, y, grid, visited, curr_min))
#     if x + 1 < len(grid):
#         results.append(recursive_traversal(x + 1, y, grid, visited, curr_min))
#     if y - 1 >= 0:
#         results.append(recursive_traversal(x, y - 1, grid, visited, curr_min))
#     if y + 1 < len(grid[0]):
#         results.append(recursive_traversal(x, y + 1, grid, visited, curr_min))
    
#     return max(results)
    
if __name__ == "__main__":
    print(min_minutes_to_rot([[2,1,1],[1,1,0],[0,1,1]]))
    # print(min_minutes_to_rot([[1,2,1,2,1,2],[2,1,2,1,2,1],[1,2,1,2,1,2],[2,1,2,1,2,1]]))