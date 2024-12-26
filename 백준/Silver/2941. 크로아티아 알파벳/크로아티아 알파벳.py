croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for croatian in croatian_alphabets:
    word = word.replace(croatian, "*")

print(len(word))