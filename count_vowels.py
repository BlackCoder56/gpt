def count_vowels(s: str) -> int:
    num = 0
    cleaned = s.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Use a set for faster lookups

    for i in cleaned:
        if i in vowels:
            num += 1
    
    return num


print(count_vowels('Monopoly and lopisI'))  # Output: 7
