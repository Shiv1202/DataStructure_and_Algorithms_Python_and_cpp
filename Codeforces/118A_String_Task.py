input_str = input()
x = list(input_str.lower())
vowels = ['u', 'i', 'a', 'o', 'e', 'y']
output = []
for char in x:
    if char not in vowels:
        output.append(char)
# x = [char for char in x if char != "u"]
print('.' + ".".join(output))