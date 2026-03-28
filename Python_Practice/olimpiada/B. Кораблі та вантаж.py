def find_max_sum(d, l, n):
    max_sum = 0

    for i in range(l):
        for j in range(i + 1, l):
            s = n[i] + n[j]
            if s % d == 0:
                if max_sum is None or max_sum < s:
                    max_sum = s
    return max_sum


d1 = int(input())
l1 = int(input())
n1 = tuple(map(int, input().split()))
print(find_max_sum(d1, l1, n1))