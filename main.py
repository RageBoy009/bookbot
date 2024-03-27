def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = count_words(text)
    letter_dict = count_letters(text)
    letter_list = list(letter_dict.items())
    def sort_on(item):
        return item[1]
    letter_list.sort(reverse=True, key=sort_on)
    print_result(letter_list, words_num, book_path)
    
    
    
def print_result(letter_list, num_words, book_path):
    print("---Begin report of ", book_path, " ---")
    print(num_words, " words found in the document\n")
    for i in range(len(letter_list)):
        char, count = letter_list[i]
        print(f"The '{char}' character was found {count} times")
        
    
   
    
    
def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def count_letters(text):
    erscheinungen = dict()
    lowered_words = text.lower()
    for char in lowered_words:
        if char.isalpha():
            if char not in erscheinungen:
                erscheinungen[char] = 1
            elif char in erscheinungen:
                erscheinungen[char] += 1
    return erscheinungen

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()