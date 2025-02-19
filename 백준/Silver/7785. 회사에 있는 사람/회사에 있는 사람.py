import sys

n = int(sys.stdin.readline().strip())
log = {}

for _ in range(n):
    name, action = sys.stdin.readline().split()
    if action == "enter":
        log[name] = True
    elif name in log:
        del log[name]

sys.stdout.write("\n".join(sorted(log.keys(), reverse=True)) + "\n")
