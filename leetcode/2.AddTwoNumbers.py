from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    # 1. Zmienić liścia odwróconego na liczbę (np. [2,4,3]=342)
    # 2. Powtórz dla drugiego liścia
    # 3. Dodaj obydwie liczby
    # 4. Zmień z powrotem z liczby na liścia odwróconego
    def get_reversed_num(node):
        current = node
        num = ""
        while current is not None:
            num += str(current.val)
            current = current.next
        num = num[::-1]
        return num

    num1 = get_reversed_num(l1)
    num2 = get_reversed_num(l2)
    res = int(num1) + int(num2)

    def num_to_reversed_linked_list(num):
        num = str(num)[::-1]
        head = ListNode(int(num[0]))
        current = head
        for digit in num[1:]:
            current.next = ListNode(int(digit))
            current = current.next
        return head

    result = num_to_reversed_linked_list(res)
    return result


node1 = ListNode(2, 4)
node2 = ListNode(4, 3)
node3 = ListNode(3)

node4 = ListNode(5, 6)
node5 = ListNode(6, 4)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

node1.next = node2
node2.next = node3

l1 = node1
l2 = node4


# input: l1 = [2,4,3], l2 = [5,6,4]
# output = [7,0,8]

print(addTwoNumbers(l1, l2), " output: [7,0,8]")
