def count_vowels(s):
    return sum(character.lower() in "aeiou" for character in s)


text = input()
print(f"Vowels: {count_vowels(text)}")
