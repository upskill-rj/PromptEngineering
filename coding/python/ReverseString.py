class ReverseString:

    # constructor
    def __init__(self, text):
        self.text = text

    #-----------------------
    # Reverse String Method
    #-------------------------

    def reverse(self):

        # convert string to array/list
        char_array = list(self.text)

        start = 0
        end = len(char_array) - 1

        #Swap Characters

        while start < end:

            char_array[start], char_array[end] = char_array[end], char_array[start]

            start += 1
            end -= 1

        # convert array back to string
        reversed_string = "".join(char_array)

        return reversed_string

# -----------------------
# Main Program
# -------------------------

obj = ReverseString("Hello World !!!!")
result = obj.reverse()
print("Reverse String === ", result)

