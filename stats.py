def get_word_count(text):
  word_list = text.split()
  return len(word_list)

def get_char_count(text):
  letters = {}
  for char in text:
    lower_char = char.lower()
    if lower_char not in letters:
      letters[lower_char] = 1
    else:
      letters[lower_char] += 1
  return letters

def get_sorted_chars(letters):
  unsorted = []
  for letter in letters:
    unsorted.append({
      "character": letter,
      "count": letters[letter]
    })
  unsorted.sort(reverse=True, key=sort_on)
  return unsorted

def sort_on(dict):
  return dict["count"]