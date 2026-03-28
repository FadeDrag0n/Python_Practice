n_antiques = int(input())
antiques_input = input().split()
antiques_list_sort = sorted(antiques_input, reverse=True)
count = 1000000
value = 0

for item in antiques_list_sort:
    if antiques_list_sort.count(item) < count:
        count = antiques_list_sort.count(item)
        value = item

print(int(value), int(count))
