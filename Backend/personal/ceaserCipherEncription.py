def ceaser_cipher(letters, key_num):
    new_letter_list = []
    for letter in letters:
        new_letter_list.append(get_new_letter(letter, key_num))
    return new_letter_list


def get_new_letter(letter, key_num):
    new_letter_code = ord(letter) + key_num

    if new_letter_code < 122:
        return chr(new_letter_code)
    else:
        return chr(96 + new_letter_code % 122)


def ceaser_cipher(letters, key_num):
    new_alphabet_list = []
    for letter in letters:
        new_alphabet_list.append(get_new_letter(letter, key_num))
    return "".join(new_alphabet_list)


def get_new_letter(letter, key_num):
    alphabets_list = list("abcdefghijklmnopqrstuvwxyz")
    new_letter_code = alphabets_list.index(letter) + key_num

    if new_letter_code < 25:
        return alphabets_list[new_letter_code]
    else:
        return chr(-1 + new_letter_code % 25)
