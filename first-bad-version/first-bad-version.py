# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    print(f"Calling bad version with version = {version}")
    return version >= 77


class Solution:
    def firstBadVersion(self, n):
        lastKnownGood = 0
        lastKnownBad = n
        while self.is_first_bad(n) is False:
            n = lastKnownGood + ((lastKnownBad - lastKnownGood) // 2)
            if isBadVersion(n):
                lastKnownBad = n
            else:
                lastKnownGood = n
        return n

    def is_first_bad(self, n):
        return isBadVersion(n - 1) == False and isBadVersion(n) == True
        

if __name__ == "__main__":
    s = Solution()
    print(s.firstBadVersion(100))