def count_unique_substrings(s):
    unique_substrings = set()
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            unique_substrings.add(s[i:j])
    
    return len(unique_substrings)

s = input().strip()

print(count_unique_substrings(s))
