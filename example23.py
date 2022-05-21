# "12" = ["12", "21"]
# "123" = ["123", "213", "312", "132", "321", "231"]
# "ali" = ["ila", "ial", ...]
def n_binary(n, accumulated=''):
  if n == 0:
    return [accumulated]
  else:
    return (n_binary(n-1, accumulated+'0') +  
            n_binary(n-1, accumulated+'1')  )

def anagram_generator(user_str, anagrams = []):
    if len(user_str) == 1:
        return [user_str]
    else:
        for anagram in anagram_generator(user_str[1:]):
            for i in range(len(anagram)):
                anagrams.append(anagram[:i] + user_str[0] + anagram[i:])
        return anagrams

def insert(string, char):
    inserted = []
    for i in range(len(string) + 1):
        inserted.append(string[:i] + char + string[i:])
    return inserted

# print(anagram_generator("ali"))
print(insert("asd", "c"))