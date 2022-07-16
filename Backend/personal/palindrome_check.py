# def palindrome(word):
#     return word is "".join(reversed(word))


def palindrome(word):
    rev_word = ""
    revs_word = []
    for i in range(len(word)-1, -1, -1):
        # print(rev_word)
        rev_word += word[i]
        revs_word.append(word[i])

    print(revs_word)
    return word == rev_word


# def palindrome(word):
#     rev_word = [word[i] for i in range(len(word)-1, -1, -1)]
#     print(rev_word)
#     return word == "".join(rev_word)


print(palindrome("letter"))
