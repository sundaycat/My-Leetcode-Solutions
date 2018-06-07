# implement it by linked list
class ListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue(object):

    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    def __len__(self):
        return self.__size

    def empty(self):
        return self.__size == 0

    def enqueue(self, value):

        new_item = ListNode(value)
        if self.empty():
            self.__head = new_item
            self.__tail = new_item
        else:
            self.__tail.next = new_item
            self.__tail = new_item

        self.__size += 1

    def dequeue(self):

        if self.empty():
            return None
        else:
            value = self.__head.value
            self.__head = self.__head.next

        self.__size -= 1
        return value


    def front(self):
        return self.head.value

q = Queue()
q.enqueue(1)
q.enqueue(2)
c = q.dequeue()
print(c)

