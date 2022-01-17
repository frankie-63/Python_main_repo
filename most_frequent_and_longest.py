def mfl(text):
    list_from_text = list(text)
    if ',' in list_from_text:
        list_from_text.remove(',')
    if '.' in list_from_text:
        list_from_text.remove('.')
    if '\n' in list_from_text:
        list_from_text.remove('\n')
    list_from_text.append(' ')
    list_word = []
    list_global = []
    list_len = []
    count = 0
    for i in list_from_text:
        if i != ' ':
            list_word.append(i)
            count += 1
        else:
            str_in = ''.join(list_word)
            list_global.append(str_in)
            list_len.append(count)
            list_word.clear()
            count = 0
    max_len = max(list_len)
    k = 0
    dict_inner1 = dict()
    for j in list_len:
        dict_inner1[j] = list_global[k]
        k += 1
    max_len_word = dict_inner1[max_len]
    dict_inner2 = dict()
    for w in list_global:
        if w in dict_inner2:
            dict_inner2[w] += 1
        else:
            dict_inner2[w] = 1
    max_freq = max(list(dict_inner2.values()))
    most_freq_word = list(dict_inner2.keys())[list(dict_inner2.values()).index(max_freq)]
    print()
    print(f'The longest word is "{max_len_word}", its length is {max_len} literals')
    print()
    print(f'The most frequent word is "{most_freq_word}", its frequency is {max_freq} times')


text1 = str(input())
mfl(text1)
