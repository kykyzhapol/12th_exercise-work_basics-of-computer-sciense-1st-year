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

#6th
text = 'обратный порядок слов'
lst = text.split()
lst.reverse()
print(*lst)


#7th
text = 'обратный порядок слов'
lst = text.split()
len_lst = []
for i in lst:
    len_lst.append(len(i))
print(min(len_lst))


#9th
text = 'слов обратный слов порядок'
lst = text.split()

short_lst = lst[1:]
b_count = 0
for i in lst:
    for k in short_lst:
        if i == k:
            print(i)
            b_count = 1
            break
    else:
        short_lst = short_lst[1:]
    if b_count == 1:
        break


#8th
text = 'обратный слов порядок'
lst = text.split()
lst = sorted(lst, reverse=True)
print(*lst)


#10th
text = 'обратный обратный порядок слов'
lst = text.split()
def fst(x):
    if x == lst[0]:
        return False
    return True

def rep(x):
    ls = x.split()
    st = set(ls)
    if len(ls) == len(st):
        return True
    return False

for i in lst[1:]:
    if rep(i) + fst(i) == 2:
        print(i)


#11th
# Петя - нечетный, Вася - четный
cities = 'Москва Архангельск Киров'
lst = cities.split()


for i in range(len(lst)-1):
    if lst[i][-1] == lst[i+1][0].lower():
        pass
    else:
        if (i+1)%2 == 0:
            print('Петя проиграл')
        else:
            print('Вася проиграл')
        break
else:
    if (len(lst)) % 2 == 1:
        print('Петя выйграл')
    else:
        print('Вася выйграл')

#12th
import keyword

#Как известно, имя в языке Python может содержать только латинские символы,
#цифры и знак подчеркивания "_". При этом, имя не может начинаться с цифры и не может быть ключевым словом.
#Напишите программу, которая проверяет введенную строку, может ли она быть именем в языке Python.
#12th
name = 'отдмща'

def consist(x):
    let = []
    for num in range(26):
        let.append(chr(ord('A') + num))
    for num in range(26):
        let.append(chr(ord('a') + num))
    for i in x:
        if (i not in let) and (i not in str([x for x in range(10)])) and (i != '_'):
            return False
    return True

def start(x):
    if x[0] in str([x for x in range(10)]):
        return False
    return True


def key(x):
    return keyword.iskeyword(x)


if key(name)+start(name)+consist(name) == 2:
    print('Может')
else:
    print('Не может')


#13th

#Дима часто пользуется общественным транспортом и всегда проверяет номер билета,
#является ли он "счастливым". Счастливым считается билет, имеющий в номере четное количество цифр.
#Причем, сумма цифр первой половины номера равна сумме цифр второй половины.
#Программа на вход получает последовательность номеров билетов.
#Ввод номеров должен завершить тогда, когда будет введен "счастливый" билет.
#Программа должна вывести его порядковый номер. Счет начинается с 1.


def two(x):
    if len(x)%2 == 0:
        return True
    return False

def sum_hf(x):
    half = len(x) // 2
    numbers = [int(i) for i in x]
    return sum(numbers[:half]) == sum(numbers[half:])
entr = '0'
lst = []
while two(entr)+sum_hf(entr) != 2:
    entr = input('-->')
    lst.append(entr)
else:
    print(len(lst))


#14th
name = input('Введите слово -->')
pron = input('Введите подсказку -->')
name = name.split()
print('\n'*25)
print(*name, sep='')
print(pron)
what = list(len(name)*'*')
print(*what, sep='')

cnt = 0
guess_count = 0
while cnt != 9 or guess_count != len(name):
    choose = input('Буква или слово (0 - буква, 1 - слово)')
    if choose == 0:
        let = input()
        for i in range(len(name)):
            if name[i] == let:
                what[i] = name[i]
                guess_count += 1
    else:
        let = input()
        if let == name:
            print('победа')
        else:
            print('не угадал')
    cnt+=1
    if '*' not in what:
        print('ты выйграл')
        break
else:
    print('проиграл')
'''

