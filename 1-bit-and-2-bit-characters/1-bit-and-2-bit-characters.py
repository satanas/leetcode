class Solution:
    availableChars = [[0], [1, 0], [1, 1]]

    def isOneBitCharacter(self, bits):
        lastBit = self.getChars(bits)[-1]
        return lastBit == [0]

    def getChars(self, bits):
        chars = []
        acc = []
        for x in bits:
            acc.append(x)
            if acc in self.availableChars:
                chars.append(acc[:])
                acc.clear()
            elif [x] in self.availableChars:
                chars.append([x])
        return chars


if __name__ == "__main__":
    s = Solution()
    print(s.isOneBitCharacter([1, 0, 0]))
    print(s.isOneBitCharacter([1, 1, 1, 0]))
    print(s.isOneBitCharacter([0, 0]))
        