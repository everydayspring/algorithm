import sys, random

def ask(qtype, x):
    print(f"? {qtype} {x}", flush=True)
    r = sys.stdin.readline()
    if not r:
        sys.exit(0)
    r = r.strip()
    return r == "1"

def solve_case():
    nums = list(range(1, 10001))
    random.shuffle(nums)
    A = None
    askedA = set()
    for i in range(9999):
        x = nums[i]
        askedA.add(x)
        if ask("A", x):
            A = x
            break
    if A is None:
        for x in nums:
            if x not in askedA:
                A = x
                break

    nums = list(range(1, 10001))
    random.shuffle(nums)
    B = None
    askedB = set()
    for i in range(9998):
        x = nums[i]
        askedB.add(x)
        if ask("B", x):
            B = x
            break
    if B is None:
        remain = [x for x in nums if x not in askedB]
        B = random.choice(remain)

    print(f"! {A+B}", flush=True)

def main():
    for _ in range(10):
        solve_case()

if __name__ == "__main__":
    main()
