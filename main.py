import csv
import heapq

# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
def q_1():
    nationality = []
    with open('data.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nationality.append(row['nationality'])

    nationality = (list(set(nationality)))
    return len(nationality)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    club = []
    with open('data.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            club.append(row['club'])

    club = (list(set(club)))
    return len(club)

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    names = []
    cont = 0
    with open('data.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names.append(row['full_name'])
            cont = cont + 1
            if cont == 20:
                break
    return names

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    wages = []
    names = []
    result = []

    with open('data.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            wages.append(row['eur_wage'])
            names.append(row['full_name'])

    wages = [float(x) for x in wages]
    largest = heapq.nlargest(10, wages)
    for x in largest:
        indice = wages.index(x)
        result.append(names[indice])
        del (wages[indice])
        del (names[indice])
    return result

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    ages = []
    names = []
    result = []

    with open('data.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ages.append(row['age'])
            names.append(row['full_name'])

    ages = [int(x) for x in ages]
    largest = heapq.nlargest(10, ages)
    for x in largest:
        indice = ages.index(x)
        result.append(names[indice])
        del (ages[indice])
        del (names[indice])
    return result

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    dic_ages = {}
    ages = []

    with open('data.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ages.append(row['age'])

    ages = [int(x) for x in ages]
    ages_set = list(set(ages))

    for x in ages_set:
        num = ages.count(x)
        dic_ages[x] = num

    return dic_ages