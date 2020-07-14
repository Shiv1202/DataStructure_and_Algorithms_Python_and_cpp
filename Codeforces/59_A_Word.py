word = input()
up = low = 0
for i in word:
    if i.islower():
        low += 1
    else:
        up += 1
if low >= up:
    print(word.lower())
else:
    print(word.upper())
