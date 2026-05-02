class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next


#Сложность - О(n+k)k = номер элемента на котором начинается цикл, память - О(n)
def detect_cycle(head):
    # Защита от неправильного использования
    if not isinstance(head, ListNode):
        print("Переданный в фунцию объект не является связным списком")
        exit()


    address = []
    #Идем по связному списку пока он не закончится
    #Если в списке адресов(address) нет элемента из связного списка, кладем элемент в него,
    #если он уже есть - это начало цикла
    while head:
        if not head in address:
            address.append(head)
            head = head.next
        else:
            return head
    #Если не цикл - выводит False
    return False


# # Тест 1
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n1.next = n2;
# n2.next = n3;
# n3.next = n4
# n4.next = n2  # цикл: 4 → 2
# print(detect_cycle(n1).val)

# Тест 2
# n1 = 12
# print(detect_cycle(n1).val)

# Тест 3
# n1 = ListNode(1)
# n1.next = n2
# print(detect_cycle(n1))

# Тест 4
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# print(detect_cycle(n1))