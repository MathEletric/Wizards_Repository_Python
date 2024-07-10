import re

def main():

    coh_piah = le_assinatura()   
    textos = le_textos()
    avalia_textos(textos, coh_piah)
    


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    sum_dif = 0
    for i in range(6):
        sum_dif += float(abs(as_a[i] - as_b[i]))

    s_a_b = sum_dif/6.0

    return s_a_b

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    total_frases = 0  
    total_caractere = 0
    total_caractere_frase = 0
    total_caractere_sentenca = 0
    total_palavras = 0
    lista_total_palavras = []
    lista_palavras_diferentes = []
    lista_palavras_unicas = []
    lista_total_palavras = []

    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        total_frases += len(separa_frases(sentenca))
        frases = separa_frases(sentenca)
        total_caractere_sentenca += len(sentenca)
        for frase in frases:
            total_caractere_frase += len(frase)
            palavras = separa_palavras(frase)
            total_palavras += len(palavras)
            for palavra in palavras:
                palavra = palavra.lower()
                lista_total_palavras.append(palavra)
                total_caractere += len(palavra)
                if palavra not in lista_palavras_diferentes:
                    lista_palavras_diferentes.append(palavra)   
    for palavra in lista_total_palavras:
        if lista_total_palavras.count(palavra) == 1:
            lista_palavras_unicas.append(palavra)

    tamanho_medio_palavra = total_caractere/total_palavras
    type_token = len(lista_palavras_diferentes)/total_palavras
    hapax_legomana = len(lista_palavras_unicas)/len(lista_total_palavras)
    tamanho_medio_sentenca = total_caractere_sentenca/len(sentencas)
    complexidade_sentenca = total_frases/len(sentencas)
    tamanho_medio_frase = total_caractere_frase/total_frases 
   
    return [
            tamanho_medio_palavra, 
            type_token, 
            hapax_legomana, 
            tamanho_medio_sentenca,
            complexidade_sentenca, 
            tamanho_medio_frase
            ]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) 
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    estatistica_texto = []
    similaridade = []

    for texto in textos:
        estatistica_texto.append(calcula_assinatura(texto))

    print(estatistica_texto)
    for estatistica in estatistica_texto:
        similaridade.append(compara_assinatura(estatistica, ass_cp))

    menor = similaridade[0]
    indice_menor = 0
    print(similaridade)
    for i in range(len(similaridade)):
        if similaridade[i] < menor:
            menor = similaridade[i]
            indice_menor = i
    
    return indice_menor + 1


if __name__ == "__main__":
    main()