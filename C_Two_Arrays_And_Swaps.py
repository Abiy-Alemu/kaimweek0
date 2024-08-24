t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    i = 0
    j = 0

    while k > 0 and i < n and j < n:
        if a[i] < b[j]:
            a[i] = b[j]
            k -= 1
            i += 1
            j += 1
        else:
            break

    print(sum(a))