import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

nums.sort()
count = Counter(nums)
mode_freq = count.most_common()

max_freq = mode_freq[0][1]
modes = [num for num, freq in mode_freq if freq == max_freq]
modes.sort()

print(round(sum(nums) / n))
print(nums[n // 2])
print(modes[1] if len(modes) > 1 else modes[0])
print(nums[-1] - nums[0])
