# Hash map approach
# .insert("apple")
# {
#     "apple": {
#         "": "apple"
#     }
# }

# .insert("app")
# {
#     "app": {
#         "le": {
#             "": "apple"
#         }
#         "": "app"
#     }
# }

# .insert("application")
# {
#     "app": {
#         "l": {
#             "e": {
#                 "": "apple",
#             }
#             "ication": {
#                 "": "application"
#             }
#         }
#         "": "app"
#     }
# }

# .insert("a")
# {
#     "a": {
#         "": "a"
#         "pp": {
#             "l": {
#                 "e": {
#                     "": "apple",
#                 }
#                 "ication": {
#                     "": "application"
#                 }
#             }
#             "": "app"
#         }
#     }
# }

# .insert(str)
# we iterate the chars of each key while they match with str
# once they don't match, we save the current value of the matching key and create a new hashmap with the current matching
# then put the remainder (the part that doesn't match as key) as a new object with the previous value
# and insert the 

# .search(str)
# for each key, we check if the string contains the key
# if it does, then we remove the key from the string and repeat the process until we remain with "" and find that in the hash map

# .startsWith(str)
# we start iterating the keys while they match str. If we find a sequence of keys that match str then return true, otherwise false.

# ====== After looking at solution
# The implementation is via a tree structure where each node has links to letters of the word, starting from the root.


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.links = []
        self.end = False

    def contains(self, char):
        print(f">> searching for {char}")
        for node in self.links:
            if node.char == char:
                print(f"{char} found")
                return True
        return False

    def put(self, char):
        print(f"++ inserting {char}")
        self.links.append(TrieNode(char))

    def get(self, char):
        for node in self.links:
            if node.char == char:
                return node
        return None

    def is_end(self):
        print(f"?? is end? {len(self.links) == 0 or self.end}")
        return len(self.links) == 0 or self.end

    def set_as_end(self):
        self.end = True


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for letter in word:
            if not curr.contains(letter):
                curr.put(letter)
            
            curr = curr.get(letter)
        curr.set_as_end()

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.__find_node(word)
        return node is not None and node.is_end()
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.__find_node(prefix)
        return node is not None

    def __find_node(self, word):
        curr = self.root
        for i in range(len(word)):
            letter = word[i]
            if curr.contains(letter):
                curr = curr.get(letter)
            else:
                return None
        return curr

if __name__ == "__main__":
    obj = Trie()
    obj.insert("apple")
    result = obj.search("apple")
    print(f"search 'apple' {result}")
    result = obj.search("app")
    print(f"search 'app' {result}")
    result = obj.startsWith("app")
    print(f"startsWith 'app' {result}")
    obj.insert("app")
    result = obj.search("app")
    print(f"search 'app' {result}")