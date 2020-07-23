def merge(intervals_a, intervals_b):
    merged = intervals_a + intervals_b
    merged.sort(key=lambda x: x[0])
    result = []
    for i in range(len(merged) - 1):
        if merged[i + 1][0] <= merged[i][1]:
            start = max(merged[i][0], merged[i + 1][0])
            end = min(merged[i][1], merged[i + 1][1])
            result.append([start, end])
    return result



if __name__ == "__main__":
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))