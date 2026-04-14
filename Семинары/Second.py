#Задание 7.1
def threshold_nums(lst: list[float], k:int ,threshold: (int,float))->list[int]:
    #Функция проходит по первым К значениям списка и находит количество тех что больше threshold записывая его в  count
    #Далее если последний символ окна больше threshold то из count вычетается 1, значение удаляется из окна
    #Если следуйщее перед окном значение больше threshold от к count добавляется 1, значение добавляется в окно
    #При каждом сдвигании окна в список оге добавляется нынешнее count

    length = len(lst)

    if k>length:
        return -1

    window = lst[:k]
    count = 0

    for i in range(0,k):
        if window[i]>threshold:
            count+=1
    out = [count]

    for i in range(k,length):

        if window[0]>threshold:
            count-=1
        window.pop(0)

        if lst[i]>threshold:
            count+=1
        window.append(lst[i])

        out.append(count)

    return out

lst1 = [1, 5.6, 3, 7, 2.9999, 8, 4]
#print(threshold_nums(lst1,3,8))
#Задача 7.2
from collections import Counter
def anogram(main: str,sub: str):
    #Функция проходит по строке ища подстроку содержащую все буквы подстроки sub
    #Когда такая строка находится функция сужает её, сдвигая левый край окна и проверяет вышел ли за пределы окна один из символов строки sub
    #Если он вышел - поиск строки содержащей все символы строки sub продолжается: окно расширяется направо пока не будет выполнено условие
    #Размеры и координаты всех найденых окон сравниваются и выводится самое маленькое

    if len(main)<len(sub):
        return -1

    need = Counter(sub)
    missing = len(sub)
    left = 0
    best = (float('inf'),0,0)

    for right,char in enumerate(main):
        if need[char] > 0:
            missing -=1
        need[char] -= 1

        while missing == 0:
            win_len = right - left + 1
            if win_len < best[0]:
                best = (win_len,left,right)

            need[main[left]] += 1
            if need[main[left]]>0:
                missing += 1
            left += 1
    return "" if best[0] == float('inf') else main[best[1]: best[2] + 1]

#print(anogram("ADOBECODEBANC", "ABCD"))

#Задача 7.3
def polindrom(string:str)->bool:
    #Функция получает на вход строку переводит её в нижний регистр
    #Проходит по строке пропуская все символы кроме букв(русских,английских) и цифр
    #Если буквы расположеные на равном расстоянии от центра строки не равны хотя бы раз выдает False иначе True

    if not str:
        return False

    left = 0
    right = len(string)-1
    nums = '1234567890'
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
    string = string.lower()

    while (left<right):

        if (string[left] in nums or string[left] in letters):

            if(string[right] in nums or string[right] in letters):

                if(string[left] == string[right]):

                    left += 1
                    right -= 1

                else: return False

            else: right -= 1

        else: left += 1

    return True

#print(polindrom("Amanaplaanalpanama"))