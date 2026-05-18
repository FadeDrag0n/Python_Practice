s1 = 'heart'
s2 = 'earth'

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

print(is_anagram(s1, s2))