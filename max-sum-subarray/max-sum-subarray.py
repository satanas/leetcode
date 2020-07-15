def max_sub_array_of_size_k(k, arr):
    index_acc = 0
    curr_sum = 0
    max_sum = -1

    for x in range(len(arr)):
        index_acc += 1
        index_out = x - k
        curr_sum += arr[x]

        if index_acc == k:
            if index_out >= 0:
                curr_sum -= arr[index_out]
            if curr_sum > max_sum:
                max_sum = curr_sum
            index_acc = 0

    return max_sum

if __name__ == "__main__":
    print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))