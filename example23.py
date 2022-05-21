# "12" = ["12", "21"]
# "123" = ["123", "213", "312", "132", "321", "231"]
# "ali" = ["ila", "ial", ...]
def anagram_generator(user_str):
    if len(user_str) == 1:
        return [user_str]
    else:
        anagrams = []
        for anagram in anagram_generator(user_str[1:]):
            anagrams += insert(anagram, user_str[0])
        return anagrams

def insert(string, char):
    inserted = []
    for i in range(len(string) + 1):
        inserted.append(string[:i] + char + string[i:])
    return inserted

print(anagram_generator("ali"))

def anagrams_of(s):
    if len(s) <= 1:
        return [s]
    else:
        anagrams = []
        for anagram in anagrams_of(s[:-1]):
            for i in range(len(s)):
                anagrams.append(anagram[i:] + s[-1] + anagram[:i])
        return anagrams

print(anagrams_of("alijaadx"))