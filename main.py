def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict=get_char_dict(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for key in sorted(char_dict, key=char_dict.get, reverse=True):
         print(f"The '{key}' character was found {char_dict[key]} times")
    
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_dict(text):
    char_dict={}
    lower_text=text.lower()
    for c in lower_text:
        if c.isalpha():
            if c not in char_dict:
                char_dict[c]=1
            else:
                char_dict[c]+=1

    return char_dict




main()