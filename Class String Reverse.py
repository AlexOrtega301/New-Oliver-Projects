class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


# Take input from user
word = input("Enter a word: ")

# Create object
obj = Reverse(word)

# Display reversed string
print("Reversed string:", obj.reverse_string())
