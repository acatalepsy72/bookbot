def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(path):
    return len(get_book_text(path).split())

def count_char(path):
    count = {}
    lowercase_text = get_book_text(path).lower()
    for char in lowercase_text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def cat_list(dict):
    categorized_list = []
    #items() provides access to both keys and values of a dictionary
    # ex usage: for key, value in dict.items()
    for char, count in dict.items():
        dictionary = {}
        if char.isalpha():
            dictionary["char"] = char
            dictionary["num"] = count
            categorized_list.append(dictionary)
    return categorized_list

def sort_helper(dict):
    return dict["num"]

