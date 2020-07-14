s = input()
output = ""
i = 0
while i < len(s):
    if s[i] ==".":
        output = output + "0"
        i += 1
    else:
        if i != len(s) - 1 and s[i + 1] == ".":
            output += "1"
        else:
            output += "2"
        i += 2
    
print(output)