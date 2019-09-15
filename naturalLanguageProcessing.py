import re

from collections import Counter

regex = "[a-zA-ZçÇãÃõÕáÁéÉíÍóÓúÚâÂêÊîÎôÔûÛàÀ]+"
data = open("Shakespeare.txt").read()
tokens = re.findall(regex, data)
tokens_count = Counter(tokens)

def p_bigram(w1, w2):
    count_w1 = tokens_count[w1]
    count_w1w2 = 0

    for i in range(len(tokens)):
        if tokens[i] == w1 and tokens[i+1] == w2:
            count_w1w2 += 1        
    return count_w1w2/count_w1

def p_trigram(w1, w2, w3):
    count_w1w2 = tokens_count[w1] + tokens_count[w2]
    count_w1w2w3 = 0

    for i in range(len(tokens)-2):
        if tokens[i] == w1 and tokens[i+1] == w2 and tokens[i+2] == w3:
            count_w1w2w3 += 1        
    return count_w1w2w3/count_w1w2

def sugerirPalavra2(p1, p2):
    palavras = []
    count_palavras = 0

    for i in range(len(tokens)):
        if(tokens[i] == p1 and tokens[i+1] == p2):
            palavras.append(tokens[i+2].lower())

    maior1 = 0
    palavra1 = ""
    for i in range (len(palavras)):
        if(palavras.count(palavras[i]) > maior1):
            maior1 = palavras.count(palavras[i])
            palavra1 = palavras[i] 

    maior2 = 0
    palavra2 = ""
    for i in range (len(palavras)):
        if(palavras[i] == palavra1):
            continue
        else:
            if(palavras.count(palavras[i]) > maior2):
                maior2 = palavras.count(palavras[i])
                palavra2 = palavras[i] 

    maior3 = 0
    palavra3 = ""
    for i in range (len(palavras)):
        if(palavras[i] == palavra1 or palavras[i] == palavra2):
            continue
        else:
            if(palavras.count(palavras[i]) > maior3):
                maior3 = palavras.count(palavras[i])
                palavra3 = palavras[i] 
    print(p1+" "+p2+" "+palavra1)
    print(p1+" "+p2+" "+palavra2)
    print(p1+" "+p2+" "+palavra3)
    print()
    print("Probabilidade de ser "+p1+" "+p2+" "+palavra1+": ",end="")
    print(p_trigram(p1, p2, palavra1))
    print("Probabilidade de ser "+p1+" "+p2+" "+palavra2+": ",end="")
    print(p_trigram(p1, p2, palavra2))
    print("Probabilidade de ser "+p1+" "+p2+" "+palavra3+": ",end="")
    print(p_trigram(p1, p2, palavra3))


def sugerirPalavra1(palavraX):
    palavras = []
    count_palavras = 0

    for i in range(len(tokens)):
        if(tokens[i] == palavraX):
            palavras.append(tokens[i+1].lower())

    maior1 = 0
    palavra1 = ""
    for i in range (len(palavras)):
        if(palavras.count(palavras[i]) > maior1):
            maior1 = palavras.count(palavras[i])
            palavra1 = palavras[i] 

    maior2 = 0
    palavra2 = ""
    for i in range (len(palavras)):
        if(palavras[i] == palavra1):
            continue
        else:
            if(palavras.count(palavras[i]) > maior2):
                maior2 = palavras.count(palavras[i])
                palavra2 = palavras[i] 

    maior3 = 0
    palavra3 = ""
    for i in range (len(palavras)):
        if(palavras[i] == palavra1 or palavras[i] == palavra2):
            continue
        else:
            if(palavras.count(palavras[i]) > maior3):
                maior3 = palavras.count(palavras[i])
                palavra3 = palavras[i] 
    print(palavraX+" "+palavra1)
    print(palavraX+" "+palavra2)
    print(palavraX+" "+palavra3)
    
    print()
    print("Probabilidade de ser "+palavra1+": ",end="")
    print(p_bigram(palavraX, palavra1))
    print("Probabilidade de ser "+palavra2+": ",end="")
    print(p_bigram(palavraX, palavra2))
    print("Probabilidade de ser "+palavra3+": ",end="")
    print(p_bigram(palavraX, palavra3))
    print()

sugerirPalavra1("the")
sugerirPalavra2("the","king")

