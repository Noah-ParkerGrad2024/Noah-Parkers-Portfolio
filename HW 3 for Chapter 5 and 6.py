def analyze_string(s):
    vowels = 'aeiou'
    result = {
        'length': len(s),
        'character_count': len(s),
        'vowel_count': 0,
        'consonant_count': 0
    }
    
    for char in s.lower():
        if char.isalpha():
            if char in vowels:
                result['vowel_count'] += 1
            else:
                result['consonant_count'] += 1
    
    return result

user_input = input('Enter a string: ')
analysis = analyze_string(user_input)

print(f'Length: {analysis["length"]}')
print(f'Character count: {analysis["character_count"]}')
print(f'Vowel count: {analysis["vowel_count"]}')
print(f'Consonant count: {analysis["consonant_count"]}')
