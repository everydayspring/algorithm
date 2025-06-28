import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
w = int(input())
events = [tuple(map(int, input().split())) for _ in range(w)]
dp = [[-1] * (w+1) for _ in range(w+1)]

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve(a, b):
    if a == w or b == w:
        return 0
    if dp[a][b] != -1:
        return dp[a][b]
    next_event = max(a, b) + 1
    if a == 0:
        car1_pos = (1, 1)
    else:
        car1_pos = events[a-1]
    if b == 0:
        car2_pos = (n, n)
    else:
        car2_pos = events[b-1]
    go_car1 = solve(next_event, b) + dist(car1_pos, events[next_event-1])
    go_car2 = solve(a, next_event) + dist(car2_pos, events[next_event-1])
    dp[a][b] = min(go_car1, go_car2)
    return dp[a][b]

def trace(a, b):
    if a == w or b == w:
        return
    next_event = max(a, b) + 1
    if a == 0:
        car1_pos = (1, 1)
    else:
        car1_pos = events[a-1]
    if b == 0:
        car2_pos = (n, n)
    else:
        car2_pos = events[b-1]
    go_car1 = solve(next_event, b) + dist(car1_pos, events[next_event-1])
    go_car2 = solve(a, next_event) + dist(car2_pos, events[next_event-1])
    if go_car1 < go_car2:
        print(1)
        trace(next_event, b)
    else:
        print(2)
        trace(a, next_event)

print(solve(0, 0))
trace(0, 0)
