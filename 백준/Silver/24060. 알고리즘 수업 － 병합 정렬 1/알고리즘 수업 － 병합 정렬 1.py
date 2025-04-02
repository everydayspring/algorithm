import sys
input = sys.stdin.read

sys.setrecursionlimit(10**6)

n, k, *nums = map(int, input().split())
a = nums
cnt = 0
result = -1

def merge_sort(p, r):
    global cnt, result
    if p < r:
        q = (p + r) // 2
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)

def merge(p, q, r):
    global cnt, result
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    while i <= q:
        tmp.append(a[i])
        i += 1
    while j <= r:
        tmp.append(a[j])
        j += 1

    for i in range(len(tmp)):
        a[p + i] = tmp[i]
        cnt += 1
        if cnt == k:
            result = tmp[i]

merge_sort(0, n - 1)
print(result)
