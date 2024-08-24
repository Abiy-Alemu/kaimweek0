t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total_sum = sum(a)
    max_sum = float('-inf')

    for i in range(n - 1):
        if a[i] == a[i + 1]:
            if a[i] == 1:
                max_sum = max(max_sum, total_sum - 4)
            else:
                max_sum = max(max_sum, total_sum + 4)
        else:
            max_sum = max(max_sum, total_sum)

    print(max_sum)