def get_num_words(text, filepath):
    count = len(text.split())
    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {filepath}...\n"
        "----------- Word Count ----------\n"
        f"Found {count} total words"
    )

def get_char_num(text):
    counts = {}
    for word in text.split():
        for char in word.lower():
            if char.isalpha():
                counts[char] = counts.get(char, 0) + 1
    return counts

def sort_on(item):
    return item[1]

def sort_characters(char_counts):
    sorted_chars = list(char_counts.items())
    sorted_chars.sort(reverse=True, key=sort_on) 

    print("--------- Character Count -------")
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ===============")
