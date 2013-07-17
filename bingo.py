#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import datetime

# inicializa listas
lista = []
final = []
html = True

# abre base de palavras
arquivo = open('palavras.txt','r')

# percorre arquivo de palavras
linhas = arquivo.readlines()

for palavra in linhas:
    # adiciona na lista de palavras, removendo o '\n'
    lista.append(palavra[:-1])

# verifica se há palavras o suficiente
if len(lista) < 25:
    print 'ERRO: poucas palavras no palavras.txt'
    exit(1)

# escolhe 24 palavras para tabela
escolhidas = set()
for contador in range (1,25):
    # gera um número aleatório até encontrar uma palavra que não foi escolhida
    while True:
        indice = int(len(lista) * random.random())
        if indice not in escolhidas:
            break;

    # adiciona a palavra escolhida na lista da cartela
    final.append(lista[indice])
    # marca palavra como escolhida
    escolhidas.add(indice)

if html:
    # abre arquivo de saída
    saida = open('bingo.html','w')

    # insere cabeçalho
    saida.write('<html><head><title>WEB BINGO DO DCE!</title></head><body>')
    saida.write('<h1>Bingo do DCE</h1>')
    hoje = datetime.date.today()
    saida.write('<p>Cartela gerada %s</p>' % hoje)
    saida.write('<p> Seu nome: ___________________________<br /><br />')
    saida.write('    Seu RA: _____________________________</p><br />')

    # símbolo especial para o centro da cartela
    especial = '<IMG SRC="161590.jpg">'

    # cartela
    saida.write('<table border="1">')
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>' %(final[0],final[1],final[2],final[3],final[4]))
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>' %(final[5],final[6],final[7],final[8],final[9]))
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>' %(final[10],final[11],especial,final[12],final[13]))
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>' %(final[14],final[15],final[16],final[17],final[18]))
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>' %(final[19],final[20],final[21],final[22],final[23]))
    saida.write('</table>')
    saida.write('</body></html>')

    saida.close()

arquivo.close()

exit(0)
