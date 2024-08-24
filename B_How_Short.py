k, n, w = map(int, input().split())
total_cost = 0
for i in range(1, w+1):
    total_cost += i * k

borrow_amount = max(0, total_cost - n)

print(borrow_amount)