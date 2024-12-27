def is_group_word(word):
    seen = set()
    prev_char = ''
    for char in word:
        if char != prev_char:
            if char in seen:
                return False
            seen.add(char)
        prev_char = char
    return True

N = int(input())
words = [input().strip() for _ in range(N)]
group_word_count = sum(1 for word in words if is_group_word(word))
print(group_word_count)