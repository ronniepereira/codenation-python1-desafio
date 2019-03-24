# coding: utf-8
import csv
import heapq
# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
def q_1():
    nacio_list = []
    arquivo = open('data.csv', encoding = "utf8")
    jogadores_dic = csv.DictReader(arquivo)
        
    for jogador in jogadores_dic:
        nacionalidade = jogador['nationality']
        count_nacio = nacio_list.count(nacionalidade)
        if count_nacio == 0:
            nacio_list.append(nacionalidade)
    arquivo.close
    return len(nacio_list)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    arquivo = open('data.csv', encoding = "utf8")
    jogadores_dic = csv.DictReader(arquivo)
    club_list = []
    
    for jogador in jogadores_dic:
        club = jogador['club']
        if club not in club_list:
            club_list.append(club)
    else:
        arquivo.close
        return len(club_list)

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    arquivo = open('data.csv', encoding = "utf8")
    jogadores_dic = csv.DictReader(arquivo)
    nomes_jogadores = []
    resultado = []
    for jogador in jogadores_dic:
        nomes_jogadores.append(jogador['full_name'])
    for nome in nomes_jogadores[:20]:
            resultado.append(nome)
    arquivo.close
    return resultado

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    
    jogadores_list = []
    mais_valiosos = []

    with open('data.csv', encoding='utf8') as data:
        dic = csv.DictReader(data)
        for linha in dic:
            jogadores_list.append([ linha['full_name'], float(linha['eur_wage'])])
    maior_pontuacao = heapq.nlargest(10, jogadores_list, key=lambda x: x[1])
    for jogador in maior_pontuacao:
        mais_valiosos.append(jogador[0])
    return mais_valiosos

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():

    jogadores_list = []
    mais_velhos = []
    
    with open('data.csv', encoding='utf8') as data:
        dic = csv.DictReader(data)
        for linha in dic:
            jogadores_list.append([ linha['full_name'], float(linha['age'])])
    maior_idade = heapq.nlargest(10, jogadores_list, key=lambda x: x[1])
    for jogador in maior_idade:
        mais_velhos.append(jogador[0])
    return mais_velhos

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    list_idades = []
    idades_dic = dict()
    
    arquivo = open('data.csv', encoding = "utf8")
    jogadores_dic = csv.DictReader(arquivo)

    for jogador in jogadores_dic:
        list_idades.append(int(jogador['age']))

    set_idade = list(set(list_idades))
    for i in set_idade:
        if i not in idades_dic:
            idades_dic[i] = list_idades.count(i)
    arquivo.close
    return idades_dic

