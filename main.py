from stats import get_word_count, get_char_count, get_sorted_chars
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
  


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  words = get_book_text(sys.argv[1])
  count = get_word_count(words)
  char_count = get_char_count(words)
  sorted_chars = get_sorted_chars(char_count)
  print("================BOOKBOT================")
  print("Analyzing book found at books/frankenstein.txt...")
  print("-------- Word Count --------")
  print(f"Found {count} total words")
  print("-------- Character Count --------")
  slices = sorted_chars[0:len(sorted_chars)-1]
  for slice in slices:
    if slice["character"].isalpha():
      print(f"{slice["character"]}: {slice["count"]}")


main()