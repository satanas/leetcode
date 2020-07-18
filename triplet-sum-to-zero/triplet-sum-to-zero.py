def search_triplets(arr):
    triplets = []
    
    arr.sort()
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        triplets += search_pairs(-arr[i], i + 1, arr)

    return triplets

def search_pairs(target_sum, left, arr):
    results = []
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum > target_sum:
            right -= 1
        elif curr_sum < target_sum:
            left += 1
        else:
            results.append([-target_sum, arr[left], arr[right]])
            right -= 1
            left += 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
    return results



if __name__ == "__main__":
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))

    #[-3, -2, -1, 0, 1, 1, 2]
