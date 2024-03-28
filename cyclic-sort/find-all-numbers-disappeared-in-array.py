def find_disappeared_numbers(nums):
    cyclic_sort(nums)
    print(nums)
    
    result = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            result.append(i + 1)
    return result

def cyclic_sort(nums):
    for i in range(len(nums)):
        print("Processing index ", i)
        while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
            tmp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = tmp

if __name__ == "__main__":
    # print(find_disappeared_numbers([1,2,5,2,2]))
    print(find_disappeared_numbers([3,7,3,1,9,13,10,3,8,7,1,5,13]))