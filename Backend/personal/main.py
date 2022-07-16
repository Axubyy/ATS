# def fibo_dp(n):
#     mem = [0, 1]
#     for i in range(2, n+1):
#         mem.append(mem[-2] + mem[-1])
#     return mem[n]


# def fibo_dp_mem(n):
#     mem = [0, 1]
#     for i in range(2, n + 1):
#         mem[i % 2] = mem[0] + mem[1]
#     print(mem)
#     return mem[n % 2]


# print(fibo_dp_mem(10))

def anagrams(S):
    print(sorted(S))
    d = {}
    for word in S:
        print(sorted(word))
        s = ''.join(sorted(word))
        print(s)  # calculate the signature
        if s in d:
            d[s].append(word)

        else:
            d[s] = [word]

    return [d[s] for s in d if len(d[s]) > 1]
    # print(S)
    # dic = {}
    # for s in S:
    #     word = ''.join(sorted(s))
    #     print(word)
    #     if word in dic:
    #         dic[word].append(s)
    #         # dic[word]+1
    #     else:
    #         dic[word] = [s]
    #     print(dic)
    #     word_list = [dic[word] for word in dic if len(dic[word]) > 1]
    #     return word_list


print(anagrams("bowel maker"))
