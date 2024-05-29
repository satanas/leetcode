# Assume that HotelCo decided to enable search on user reviews. In order to
# make the search better, you need to tag specific words in the review.

# The search team has given you a bunch of tags which are key value pairs.
# The keys denote words which may or may not present in a review and the value
# corresponds to the search metadata tag. Your task is to prepend the metadata
# tag and highlight the specific review word in brackets.

# Input:

# Review:
# "I visited San Francisco for work and stayed at HotelCo.
# I really loved the city and the home where I stayed."

# "Francisco visited San Francisco for work and stayed at HotelCo.
# He really loved the city and the home where he stayed."

# Tags: {
# "HotelCo": "business",
# "san francisco": "city",
# "Francisco": "name"
# }

# Output:
# "I visited [city]{San Francisco} for work and stayed at [business]{HotelCo}.
# I really loved the city and the home where I stayed."

# "[name]{Francisco} visited [city]{San Francisco} for work and stayed at [business]{HotelCo}.
# I really loved the city and the home where I stayed."

tags = {
    "HotelCo": "business",
    "san francisco": "city",
    "Francisco": "name"
}

class TrieNode:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root

        for char in word.lower():
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.is_word = True

    def partial_search(self, word):
        curr = self.root
        i = 0
        while i < len(word):
            char = word[i].lower()
            if char in curr.children:
                curr = curr.children[char]
                i += 1
            else:
                return None
        return curr

# Trie approach
def tag_speficic_word(review, tags):
    trie = Trie()
    lowercase_tags = {}
    for tag in tags:
        trie.add(tag)
        lowercase_tags[tag.lower()] = tags[tag]

    start = 0
    end = 1
    parsed_review = ""
    while end < len(review) + 1:
        node = trie.partial_search(review[start:end])
        if node:
            if node.is_word:
                parsed_review += "[" + lowercase_tags[review[start:end].lower()] + "]{" + review[start:end] + "}"
                start = end
            end += 1
        else:
            parsed_review += review[start:end]
            start = end
            end += 1
    return parsed_review


def tag_speficic_word_iteration(review, tags):
    lowercase_review = review.lower()
    lowercase_tags = {}
    for key in tags:
        lowercase_tags[key.lower()] = tags[key]
    sorted_tags = sorted([tag.lower() for tag in tags])[::-1]
    current_tags = set([])

    for tag in sorted_tags:
        for index in find_all(lowercase_review, tag):
            if is_tagged(current_tags, index):
                # print("word %s already tagged" % (lowercase_review[index:index + len(tag)]))
                continue
            current_tags.add((index, index + len(tag), lowercase_tags[tag]))

    sorted_current_tags = sorted(current_tags)
    i = 0
    parsed_review = ""
    while i < len(review):
        if len(sorted_current_tags) > 0 and i == sorted_current_tags[0][0]:
            curr_tag = sorted_current_tags[0]
            parsed_review += "[" + curr_tag[2] + "]{" + review[curr_tag[0]: curr_tag[1]] + "}"
            i += curr_tag[1] - curr_tag[0]
            sorted_current_tags.pop(0)
        else:
            parsed_review += review[i]
            i += 1
    
    return parsed_review

def find_all(review, tag):
    index = 0
    result = []
    while index < len(review):
        index = review.find(tag, index)
        if index < 0:
            break
        result.append(index)
        index += 1
    return result

def is_tagged(current_tags, index):
    for curr in current_tags:
        if index >= curr[0] and index <= curr[1]:
            return True
    return False



# print(tag_speficic_word("""I visited San Francisco for work and stayed at HotelCo.
# I really loved the city and the home where I stayed.""", tags))

# print(tag_speficic_word("""Francisco visited San Francisco for work and stayed at HotelCo.
# He really loved the city and the home where he stayed.""", tags))

# print(tag_speficic_word("""I visited San Francisco for work and stayed at HotelCo, San Francisco.
# I really loved San Francisco and the home where I stayed.""", tags))



more_tags = {
    "san": "person",
    "francisco": "person",
    "san francisco": "city",
    "HotelCo": "business",
    "city": "location",
}

print(tag_speficic_word_iteration("""I traveled to San Francisco for work and stayed at HotelCo.
I really loved the city and the home where I stayed.
I stayed with San and Francisco.
They both were really good hosts and san’s hospitality was outstanding.""", more_tags))
