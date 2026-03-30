from collections import Counter

# def word_counter(text: str) -> dict:
#     words = (''.join(d for d in text if d.isalpha() or d.isspace())).split()
#     res = dict()
#     for item in words:
#         if item.lower() in res:
#             res[item.lower()] += 1
#         else:
#             res[item.lower()] = 1
#     return res

def word_counter(text: str) -> dict:
    words = ''.join(d for d in text if d.isalpha() or d.isspace()).split()
    return dict(Counter(w.lower() for w in words))

print(word_counter("Hello world! Hello, Python."))
print(word_counter(input("Enter a text: ")))