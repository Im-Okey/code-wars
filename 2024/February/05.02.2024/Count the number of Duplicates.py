"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicate_count(text: str) -> int:
    text = text.lower()  # Convert the input string to lowercase
    seen = set()
    duplicates = set()
    for char in text:
        if char.isalnum() and char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return len(duplicates)


if __name__ == "__main__":
    print(duplicate_count("abcdeaB"))