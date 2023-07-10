def processPlainText(text):
    newText = text.lower()
    newText = newText.replace("j", "i")
    newText = newText.replace(" ", "")
    if len(newText) % 2 != 0:
        newText = newText + 'x'
    i = 0
    while i < len(newText):
        if len(newText) % 2 != 0:
            newText = newText + 'x'
        ch = newText[i:i + 2]
        if ch[0] == ch[1]:
            newText = newText[:i + 1] + 'x' + newText[i + 1:]
        newText = newText.replace("xx", "x")
        i += 2
    newText = newText.replace("xx", "x")
    if len(newText) % 2 != 0:
        newText = newText[:-1]
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


def find_index_2d(lst, value):
    for i, row in enumerate(lst):
        for j, item in enumerate(row):
            if item == value:
                return i, j
    return -1, -1


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
cipher_text = ""
i = 0
while i < len(processedText):
    ch = processedText[i:i + 2]
    print(ch)
    row_index1, col_index1 = find_index_2d(matrix_2d, ch[0])
    row_index2, col_index2 = find_index_2d(matrix_2d, ch[1])
    print("ch1 ",row_index1, col_index1)
    print("ch2 ",row_index2, col_index2)
    if row_index1 == row_index2:
        col_index1 = (col_index1 + 1) % 5
        col_index2 = (col_index2 + 1) % 5
        # print("new 1 ", row_index1, col_index1)
        # print("new 2 ", row_index2, col_index2)
        cipher_text = cipher_text + matrix_2d[row_index1][col_index1]
        cipher_text = cipher_text + matrix_2d[row_index2][col_index2]
    elif col_index1 == col_index2:
        row_index1 = (row_index1 + 1) % 5
        row_index2 = (row_index2 + 1) % 5
        cipher_text = cipher_text + matrix_2d[row_index1][col_index1]
        cipher_text = cipher_text + matrix_2d[row_index2][col_index2]
    else:
        cipher_text = cipher_text + matrix_2d[row_index1][col_index2]
        cipher_text = cipher_text + matrix_2d[row_index2][col_index1]
    i += 2
print(cipher_text)

alpha2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
userCipher = input("Enter Cipher Text :")
userKey = input("Enter cipher Key  :")
userKey = processCipherText(userKey)
print("userCipher - ", userCipher)
print("userKey - ", userKey)
print("alpha - ", alpha2)
cipher_matrixList = processAlpha(alpha2, userKey)

cipher_matrix_2d = []
row = []
count = 0

for char in cipher_matrixList:
    row.append(char)
    count += 1

    if count == 5:
        cipher_matrix_2d.append(row)
        row = []
        count = 0
print(cipher_matrix_2d)
plain_text = ""
j = 0
while j < len(userCipher):
    ch = userCipher[i:i + 2]
    print(ch)
    row_index1, col_index1 = find_index_2d(cipher_matrix_2d, ch[0])
    row_index2, col_index2 = find_index_2d(cipher_matrix_2d, ch[1])
    print("ch1 ",row_index1, col_index1)
    print("ch2 ",row_index2, col_index2)
    if row_index1 == row_index2:
        col_index1 = (col_index1 - 1) % 5
        col_index2 = (col_index2 - 1) % 5
        # print("new 1 ", row_index1, col_index1)
        # print("new 2 ", row_index2, col_index2)
        plain_text = plain_text + cipher_matrix_2d[row_index1][col_index1]
        plain_text = plain_text + cipher_matrix_2d[row_index2][col_index2]
    elif col_index1 == col_index2:
        row_index1 = (row_index1 - 1) % 5
        row_index2 = (row_index2 - 1) % 5
        plain_text = plain_text + cipher_matrix_2d[row_index1][col_index1]
        plain_text = plain_text + cipher_matrix_2d[row_index2][col_index2]
    else:
        plain_text = plain_text + cipher_matrix_2d[row_index1][col_index2]
        plain_text = plain_text + cipher_matrix_2d[row_index2][col_index1]
    j += 2
print(plain_text)
