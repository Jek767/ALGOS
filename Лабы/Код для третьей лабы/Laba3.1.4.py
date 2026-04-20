#451. Sort Characters By Frequency
# Функция создает словарь в который записываются {буква:количество}
# По этому словарю строится новая строка
# Каждый раз выбирается максимальный элемент он записывается в строку и удаляется
# Cложность - O(n)
def frequencySort(s: str) -> str:
    letters = {}
    if len(s)==0:
        return -1
    for i in s:
        if i in letters:
            letters[i]+=1
        else:
            letters.update({i:1})
    new_str = ''
    while letters:
        max_let = max(letters,key=letters.get)
        max_count = letters[max_let]
        new_str += max_count*max_let
        del letters[max_let]
    return new_str

str = 'RRTYYYYSLLLLLLLLLLLLL'
print(frequencySort(str))