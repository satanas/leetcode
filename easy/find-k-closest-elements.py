def find_closest_elements(nums, k, target):
    # First special case
    if target < nums[0]:
        print("target is less than lowest number in nums")
        return nums[:k]

    # Second special case
    if target > nums[-1]:
        print("target is greater than highest number in nums")
        return nums[-k]

    start = end = find_closest_to_target(nums, target)
    print("closest index to target:", start)
    while end - start + 1 < k:
        if start - 1 < 0:
            end += 1
        elif end + 1 > len(nums) - 1:
            start -= 1
        else:
            left = abs(nums[start - 1] - target)
            right = abs(nums[end + 1] - target)
            if left < right:
                start -= 1
            elif right < left:
                end += 1
            else:
                if nums[start - 1] < nums[end + 1]:
                    start -= 1
                else:
                    end += 1

    return nums[start:end + 1]

def find_closest_to_target(nums, target):
    start = 0
    end = len(nums) - 1

    while start != end:
        middle = start + ((end - start) // 2)
        print("checking start=%s - middle=%s - end=%s - target=%s - nums[middle]=%s" % (start, middle, end, target, nums[middle]))

        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            start = middle + 1
        else:
            end = middle
            
    return start

if __name__ == "__main__":
    # print(find_closest_elements([1,2,3,4,5], 4, 3))
    # print(find_closest_elements([1,2,3,4,5], 4, -1))
    print(find_closest_elements([1,2,3,4,5,6,7], 5, 7))
    print(find_closest_elements([-29,-11,-3,0,5,10,50,63,198], 6, 8))
    