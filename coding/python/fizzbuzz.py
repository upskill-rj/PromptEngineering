class fizbuzz:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_fizzbuzz(self):

        for i in range(self.start, self.end + 1):

            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")

            elif i % 3 == 0:
                print("Fizz")

            elif i %5 == 0:
                print("Buzz")

            else:
                print(i)

fb = fizbuzz(1, 100)

fb.print_fizzbuzz()