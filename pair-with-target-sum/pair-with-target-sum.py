def pair_with_targetsum(arr, target_sum):
    start_pointer = 0
    end_pointer = len(arr) - 1

    while start_pointer < end_pointer:
        curr_sum = arr[start_pointer] + arr[end_pointer]

        if curr_sum == target_sum:
            return [start_pointer, end_pointer]

        if curr_sum < target_sum:
            start_pointer += 1
        if curr_sum > target_sum:
            end_pointer -= 1

    return [-1, -1]

if __name__ == "__main__":
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
    print(pair_with_targetsum([1, 3, 7, 8, 10], 24))