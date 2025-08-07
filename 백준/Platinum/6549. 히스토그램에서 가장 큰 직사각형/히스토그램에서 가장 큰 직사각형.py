import sys

def largest_rectangle(hist):
    stack = []
    max_area = 0
    hist.append(0)
    for i, h in enumerate(hist):
        while stack and hist[stack[-1]] > h:
            height = hist[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

while True:
    line = sys.stdin.readline()
    if line.strip() == '0':
        break
    _, *heights = map(int, line.strip().split())
    print(largest_rectangle(heights))
