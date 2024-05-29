# Requirements
# 1. Matrix of size m x n
# 2. Input of coord (x, y)
# 3. Starting position
# 4. Manhattan distance to the closest store

def shortest_distances(m, n, coords, x, y):
    input_validation(m, n, coords, x, y)

    queue = [(x, y, 0)]
    coord_set = set(coords)
    visited = set([])
    results = []

    while len(queue) > 0:
        level_size = len(queue)

        for i in range(level_size):
            x1, y1, dist = queue.pop(0)
            if (x1, y1) in visited:
                continue

            if (x1, y1) in coord_set:
                coord_set.remove(x1, y1)
                results.append(dist)
            
            visited.add((x1, y1))

            if x1 - 1 >= 0:
                queue.append((x1 - 1, y1, dist + 1))
            if x1 + 1 < m:
                queue.append((x1 + 1, y1, dist + 1))
            if y1 - 1 >= 0:
                queue.append((x1, y1 - 1, dist + 1))
            if y1 + 1 < n:
                queue.append((x1, y1 + 1, dist + 1))

    return results

def shortest_distance(m, n, coords, x, y):
    input_validation(m, n, coords, x, y)

    queue = [(x, y, 0)]
    coord_set = set(coords)
    visited = set([])

    while len(queue) > 0:
        level_size = len(queue)

        for i in range(level_size):
            x1, y1, dist = queue.pop(0)
            if (x1, y1) in visited:
                continue

            if (x1, y1) in coord_set:
                return dist
            
            visited.add((x1, y1))

            if x1 - 1 >= 0:
                queue.append((x1 - 1, y1, dist + 1))
            if x1 + 1 < m:
                queue.append((x1 + 1, y1, dist + 1))
            if y1 - 1 >= 0:
                queue.append((x1, y1 - 1, dist + 1))
            if y1 + 1 < n:
                queue.append((x1, y1 + 1, dist + 1))

    return -1

def input_validation(m, n, coords, x, y):
    # TODO: Input validation/exception
    # Making sure the starting position is valid
    # Making sure all the input coords are valid
    if m <= 0 or n <= 0 or len(coords) <= 0:
        pass
    return True      

if __name__ == "__main__":
    # print(shortest_distance(4, 4, [(2, 0), (3,1)], 0, 1))
    print(shortest_distance(4, 4, [(2, 0), (3,1)], 2, 0))
