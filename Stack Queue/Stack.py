class Stack(object):

    def __init__(self):
        self.__item = []

    def __len__(self):
        return len(self.__item)

    def empty(self):
        return len(self.__item) == 0

    # end of list is the top of the stack
    def push(self, value):
        self.__item.append(value)

    # pop out the 1st element of array
    def pop(self):
        return self.__item.pop()

    def top(self):
        return self.__item[-1]


class MinStack(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__min = Stack()

    def push(self, value):
        Stack.push(self, value)
        if self.__min.empty() or value < self.__min.top():
            self.__min.push(value)

    def pop(self):
        value = Stack.pop(self)
        if value == self.__min.top():
            self.__min.pop()

        return value

    def get_min(self):
        return self.__min.top()


# Implement MinQueue with two MinStack
class MinQueue(object):

    def __init__(self):
        # stack in for enqueue
        self.__in = MinStack()

        # stack out for dequeue
        self.__out = MinStack()

    def size(self):
        return len(self.__in) + len(self.__out)

    def empty(self):
        return self.size() == 0

    def enqueue(self, value):
        self.__in.push(value)

    def dequeue(self):
        # if dequeue stack is empty, then push all the elements from enqueue
        # to dequeue
        if self.__out.empty():
            while not self.__in.empty():
                item = self.__in.pop()
                self.__out.push(item)

        return self.__out.pop()

    def front(self):
        return self.__out.top()

    def get_min(self):

        if self.empty():
            return None

        min_in = self.__in.get_min() if not self.__in.empty() else float('inf')
        min_out = self.__out.get_min() if not self.__out.empty() else float('inf')

        return min(min_in, min_out)


min_q = MinQueue()
min_q.enqueue(5)
min_q.enqueue(3)
min_q.enqueue(4)
min_q.enqueue(9)
min_q.enqueue(6)
min_q.enqueue(10)
smallest = min_q.get_min()
print(smallest)

min_q.dequeue()
min_q.dequeue()
smallest = min_q.get_min()
print(smallest)

'''        
ms = MinStack()
ms.push(5)
ms.push(4)
ms.push(9)
ms.push(6)
ms.push(3)
ms.push(10)

min = ms.get_min()
print(min)

ms.pop()            # pop 10
ms.pop()            # pop 3
min = ms.get_min()
print(min)

ms.pop()            # pop 6
ms.pop()            # pop 9
ms.pop()            # pop 4
min= ms.get_min()
print(min)
'''


def is_valid(s):

    if not s:
        return True

    stack = []
    stack.append(s[0])

    count = 1
    while count < len(s):

        if not stack:
            stack.append(s[count])
        else:

            top = stack[-1]
            if top == "(" and s[count] == ")" or \
                    top == "[" and s[count] == "]" or \
                    top == "{" and s[count] == "}":

                stack.pop()
            else:
                stack.append(s[count])

        count += 1

    return len(stack) == 0

def evalRPN(tokens):

    stack = []
    for t in tokens:

        if t in ["*", "+", "-", "/"]:

            # right operand pop out before left operand
            r, l = stack.pop(), stack.pop()
            if t == "*":
                stack.append(l * r)
            elif t == "+":
                stack.append(l + r)
            elif t == "-":
                stack.append(l - r)
            elif t == "/":
                stack.append(l // r)
        else:

            stack.append(int(t))

    return stack.pop