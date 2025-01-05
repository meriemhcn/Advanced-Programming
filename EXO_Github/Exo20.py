import statistics

user_list = []

while True:
    try:
        number = int(input("Enter a number (0 to quit): "))
        if number == 0:
            print("Goodbye!")
            save_option = input("Would you like to save the list to a file? (yes/no): ").strip().lower()
            if save_option == "yes":
                filename = input("Enter filename to save: ").strip()
                try:
                    with open(filename, "w") as file:
                        file.write("Current List: " + str(user_list) + "\n")
                        file.write("Sorted List (Ascending): " + str(sorted(user_list)) + "\n")
                        file.write("Sorted List (Descending): " + str(sorted(user_list, reverse=True)) + "\n")
                        file.write(f"Mean: {statistics.mean(user_list):.2f}\n")
                        file.write(f"Median: {statistics.median(user_list):.2f}\n")
                    print(f"List saved to {filename}.")
                except Exception as e:
                    print(f"Error saving file: {e}")
            break
        user_list.append(number)
        print("Current List:", user_list)
        print("Sorted List (Ascending):", sorted(user_list))
        print("Sorted List (Descending):", sorted(user_list, reverse=True))
        if len(user_list) > 1:
            print(f"Mean: {statistics.mean(user_list):.2f}")
            print(f"Median: {statistics.median(user_list):.2f}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
