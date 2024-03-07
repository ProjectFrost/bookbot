def main ():
    book_path = "books/frankestein.txt"
    text = get_text(book_path)
    words = count_words(text)
    characters = count_letters(text)
    converted_list = convert_to_dict_list(characters)
    converted_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"This book contains {words} words.")
    print("Character counts:")
    print()
     
    for entry in converted_list:
        print(f"The character {entry["char"]} was found {entry["num"]} times.")

    print("--- End of report ---")
def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict = {}
    for character in text:
        if character in letter_dict:
            letter_dict[character.lower()] += 1
        else:
            letter_dict[character.lower()] = 1
    return letter_dict

def convert_to_dict_list(dict):
    dict_list = []
    for character in dict:
        if character.isalpha():
            num = dict[character]
            new_dict = {"char": character, "num": num}
            dict_list.append(new_dict)
    return dict_list

def sort_on(dict):
    return dict["num"]
main()