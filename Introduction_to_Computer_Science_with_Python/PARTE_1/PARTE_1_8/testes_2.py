import re

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
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    sum_dif = 0
    for i in range(6):
        sum_dif += float(abs(as_a[i] - as_b[i]))

    s_a_b = sum_dif/6.0

    return s_a_b

def calcula_assinatura(texto):

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
   
    return [tamanho_medio_palavra, 
            type_token, 
            hapax_legomana, 
            tamanho_medio_sentenca,
            complexidade_sentenca, 
            tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) 
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    estatistica_texto = []
    similaridade = []

    for texto in textos:
        estatistica_texto.append(calcula_assinatura(texto))

    for estatistica in estatistica_texto:
        similaridade.append(compara_assinatura(estatistica, ass_cp))

    menor = similaridade[0]
    print(similaridade)
    for i in range(len(similaridade)):
        if similaridade[i] < menor:
            menor = similaridade[i]
            indice_menor = i + 1
    
    return f"O autor do texto {indice_menor} está infectado com COH-PIAH"


def calcula_assinatura(texto):

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
   
    return [tamanho_medio_palavra, 
            type_token, 
            hapax_legomana, 
            tamanho_medio_sentenca,
            complexidade_sentenca, 
            tamanho_medio_frase]

texto = 'Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.'
texto2 = 'Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.'
print(calcula_assinatura(texto2))