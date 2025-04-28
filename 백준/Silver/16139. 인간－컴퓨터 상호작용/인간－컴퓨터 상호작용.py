import sys
input = sys.stdin.read

data = input().split()
s = data[0]
q = int(data[1])
queries = data[2:]

prefix = [[0] * (len(s) + 1) for _ in range(26)]

for i in range(len(s)):
    for j in range(26):
        prefix[j][i + 1] = prefix[j][i]
    prefix[ord(s[i]) - ord('a')][i + 1] += 1

output = []
for i in range(q):
    alpha = queries[i * 3]
    l = int(queries[i * 3 + 1])
    r = int(queries[i * 3 + 2])
    idx = ord(alpha) - ord('a')
    output.append(str(prefix[idx][r + 1] - prefix[idx][l]))

print('\n'.join(output))
