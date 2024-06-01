class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LLStack:
    def __init__(self, head_value=None):
        self.head = None
        if head_value != None:
            self.head = Node(head_value)

    def push(self, node_value):
        node = Node(node_value)
        if not self.is_empty():
            node.next = self.head
        self.head = node

    def peek(self):
        if not self.is_empty():
            return self.head.value

    def is_empty(self):
        return self.head == None

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")

        head = self.head
        self.head = self.head.next
        return head.value

    def depth(self):
        if self.is_empty():
            return 0
        else:
            count = 1
            temp = self.head
            while temp.next != None:
                count += 1
                temp = temp.next
            return count

    def __str__(self):
        str = "[ "
        if not self.is_empty():
            node = self.head
            while node.next != None:
                str += f"{node.value}"
                str += ", "
                node = node.next
            str += f"{node.value}"
        str += " ]"
        return str


# print("PUSH Case 1: Stack is empty; push 1 => [ 1 ] ?", end=" ")
# stack = LLStack()
# stack.push(1)
# print(stack)

# print("PUSH Case 2: Stack is [ 1 ]; push 2 => [ 2, 1 ] ?", end=" ")
# stack = LLStack(1)
# stack.push(2)
# print(stack)

# print("POP Case 1: Stack is [ 1 ]; pop => 1 [ ] ?", end=" ")
# stack = LLStack(1)
# print(stack.pop(), end=" ")
# print(stack)

# try:
#     print("POP Case 2: Stack is empty; pop => IndexError ?", end=" ")
#     stack = LLStack()
#     print(stack.pop(), end=" ")
#     print(stack)
# except IndexError as e:
#     print(f"{type(e).__name__}: {e}")
