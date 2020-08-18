class Solution:
    def groupAnagrams(self, strs):
        result = []
        hashmap = {}
        index = -1

        for elem in strs: # o (n)
            sorted_elem = tuple(sorted(elem)) # o(n * log m)
            if sorted_elem in hashmap:
                index = hashmap[sorted_elem]
            else:
                result.append([])
                index = len(result) - 1
                hashmap[sorted_elem] = index
                
            result[index].append(elem)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))