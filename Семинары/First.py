#Задание 1
"""def Next_Smaler_Element(lst: list[int]) -> list:

    #Проход идет с конца
    #Для того чтобы в конце стека лежали наибольшие числа используется монотонный стек

    length = len(lst)
    out = [-1]*length
    stack = []
    for i in range(length-1,-1,-1):
        while (stack and stack[-1] >= lst[i]):
            stack.pop()
        if stack:
            out[i] = stack[-1]
        stack.append(lst[i])
    return out
#Выход: [2, 2, -1, 8, -1]
lst1=[4, 5, 2, 10, 8,0,1200,200,50]
print(Next_Smaler_Element(lst1))"""

#Задание 2
"""def delet_doubles(word: str) -> str:

    #Проходит по строке слева направо складывая буквы в стек
    #Если верхняя буква в стеке та же что и i-ая буква слова,
    #то верхняя буква стека удаляется а i-ая буква не попадает в стек
    #В конце выводим стек
    
    length = len(word)
    stack = ""
    for i in range(0,length):
        if stack and stack[-1] == word[i]:
            stack = stack[:-1]
        else:
            stack+=word[i]
    return stack
word1 = "111232334543"
print(delet_doubles(word1))"""

#Задание 3
"""def pop_push(pushed: list, popped: list)->bool:

    #Берем последний элемент pushed и первый элемент popped
    #Если они равны то удаляем последний элемент pushed и первый(нулевой) элемент popped
    #Повторяем пока списки не опустеют
    #Если списки пусты выводим True иначе - False
    #Если длинна списков не равна - выводим False
    
    if len(pushed) != len(popped):
        return False
    length = len(pushed)
    while pushed and pushed[-1] == popped[0]:
        pushed.pop()
        popped.pop(0)
    return not pushed
push1 = [1,2,3,4,5,6]
pop1 = [6,5,4,3,2,1]
print(pop_push(push1,pop1))"""

"""#Задание 4
def round(lst: list[int]) -> list:
    length = len(lst)
    out = [-1]*length
    stack = []

    for i in range(length-1,-1,-1):
        while (stack and stack[-1] <= lst[i]):
            stack.pop()
        if stack:
            out[i] = stack[-1]
        stack.append(lst[i])

    for i in range(length-1,-1,-1):
        while (stack and stack[-1] <= lst[i]):
            stack.pop()
        if stack:
            out[i] = stack[-1]
        stack.append(lst[i])
    return out

lst1=[1, 2, 1,3,2,5]
print(round(lst1))"""
