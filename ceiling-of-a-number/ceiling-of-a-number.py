def search_ceiling_of_a_number(arr, key):
    start = 0
    end = len(arr) - 1

    while start < end:
        middle = (start // 2) + (end // 2)
        if arr[middle] == key:
            return middle

        if end - start == 1:
            if arr[start] >= key:
                return start
            if arr[start] < key and arr[end] > key:
                return end
            break
        else:
            if arr[middle] < key:
                start = middle
            elif arr[middle] > key:
                end = middle

    return -1

if __name__ == "__main__":
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))