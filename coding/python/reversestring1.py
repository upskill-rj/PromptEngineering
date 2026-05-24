class reversestring1:

    def reverse(self, text):

        char_array = list(text)
        char_array.reverse()

        return "".join(char_array)

obj = reversestring1()
print(obj.reverse("Hello World 123456"))


