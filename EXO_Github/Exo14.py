word = input("Word: ")
spaces = (30 - len(word)) // 2
print(" " * spaces + word + " " * (30 - len(word) - spaces))
