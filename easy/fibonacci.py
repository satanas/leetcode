class Solution2:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.memoize(n)

    def memoize(self, n):
        cache = {0: 0, 1: 1}
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]


if __name__ == "__main__":
    s = Solution()
    print(s.fib(2))
    print(s.fib(3))
    print(s.fib(4))
        