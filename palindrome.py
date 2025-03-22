# check whether the word is a palindrome
# example "dad" will be reversed the same word
def palindrome(word):
    word_ = "".join(e.lower() for e in word if e.isalnum())  # Remove non-alphanumeric and convert to lowercase
    left = 0
    right = len(word_) - 1
    while left < right:
        if word_[left] != word_[right]:
            return False
        left += 1
        right -= 1
    return True

word = "dad"
result = palindrome(word)

# Show the result in the desired format
if result:
    print(f"{word} can be reversed to {word}")
else:
    print(f"{word} -> Not a palindrome")
