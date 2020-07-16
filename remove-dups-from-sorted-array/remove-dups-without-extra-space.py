def remove_duplicates(arr):
    start_pointer = 0
    end_pointer = len(arr) - 1
    left_elem = True
    right_elem = False
    new_array_size = 0

    while start_pointer < end_pointer:
        if left_elem != arr[start_pointer] and arr[start_pointer] != right_elem:
            new_array_size += 1
        if right_elem != arr[end_pointer] and left_elem != arr[end_pointer]:
            new_array_size += 1

        left_elem = arr[start_pointer]
        right_elem = arr[end_pointer]

        start_pointer += 1
        end_pointer -= 1

    return new_array_size


if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 2, 2, 11]))
    print(remove_duplicates([2, 2, 2, 11]))
    