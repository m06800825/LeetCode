start1 = 1
start2 = 1
for _ in range(2, n+1):
    cur = start1 + start2
    start2 = start1
    start1 = cur

return start1