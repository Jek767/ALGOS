class PolyNode:
    def __init__(self, coeff, exp, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next


#Сложность - О(n), дополнительная память - О(n)
def add_polynomials(p1, p2):
    if not isinstance(p1,PolyNode) or not isinstance(p2,PolyNode):
        print("Введенное значение не является связным списком")
        exit()

    new_polinom = PolyNode(0,0)#Новый полином

    temp = new_polinom #Переменная для вывода

    #Пока списки не закончились, идем по ним
    #Добавляем в новый список те элементы степень которых больше и двигаем голову того списка из которого взяли значение
    while p1 or p2:
        if p1 and p2:
            if p1.exp > p2.exp:

                #Создаем элемент нового полинома из элемента нужного списка
                new_polinom.next = PolyNode(p1.coeff,p1.exp)

                #Двигаем голову нового полинома
                new_polinom = new_polinom.next

                #Двигаем голову списка
                p1 = p1.next

            elif p1.exp < p2.exp:
                new_polinom.next = PolyNode(p2.coeff, p2.exp)

                new_polinom = new_polinom.next

                p2 = p2.next

            else:
                new_polinom.next = PolyNode(p2.coeff + p1.coeff, p1.exp)

                new_polinom = new_polinom.next

                p1 = p1.next
                p2 = p2.next
        elif p1:
            new_polinom.next = PolyNode(p1.coeff, p1.exp)

            new_polinom = new_polinom.next

            p1 = p1.next
        else:
            new_polinom.next = PolyNode(p2.coeff, p2.exp)

            new_polinom = new_polinom.next

            p2 = p2.next

    temp = temp.next#Убираем первое незначащие значение
    return temp

def print_poly(polinom) -> None:
    coeff = []
    exp = []
    #Создаем из полиновама массив
    while polinom:
        coeff.append(str(polinom.coeff))
        exp.append(str(polinom.exp))
        polinom = polinom.next
    #Выводим этот массив
    for i in range(0,len(coeff)):
        if i != len(coeff)-1:
            print(coeff[i] + "x" + "^" + exp[i], end=" + ")
        else:
            print(coeff[i] + "x" + "^" + exp[i])


# Тест 1
# p1 = PolyNode(3,4, PolyNode(2,2, PolyNode(1,0)))
# p2 = PolyNode(5,3, PolyNode(2,2, PolyNode(4,1)))
# result = add_polynomials(p1, p2)
# print_poly(result)  # 3x^4 + 5x^3 + 4x^2 + 4x^1 + 1x^0

# Тест 2
# p1 = []
# p2 = []
# result = add_polynomials(p1, p2)

# Тест 3
# p1 = PolyNode(3,4, PolyNode(2,2))
# p2 = PolyNode(5,3, PolyNode(2,2))
# result = add_polynomials(p1, p2)
# print_poly(result)  # 3x^4 + 5x^3 + 4x^2