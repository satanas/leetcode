class Solution:
    def maxArea(self, height):
        if len(height) < 2:
            return 0

        max_area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            max_area = max(max_area, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            
        return max_area

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))