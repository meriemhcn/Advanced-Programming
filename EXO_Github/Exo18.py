numbers = [1, 2, 3, 4, 5]

def display_menu():
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Sort")
    print("6. Reverse")
    print("7. Search")
    print("8. Save to file")
    print("9. Load from file")
    print("10. Quit")

def save_to_file(lst, filename="list.txt"):
    with open(filename, "w") as file:
        file.write(", ".join(map(str, lst)))
    print(f"List saved to {filename}")

def load_from_file(filename="list.txt"):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return list(map(int, content.split(", ")))
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

while True:
    print("\nCurrent List:", numbers)
    display_menu()
    try:
        option = int(input("Choose an option: "))
        if option == 1:
            value = int(input("Enter value: "))
            numbers.append(value)
        elif option == 2:
            value = int(input("Enter value: "))
            index = int(input("Enter index: "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
            else:
                print("Invalid index.")
        elif option == 3:
            if numbers:
                index = int(input("Enter index to pop (-1 for last element): "))
                if index == -1:
                    numbers.pop()
                elif 0 <= index < len(numbers):
                    numbers.pop(index)
                else:
                    print("Invalid index.")
            else:
                print("List is empty.")
        elif option == 4:
            value = int(input("Enter value to remove: "))
            if value in numbers:
                numbers.remove(value)
            else:
                print("Value not found in list.")
        elif option == 5:
            numbers.sort()
        elif option == 6:
            numbers.reverse()
        elif option == 7:
            value = int(input("Enter value to search: "))
            if value in numbers:
                print(f"Value {value} found at index {numbers.index(value)}.")
            else:
                print("Value not found in list.")
        elif option == 8:
            save_to_file(numbers)
        elif option == 9:
            numbers = load_from_file()
        elif option == 10:
            break
        else:
            print("Invalid option. Please choose from the menu.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
