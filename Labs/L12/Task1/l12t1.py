dblVal = lambda x: 2*x
midChar = lambda phrase: phrase[(len(phrase)//2)-1]
isOddPositive = lambda val: (val >= 0 and not val % 2 == 0)
startVowel = lambda phrase: phrase[0].lower() in ['a', 'e', 'i', 'o', 'u']

print(f"dblVal(2): {dblVal(2)}")
print(f"midChar('Sentence!'): {midChar('Sentence!')}")
print(f"isOddPositive(5): {isOddPositive(5)}")
print(f"isOddPositive(-5): {isOddPositive(-5)}")
print(f"startVowel('Apple'): {startVowel('Apple')}")