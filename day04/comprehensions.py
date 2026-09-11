# ##############
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_no = [eve for eve in numbers if eve % 2 == 0]

# print(even_no)

# ###############
# names = ["tai", "john", "mary", "david"]
# upper_c = [words.upper for words in names]

# print(upper_c)

#################
# words = ["python", "django", "api", "database", "git"]
# word_len = [len(worl) for worl in words]

# print(word_len)

#################
# numbers = [1, 2, 3, 4, 5]
# result = [number**2 for number in numbers if number%2==0]

# print(result)

###################

# strs = ["Hello","World"]
# encrypted_words = {"encoded":""}
# for word in strs:
#     text = "-"
#     for letter in word:
#         text = text + "," + str(ord(letter))
#     encrypted_words["encoded"] += text
# print( chr(97))

# s = "-,72,101,108,108,111-,87,111,114,108,100"
# my_list = []
# for numbers in s.split("-"):
#     text = ""
#     for number in numbers.split(","):
#         number = int(number)
#         text = text + chr(number)
#     my_list.append(text)
# print(my_list)

def encode(strs):
    encrypted_words = {"encoded" :""}
    for word in strs:
        text = "-"
        for letter in word:
            text = text + "#" + str(ord(letter))
        encrypted_words["encoded"] += text
    return encrypted_words["encoded"]


def decode(s):
    my_list = []
    for numbers in s.split("-")[1:]:
        text = ""
        for number in numbers.split("#")[1:]:
            number = int(number)
            text = text + chr(number)
        my_list.append(text)
    return my_list

print("ans")
print(decode(encode(strs = ["Hello","World"])))

# listdd = "a,b,c,d"

# print(listdd.split(",")[1:])