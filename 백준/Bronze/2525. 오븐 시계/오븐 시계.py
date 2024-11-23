h, m = map(int, input().split())
d = int(input())

h += int((m + d) / 60)
m = (m + d) % 60

if h > 23:
    h -= 24

print(h, m)