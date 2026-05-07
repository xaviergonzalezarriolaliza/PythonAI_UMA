class Stack:
    def __init__(self):
        self.__items = []

    def push(self, x):
        self.__items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        else:
            # raise IndexError("Stack is empty")
            raise ValueError("Pop on empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.__items) == 0
    
    def extend(self, items):    
        self.__items.extend(items)  

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)
    
    def __eq__(self, other):
        return self.__items == other.__items

    def __iter__(self):
        return _IteradorStack(self.__items)
    
class _IteradorStack:
    def __init__(self, source):
        self.__data = source
        self.__indice = len(self.__data) - 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice >= 0:
            value = self.__data[self.__indice]
            self.__indice -= 1
            return value
        else:
            raise StopIteration

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(1)
stack.push(8)
stack.push(3)
print(stack)

stack.pop()
stack.pop()

print("After 2xPops...")
print(stack)

p3 = Stack()    
p3.push(5)
p3.push(2)
print(stack==p3)

p3.extend([1,8,3])   
p3.extend("python")
p3.extend((1,2,3))
print(p3)