target = str(input())
i = 0
j = 0
sam = 0
sle = 0
word = str()
liss = []
while i < len(target):
    while target[i].isalpha():
        word += target[i]
        if i != len(target)-1:
            i += 1
        else: 
            break
    if word.isalpha() == False:
        i += 1
        continue
    word = word.lower()
    if len(liss) == 0:
            wordwnum = {
                "text": word,
                "amount": 0,
                "length": len(word)
            }
            liss.append(wordwnum)
    while j < len(liss):
        if liss[j]["text"] == word:
            liss[j]["amount"] += 1
            break
        if j == len(liss)-1:
            wordwnum = {
                "text": word,
                "amount": 0,
                "length": len(word)
            }
            liss.append(wordwnum)
        j += 1
    i += 1
    word = ""
    j = 0
i = 0
while i < len(liss):
    if liss[i]["amount"] > j:
        j = liss[i]["amount"]
        sam = i
    i += 1
i = 0
j = 0
while i < len(liss):
    if liss[i]["length"] > j:
        j = liss[i]["length"]
        sle = i
    i += 1
print("Most frequent word: \"" + str(liss[sam]["text"]) + "\", it was used " + str(liss[sam]["amount"]) + " times.")
print("The longest word: \"" + str(liss[sle]["text"]) + "\", it is " + str(liss[sle]["length"]) + " letters long.")