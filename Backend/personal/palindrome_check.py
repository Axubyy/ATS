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


def palindrome(word):
    leftIdx = 0
    rightIdx = len(word)-1
    while leftIdx < rightIdx:
        if word[leftIdx] == word[rightIdx]:
            leftIdx += 1
            rightIdx -= 1
        else:
            return False
    return True


# def palindrome(word):
#     rev_word = [word[i] for i in range(len(word)-1, -1, -1)]
#     print(rev_word)
#     return word == "".join(rev_word)


print(palindrome("letter"))
