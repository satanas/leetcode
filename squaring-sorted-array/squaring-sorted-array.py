def make_squares(arr):
    squares = []
    start_pointer = 0
    end_pointer = len(arr) - 1

    while start_pointer <= end_pointer:
        left = pow(arr[start_pointer], 2)
        right = pow (arr[end_pointer], 2)

        if right >= left:
            squares.insert(0, right)
            end_pointer -= 1
        else:
            squares.insert(0, left)
            start_pointer += 1
        
    return squares

if __name__ == "__main__":
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
    print(make_squares([-4, -3, -2, -1]))
    print(make_squares([1, 2, 3, 4]))
    print(make_squares([-3, -2, 0, 1]))