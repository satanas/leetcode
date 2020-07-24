def cyclic_sort(nums):
    for i in range(len(nums)):
        curr_num = nums[i]
        if curr_num != i + 1:
            temp = nums[curr_num - 1]
            nums[curr_num - 1] = curr_num
            nums[i] = temp

    return nums

if __name__ == "__main__":
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))