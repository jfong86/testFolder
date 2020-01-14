octString = input(str("Enter a number: "))
decNum = 0
for c in octString:
    decNum = decNum * 8
    decNum = decNum + int(c)
print(decNum)
