def dutch_flag_sort(arr):
    low = 0
    high = len(arr) - 1
    i = 0

    while i <= high:
        if arr[i] == 0:
            temp = arr[i]
            arr[i] = arr[low]
            arr[low] = temp
            low += 1
            i += 1
        elif arr[i] == 2:
            temp = arr[high]
            arr[high] = arr[i]
            arr[i] = temp
            high -=1
        else:
            i += 1
                
    return arr


if __name__ == "__main__":
    print(dutch_flag_sort([1, 0, 2, 1, 0]))
    print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
    print(dutch_flag_sort([2, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 1]))