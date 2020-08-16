from heapq import *

class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []
        for x in nums:
            heappush(min_heap, x)

            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]

if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))