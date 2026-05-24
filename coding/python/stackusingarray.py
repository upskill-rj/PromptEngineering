
class stackusingarray:

    # Constructor
    def __init__(self, size):

        self.capacity = size
        self.stack = [0] * size
        self.top = -1


    #---------------------------
    # Pusk Operation
    #---------------------------

    def push(self, value):

        if self.is_full():
            print("Stack Overflow....")
            return

        self.top += 1
        self.stack[self.top] = value
        print(f"{value} pushed into stack")

    #-----------------------------
    # Pop Operation
    #-------------------------------

    def pop(self):

        if self.is_empty():
            print("STack Underflow .....")
            return None

        value = self.stack[self.top]
        self.top -= 1

        return value

    #-------------------------------
    # Peep Operation
    #-------------------------------

    def peek(self):

        if self.is_empty():
            print("Stack is Empty ...222 !!!!!!!")
            return None

        return self.stack[self.top]

    #-------------------------
    # Check Empty
    #-------------------------

    def is_empty(self):

        return self.top == -1

    #----------------------------
    #Check Full
    #----------------------------

    def is_full(self):

        return self.top == self.capacity - 1

    #------------------------------
    # Display Stack
    #--------------------------------

    def display(self):

        if self.is_empty():
            print("Stack is Empty 333 !!!!")
            return

        print("Inside Display ..... Stack Elements:")

        for i in range(self.top, -1, -1):
            print(self.stack[i])


#--------------------
# Main Program
#------------------------

stack = stackusingarray(5)

stack.push(100)
stack.push(200)
stack.push(300)

stack.display()

print("Top Element : ", stack.peek())
print("Popped Element: ", stack.pop())

stack.display()