# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

def isAnagram(s,t):
    s_dict = {}
    t_dict = {}
    # for letterS, letterT in zip(s,t):
    #     s_dict[letterS] = 1 + s_dict.get(letterS, 0)
    #     t_dict[letterT] = 1 + s_dict.get(letterT, 0)
    
    for letter in s:
            s_dict[letter] = 1 + s_dict.get(letter, 0)
    for letter in t:
            t_dict[letter] = 1 + t_dict.get(letter, 0)
    
    return s_dict == t_dict


print(isAnagram("ssd", "dss"))