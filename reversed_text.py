# reverse text
def reversed_text(word):
  reversed_word = '' 
  for char in word:
    reversed_word = char + reversed_word
    return reversed_word
