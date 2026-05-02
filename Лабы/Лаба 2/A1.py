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
    """Создать список из массива: build_list([1,2,3]) → 1→2→3→None"""
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

#Cложность - O(n), память - O(1)
def insert_sorted(head, val):
    #Если первого элемента нет - создаем его
    if not isinstance(head,ListNode):
        head = ListNode(val)
        return head

    #Если val меньше первого элемента - создаем новый элемент, адресуем к нему второй элемент ,
    # адресуем новый элемент к первому, и меняем значения первого элемента и нового
    # Было (1->2), поставили новый элемент перед первым(1->-1->2), поменяли значения местами(-1->1->2)
    if val<=head.val:
        new_node = ListNode(val)
        new_val = new_node.val

        new_node.next = head.next
        head.next = new_node

        new_node.val = head.val
        head.val = new_val
        return head

    temp = head
    #Пока val меньше чем temp.next.val, temp.next.val движется к концу
    while temp.next!=None and temp.next.val < val:
        temp = temp.next
    #Адресуем первое значение которое больше val к new_node.next
    #Адресуем следующее после temp к new_node
    #New_node между temp и тем значением которое больше val
    new_node = ListNode(val)
    new_node.next = temp.next
    temp.next = new_node
    return head



# Тест 1
head = build_list([1, 3, 5, 7])
head = insert_sorted(head, 4)
print_list(head)  # 1 → 3 → 4 → 5 → 7 → None

# Тест 2
# head = insert_sorted(None, 10)
# print_list(head)  # 10 → None

# Тест 3
# head = build_list([5, 10])
# head = insert_sorted(head, 1)
# print_list(head)  # 1 → 5 → 10 → None