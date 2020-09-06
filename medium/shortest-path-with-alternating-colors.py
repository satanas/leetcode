# 0 (red)-> 1 (red)-> 2
#           1 (blue)-> 2
# 0 (red)-> 3 
#           3 (red) -> 1
# Sort red_edges and blue_edges
# Iterate from 0 to n (x)
# For each x, calculate the shortest path

# Shortest path to n
# For each i in n:
# start = 0
# end = i
# For end = 0 always return zero
# red_index = 0
# blue_index = 0
# distances
# last_link_color = None
# Get links (if exist) from

# foobar(i, last_color):
# red[i] has something: then foobar(red[i], 'red')
# dist += 1
class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        self.red = self.calculate_hashmaps(red_edges)
        self.blue = self.calculate_hashmaps(blue_edges)
        results = [0]
        print(self.red)
        print(self.blue)
        for i in range(1, n):
            red_visited = {}
            blue_visited = {}
            print(f"Analyzing {i}")
            results.append(self.recursive_search(0, 0, i, None, red_visited, blue_visited))
        
        return results

    def recursive_search(self, distance, node, n, next_color, red_visited, blue_visited):
        if node == n:
            print(f"Node found! Distance: {distance}")
            return distance 

        print(f"node: {node} - n: {n} - distance: {distance} - in red: {node in self.red} - in blue: {node in self.blue} - next_color: {next_color} - red_visited: {red_visited} - blue_visited: {blue_visited}")
        min_distance = None
        if (next_color is None or next_color == 'red') and node in self.red and node not in red_visited:
            red_visited[node] = True
            for r in self.red[node]:
                d = self.recursive_search(distance + 1, r, n, 'blue', red_visited, blue_visited)
                print(f"red => d: {d} - r: {r} - distance: {distance + 1}")
                if d >= 0 and (min_distance is None or d < min_distance):
                    min_distance = d 

        if (next_color is None or next_color == 'blue') and node in self.blue and node not in blue_visited:
            blue_visited[node] = True
            for b in self.blue[node]:
                print(f"Blue node: {b}")
                d = self.recursive_search(distance + 1, b, n, 'red', red_visited, blue_visited)
                print(f"blue => d: {d} - b: {b} - distance: {distance + 1}")
                if d >= 0 and (min_distance is None or d < min_distance):
                    min_distance = d 

        print(f"min_distance: {min_distance}")
        return min_distance if min_distance is not None else -1

    def calculate_hashmaps(self, edges):
        hashmap = {}
        for r in edges:
            orig = r[0]
            dest = r[1]
            if orig in hashmap:
                hashmap[orig].append(dest)
            else:
                hashmap[orig] = [dest]
        return hashmap

if __name__ == "__main__":
    s = Solution()
    # print(s.shortestAlternatingPaths(3, [[0,1],[1,2]], []))
    # print(s.shortestAlternatingPaths(3, [[0,1]], [[2,1]]))
    # print(s.shortestAlternatingPaths(3, [[1,0]], [[2,1]]))
    # print(s.shortestAlternatingPaths(3, [[0,1]], [[1,2]]))
    # print(s.shortestAlternatingPaths(3, [[0,1],[0,2]], [[1,0]]))
    # print(s.shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))
    print(s.shortestAlternatingPaths(5, [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]], [[1,3],[0,0],[0,3],[4,2],[1,0]]))


