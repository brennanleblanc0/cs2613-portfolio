dblVal = lambda x: 2*x
midChar = lambda phrase: phrase[len(phrase)//2]
isOddPositive = lambda val: (val >= 0 and not val % 2 == 0)
startVowel = lambda phrase: phrase[0].lower() in ['a', 'e', 'i', 'o', 'u']

mult = [8,10,7.5]
mid = ["Hello", "CompSci2613", "Lab-12"]
odd = [-15, -4, 0, 4, 23, 64, 101, 104, 123]
vowel = ["alice", "bob", "Carl", "daisy", "Earl"]

print(f"Q1: {list(map(dblVal, mult))}")
print(f"Q2: {list(map(midChar, mid))}")
resOdd = list(map(isOddPositive, odd))
outOdd = []
i = 0
for e in resOdd:
    if (e):
        outOdd.append(odd[i])
    i += 1
print(f"Q3: {outOdd}")
resVow = list(map(startVowel, vowel))
outVow = []
i = 0
for e in resVow:
    if (e):
        outVow.append(vowel[i])
    i += 1
print(f"Q4: {outVow}")