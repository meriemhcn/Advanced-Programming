unique_words = set()
total_words = 0

while True:
    word = input("Enter a word: ").strip()
    total_words += 1
    if word in unique_words:
        print(f"You typed in {len(unique_words)} unique words.")
        print("Unique words (alphabetically):", sorted(unique_words))
        save_option = input("Would you like to save the unique words to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            filename = input("Enter filename to save: ").strip()
            try:
                with open(filename, "w") as file:
                    file.write("\n".join(sorted(unique_words)))
                print(f"Unique words saved to {filename}.")
            except Exception as e:
                print(f"Error saving file: {e}")
        break
    unique_words.add(word)
