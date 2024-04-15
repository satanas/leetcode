#   {
# {"songA", "3:29"}, 
# {"songB", "2:29"}, 
# {"songC", "3:31"}, 
# … 
# {"songN", "4:31"}
# }

# Only 2 songs that sum 7 minutes, if we don’t have a combination for 7 min, we return empty array

# Hashmap = {
#   “3:29” => [“songA”, “songH”],
#   “3:31” => [“songX”]
#   …
# }

# 7m - 3:29 = 3:31
# [songA, songX]

# Return []

def song_picker(songs):
    window_duration = 7 * 60 # seconds
    hashmap = {}

    for s in songs:
        duration = convert_to_seconds(s[1])
        hashmap[duration] = s[0]
        
        remaining = window_duration - duration
        if remaining in hashmap:
            return [hashmap[duration], hashmap[remaining]]

    # for s in songs:
    #     duration = convert_to_seconds(s[1])
    #     if duration in hashmap:
    #         hashmap[duration].append(s[0])
    #     else:
    #         hashmap[duration] = [s[0]]
    
    # for duration in hashmap:
    #     remaining = window_duration - duration
    #     if remaining in hashmap:
    #         return [hashmap[duration][0], hashmap[remaining][0]]

    return []


def convert_to_seconds(time):
    minutes = time.split(":")[0]
    return (int(minutes) * 60) + int(time.split(":")[1])

visited = {}
head_hashmap = {}

for s in songs:
    head = get_head(s)
    if s in head_hashmap:
        head_hashmap.append(s)
    else:
        head_hashmap = [s]
# head_hashmap = {
#     "River": ["Song A", "Song B"]

# }

# "Down By the River",
# "River of Dreams",


result = [song1]
tail = get_tail(song1)
while tail in head_hashmap:
    for s in head_hashmap[tail]:
        if not s in visited:
            result.append(s)
            visited[s] = True
            tail = get_tail(s)
    


return result
song1 => tail

if __name__ == "__main__":
    print(song_picker([["songA", "3:29"], ["songB", "2:29"], ["songC", "3:31"], ["songN", "4:31"]]))