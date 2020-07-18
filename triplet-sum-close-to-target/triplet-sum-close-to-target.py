def triplet_sum_close_to_target(arr, target_sum):
    closest_sum = None
    arr.sort()

    for i in range(len(arr) - 2):
        closest_sum = search_pair(arr, i + 1, arr[i], target_sum, closest_sum)
    return closest_sum

def search_pair(arr, left, curr_elem, target_sum, closest_sum):
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right] + curr_elem
        if closest_sum is None or (abs(curr_sum - target_sum) < abs(closest_sum - target_sum)):
            closest_sum = curr_sum

        if curr_sum > target_sum:
            right -= 1
        elif curr_sum < target_sum:
            left += 1
        else:
            right -= 1
            left += 1

    return closest_sum

if __name__ == "__main__":
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))