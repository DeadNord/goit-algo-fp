class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "->".join(values)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            self._insert_sorted(sorted_list, current)
            current = next_node
        self.head = sorted_list.head

    def _insert_sorted(self, sorted_list, node):
        if sorted_list.head is None or node.value < sorted_list.head.value:
            node.next = sorted_list.head
            sorted_list.head = node
        else:
            current = sorted_list.head
            while current.next and current.next.value < node.value:
                current = current.next
            node.next = current.next
            current.next = node

    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy
        current1 = list1.head
        current2 = list2.head
        while current1 and current2:
            if current1.value < current2.value:
                tail.next, current1 = current1, current1.next
            else:
                tail.next, current2 = current2, current2.next
            tail = tail.next
        tail.next = current1 or current2
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


if __name__ == "__main__":
    list1 = LinkedList()
    for value in [3, 1, 4]:
        list1.append(value)
    list1.insertion_sort()

    list2 = LinkedList()
    for value in [2, 5, 6]:
        list2.append(value)
    list2.insertion_sort()

    print("List 1:", list1)
    print("List 2:", list2)

    merged_list = LinkedList.merge_sorted_lists(list1, list2)
    print("Merged List:", merged_list)
