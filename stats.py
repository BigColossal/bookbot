def get_word_amount(string):
    words = string.split()
    return len(words)

def get_character_amounts(string):
    characters = {}
    words = string.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1

    return characters

def sort_characters(char_dict):
    sorted_list = []
    for char in char_dict:
        new_char_dict = {}
        new_char_dict["character"] = char
        new_char_dict["num"] = char_dict[char]
        sorted_list.append(new_char_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]