"""Gram_v1"""

def main():
    """Gram_v1"""
    text, dic_gram, lst_gram = input(), {}, []
    for i in range(len(text)-1):
        gram = text[i:i+2]
        if gram not in dic_gram:
            dic_gram[gram] = 1
            lst_gram.append(gram)
        else:
            dic_gram[gram] += 1
    result = lst_gram.pop(0)
    for i in lst_gram:
        if dic_gram[i] > dic_gram[result]:
            result = i
    print(result)
    print(dic_gram[result])

main()
