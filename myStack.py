# a stack is a linear data structure that stores items in a last in/first out manner.
# in a stack, a new element is added at one end and an element removed from that end only.
# the insert and delete operations are often called push and pop

# simple stack

# stack = []

# # add items to the stack
# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.append('d')
# stack.append('e')
# stack.append('f')
# print("Initial Stack")
# print(stack)

# # pop items from the end of the list
# stack.pop()
# print("removed item")
# print(stack)

# stack.pop()
# print("removed item")
# print(stack)

# stack.pop()
# print("removed item")
# print(stack)



# manually implemented stack
class Stack:
    def __init__(self):
        self.stack = []

    # add item to end of stack
    def push(self, data):
        return self.stack.append(data)

    # remove item from end of stack
    def pop(self):
        return self.stack.pop()

    # get reference to last item of the stack without removing it
    def peek(self):
        stack_size = self.size()
        return self.stack[stack_size - 1]

    # get size of stack
    def size(self):
        return len(self.stack)

    # print stack values
    def print_stack(self):
        stack_str = ""
        for item in self.stack:
            stack_str += str(item) + " "
        return stack_str

    # check if stack is empty (True/False)
    def empty(self):
        if self.size() == 0:
            return True
        return False

stack = Stack()

print(stack.empty())