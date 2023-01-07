class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        temp = self.head
        pre = self.head
        if self.length == 0:
            return None

        while(temp.next is not None):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head == None
            self.tail == None

        return temp

    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_ll = LinkedList(4)
my_ll.append(5)
my_ll.append(12)
my_ll.pop()

print(my_ll.head.value)
