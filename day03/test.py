# a = {1:"a", 2:["b", "c"]}

# a[2].append("r")
# print(a)


# def groupAnagrams(strs):
#     list_g = {}
#     for i in range(len(strs)):
#         for j in range(len(strs)):
#             list_g[i] = [strs[i]]
#             if sorted(strs[i]) == strs[j] and strs[j] not in list_g:
#                 list_g[i].append(strs[j])
    
#     return list_g

# print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
# print(ord("A"))
# from collections import defaultdict

# def groupAnagrams(strs):
#     anagram_map = defaultdict(list) 
    
#     for word in strs:
#         letter_list = [0] * 26
        
#         for letter in word:
#             letter_list[ord(letter) - ord("a")] += 1
#             print(f"this is letter_list {tuple(letter_list)}")
#         anagram_map[tuple(letter_list)].append(word)

#     return anagram_map

# print(groupAnagrams(strs=["act","pots","tops","cat","stop","hat"]))

sd = ["act","pots","tops","cat","stop","hat"]
dd = {2:4, 1:2}
# sd.append("germ")
# add_this = lambda x, y: x+y
li = sorted(dd.values())
print(li)
