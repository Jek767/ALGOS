class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next



def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next



def is_palindrome(head) -> bool:
    if not isinstance(head, ListNode):
        return True
    slow, fast = head, head
    #Идем по списку пока не найдем середину
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    #Когда нашли - переворачиваем список начиная с середины
    newHead = reverse_list(slow.next)

    #Проверяем что все элементы первой половины равны соответсвующим элеметам перевернутой второй пловины
    while head and newHead:
        if head.val == newHead.val:
            head = head.next
            newHead = newHead.next
        else:
            return False
    return True

# Тестs
# print(is_palindrome(build_list([1,2,3,2,1])))    # True
# print(is_palindrome(build_list([1, 2, 3])))          # False
# print(is_palindrome(build_list([1, 1])))             # True