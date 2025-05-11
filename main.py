'''
#1st
text = 'текст текст  текст'
non = []
for i in range(len(text)):
    if text[i] == ' ':
        cont = 1
        #print(i) -- check the space places
        try:
            while text[i+cont] == ' ':
                cont +=1
            non.append(cont)
        except:
            continue
print(max(non))

#2nd
text = 'ааабобус'
non = []
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        cont = 1
        #print(i) -- check the space places
        try:
            while text[i+cont] == text[i]:
                cont +=1
            non.append(cont)
        except:
            continue
print(max(non))


#3rd
test = ('абобус')


let = []
for num in range(26):
    let.append(chr(ord('A') + num))
for num in range(26):
    let.append(chr(ord('a') + num))
for num in range(32):
    let.append(chr(ord('А') + num))
for num in range(32):
    let.append(chr(ord('а') + num))


m_let = []
for i in let:
    if test.count(i) == 0:
        continue
    m_let.append(test.count(i))
print(len(m_let))

#4th
test = ('абобубс')


let = []
for num in range(26):
    let.append(chr(ord('A') + num))
for num in range(26):
    let.append(chr(ord('a') + num))
for num in range(32):
    let.append(chr(ord('А') + num))
for num in range(32):
    let.append(chr(ord('а') + num))


m_let = []
for i in let:
    if test.count(i) == 3:
        print(i)
        break
else:
    print('no one')


#5th
text_1 = 'абобубс'
text_2 = 'аааааа'
text_3 = 'оооуус'

let = []
for num in range(26):
    let.append(chr(ord('A') + num))
for num in range(26):
    let.append(chr(ord('a') + num))
for num in range(32):
    let.append(chr(ord('А') + num))
for num in range(32):
    let.append(chr(ord('а') + num))

set_1 = set()
for i in text_1:
    set_1.add(i)

set_2 = set()
for i in text_2:
    set_2.add(i)

set_3 = set()
for i in text_3:
    set_3.add(i)

for i in set_1:
    if i not in set_2 and i not in set_3:
        print(i)
for i in set_2:
    if i not in set_1 and i not in set_3:
        print(i)
for i in set_3:
    if i not in set_1 and i not in set_2:
        print(i)
'''

#6th
text = 'обратный порядок слов'
lst = text.split()
lst = sorted(lst, reverse=True)
print(*lst)


