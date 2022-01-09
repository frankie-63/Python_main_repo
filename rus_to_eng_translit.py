# программа переводит строку на русском в транслит на английском
rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.'
eng_alphabet = 'a:b:v:g:d:e:yo:zh:z:i:j:k:l:m:n:o:p:r:s:t:u:f:kh:c:ch:sh:shch:":y:\':e:yu:ya: :,:.'
rus_al_list = list(rus_alphabet)
eng_al_list = eng_alphabet.split(':')
dict_translit = {}
# наполняем словарь:
j = 0
for i in rus_al_list:
    dict_translit[i] = eng_al_list[j]
    j += 1

# print(dict_translit)
print('Введите строку на русском языке: ')
string = str(input()).lower()
tr_list = []
for i in string:
    tr_list.append(dict_translit.get(i))


tr_string = ''.join(tr_list)


print(tr_string)
