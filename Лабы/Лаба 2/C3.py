class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def print_list(head):
    """Напечатать список"""
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    print(" → ".join(parts) + " → None")


def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next



#Сложноть по времени - О(n), по памяти - О(n)
def split_even_odd(head):
    #Защита от неправильного использования
    if not isinstance(head,ListNode):
        print("Переданный в фунцию объект не является связным списком")
        return None, None

    evens = ListNode() #Четные
    odds = ListNode() #Нечетные

    # Дубликаты для выведения в return
    evens_t = evens
    odds_t = odds

    while head:

        if head.val%2==0:
            head_temp = head #Сохраняем значение головы

            head = head.next #Перемещаем голову на след элемент
            head_temp.next = None #Убираем next чтобы записать только один элемент без тех на которые он ссылается
            evens.next = head_temp #Записываем его в список

            evens = evens.next #Двигаем голову нового списка
        else:
            #Все аналогично первому случаю
            head_temp = head

            head = head.next
            head_temp.next = None
            odds.next = head_temp

            odds = odds.next

    # Убираем первый ноль
    evens_t = evens_t.next
    odds_t = odds_t.next
    return evens_t, odds_t


# Тест 1
# head = build_list([1,2,3,4,5,6])
# evens, odds = split_even_odd(head)
# print_list(evens)  # 2 → 4 → 6 → None
# print_list(odds)   # 1 → 3 → 5 → None

# Тест 2
# head = build_list([1,1,1,1,1])
# evens, odds = split_even_odd(head)
# print_list(evens)  # 2 → 4 → 6 → None
# print_list(odds)   # 1 → 3 → 5 → None

# Тест 3
# head = build_list([2,2,2,2,2,2])
# evens, odds = split_even_odd(head)
# print_list(evens)  # 2 → 4 → 6 → None
# print_list(odds)   # 1 → 3 → 5 → None