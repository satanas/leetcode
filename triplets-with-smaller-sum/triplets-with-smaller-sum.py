def triplet_with_smaller_sum(arr, target_sum):
    count = 0

    arr.sort()

    for i in range(len(arr) - 1):
        count = search_pairs(arr[i], i + 1, arr, target_sum, count)

    return count

def search_pairs(curr_elem, left, arr, target_sum, count):
    right = len(arr) - 1

    while left < right:
        curr_sum = curr_elem + arr[left] + arr[right]

        if curr_sum >= target_sum:
            right -= 1
        else:
            count += 1
            right -= 1

    return count



if __name__ == "__main__":
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))