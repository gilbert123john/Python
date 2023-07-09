def processPlainText(text):
    newText = text.lower()
    newText = newText.replace("j", "i")
    newText = newText.replace(" ", "")
    i = 0
    while i < len(newText):
        ch = newText[i:i + 2]
        if ch[0] == ch[1]:
            newText = newText[:i + 1] + 'x' + newText[i + 1:]
        i += 2
    return newText


def processCipherText(text):
    newText = text.lower()
    newText = newText.replace("j", "i")
    newText = newText.replace(" ", "")
    p = ""
    for char in newText:
        if char not in p:
            p = p + char
    return p


def processAlpha(alp, cKey):
    for x in range(len(cKey)):
        ch = cKey[x]
        alp.remove(ch)
    cipher_list = []
    for ch1 in cKey:
        cipher_list.append(ch1)
    matrix_list = cipher_list + alp
    return matrix_list


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
plainText = input("Enter plain Text :")
cipherKey = input("Enter cipher Key  :")
processedText = processPlainText(plainText)
cipherKey = processCipherText(cipherKey)
print("plainText - ", plainText)
print("processedText - ", processedText)
print("cipherKey - ", cipherKey)
matrixList = processAlpha(alpha, cipherKey)

matrix_2d = []
row = []
count = 0

for char in matrixList:
    row.append(char)
    count += 1

    if count == 5:
        matrix_2d.append(row)
        row = []
        count = 0
print(matrix_2d)
