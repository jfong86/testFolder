quadString = input(str("Enter a number: "))
decNum = 0
for c in quadString:
    decNum = decNum * 4
    decNum = decNum + int(c)
print(decNum)
