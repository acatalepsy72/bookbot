from stats import *
import sys

arguments = sys.argv
def main():
    #INPUT
    #command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Ex: python3 main.py ../bookbot/books/frankenstein.txt")
        sys.exit(1)
    #initialize argument
    #~/github.com/acatalepsy72/bookbot$ sys.argv[0] sys.argv[1]
    script_name = sys.argv[0]
    path = sys.argv[1]

    #Data info
    print("Script Name: " + script_name)
    print("PATH: " + path)
    #REPORT
    print("================ BOOKBOT ================")
    print(f"Analyzing book found at {path}...")

    print("-------------- Word Count --------------")
    print(f"Found {word_count(path)} total words")

    print("------------ Character Count ------------")
    categorized = cat_list(count_char(path))
    categorized.sort(reverse=True, key=sort_helper)
    #Accesses the value inside the "char" and "num" 
    for item in categorized:
        print(f"{item["char"]}: {item["num"]}")

main()