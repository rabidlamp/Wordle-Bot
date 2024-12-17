import random
while True:
    def pick_random_word(file_path):
        try:
            with open(file_path, 'r') as file:
                words = file.readlines()
            words = [word.strip() for word in words if word.strip()]
            return random.choice(words) if words else None
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
    file_path = 'words.txt'
    random_word = pick_random_word(file_path)

    if random_word:
        print(f"Random word: {random_word}")
    else:
        print("The file is empty or does not exist.")

    numbers = input("Enter 5 numbers separated by spaces: ")


    numbers_list = [int(num) for num in numbers.split()]

    def add_letter_to_list(letter, letter_list):
        if letter in letter_list:
            print("The letter '{letter}' is already in the list.")
        else:
            letter_list.append(letter)
            print("The letter '{letter}' has been added to the list.")
        return letter_list
        for e in numbers_list:
            if e == 0:
                banned_list = add_letter_to_list(e, letter)
                print("Updated list:", banned_list)
            elif e == 1:
                kinda_list = add_letter_to_list(e, letter)
                print("Updated list:", kinda_list)
            elif e == 20:
                yes_list = add_letter_to_list(e, letter)
                print("Updated list:", yes_list)


