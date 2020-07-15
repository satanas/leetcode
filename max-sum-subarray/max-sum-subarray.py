def max_sub_array_of_size_k(k, arr):
    window_start = 0
    window_sum = 0
    max_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            if window_sum > max_sum:
                max_sum = window_sum
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum

if __name__ == "__main__":
    print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))