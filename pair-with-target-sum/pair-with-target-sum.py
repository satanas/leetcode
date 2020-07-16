def pair_with_targetsum(arr, target_sum):
    start_pointer = 0
    end_pointer = len(arr) - 1

    s = arr[start_pointer]
    e = arr[end_pointer]

    while s + e != target_sum:
        if s + e < target_sum:
            start_pointer += 1
        if s + e > target_sum:
            end_pointer -= 1

        s = arr[start_pointer]
        e = arr[end_pointer]

        if start_pointer == end_pointer:
            return [None, None]

    return [start_pointer, end_pointer]

if __name__ == "__main__":
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
    print(pair_with_targetsum([1, 3, 7, 8, 10], 24))