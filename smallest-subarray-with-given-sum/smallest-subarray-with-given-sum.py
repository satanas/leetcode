def smallest_subarray_with_given_sum(s, arr):
    subarray_size = None

    for window_start in range(len(arr)):
        window_sum = 0
        for x in range(window_start, len(arr)):
            window_sum += arr[x]
            #print(f"x: {x} - arr[{x}]: {arr[x]} - window_sum: {window_sum}")
            if window_sum >= s:
                if subarray_size is None or (x - window_start) < subarray_size:
                    subarray_size = x - window_start + 1
                    #print(f" - subarray size: {subarray_size}")
                break
    return 0 if subarray_size is None else subarray_size

    

if __name__ == "__main__":
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
    print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))
    print(smallest_subarray_with_given_sum(17, [3, 1, 2, 6]))