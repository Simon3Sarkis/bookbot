import sys
from stats import get_num_words, get_char_num, sort_characters


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path = sys.argv[1]
with open(file_path) as f:
    content = f.read()
    

get_num_words(content, file_path)
char_counts = get_char_num(content)
sort_characters(char_counts)