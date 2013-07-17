#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
import datetime

# inicializa listas
lista = []
final = []
html = True
latex = True

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
    saida.write('<html><head><title>Bingo do DCE</title></head><body>\n')
    saida.write('<h1>Bingo do DCE</h1>\n')
    saida.write('<p> Seu nome: ___________________________<br /><br />\n')
    saida.write('    Seu RA: _____________________________</p>\n')
    hoje = datetime.date.today()
    saida.write('<p>Cartela gerada %s</p><br />' % hoje)

    # símbolo especial para o centro da cartela
    especial = '<img src="bingo.jpg">'

    # cartela
    saida.write('<table border="1">\n')
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>\n' %(final[0],final[1],final[2],final[3],final[4]))
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>\n' %(final[5],final[6],final[7],final[8],final[9]))
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>\n' %(final[10],final[11],especial,final[12],final[13]))
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>\n' %(final[14],final[15],final[16],final[17],final[18]))
    saida.write('<tr><td> %s </td><td> %s </td><td> %s </td><td> %s </td><td> %s </td></tr>\n' %(final[19],final[20],final[21],final[22],final[23]))
    saida.write('</table>\n')
    saida.write('</body></html>\n')

    saida.close()

if latex:
    # abre arquivo de saída
    saida = open('bingo.tex','w')

    # insere cabeçalho
    saida.write('\\documentclass[12pt,a4paper]{article}\n')
    saida.write('\\usepackage{fullpage}\n')
    saida.write('\\usepackage[brazilian]{babel}\n')
    saida.write('\\usepackage[utf8]{inputenc}\n')
    saida.write('\\usepackage[T1]{fontenc}\n')
    saida.write('\\usepackage{indentfirst}\n')
    saida.write('\n')
    saida.write('\\usepackage{graphicx}\n')
    saida.write('\\usepackage{array}\n')
    saida.write('\n')
    saida.write('\\title{Bingo do DCE}\n')
    saida.write('\\author{Seu nome: \\rule{5cm}{0.1mm}\\\\\n')
    saida.write('        Seu RA:  \\rule{2.5cm}{0.1mm}}\n')
    saida.write('\\date{Cartela gerada \\today}\n')
    saida.write('\n')
    saida.write('\\begin{document}\n')
    saida.write('\\maketitle\n')
    saida.write('\n')
    saida.write('\\centering\n')

    # símbolo especial para o centro da cartela
    especial = '\\includegraphics[height=12pt]{unicamp}'

    # cartela
    saida.write('\\begin{tabular}{|c|c|c|c|c|}\\hline\n')
    saida.write('%s & %s & %s & %s & %s \\\\\\hline\n' % (final[0],final[1],final[2],final[3],final[4]))
    saida.write('%s & %s & %s & %s & %s \\\\\\hline\n' % (final[5],final[6],final[7],final[8],final[9]))
    saida.write('%s & %s & %s & %s & %s \\\\\\hline\n' % (final[10],final[11],especial,final[12],final[13]))
    saida.write('%s & %s & %s & %s & %s \\\\\\hline\n' % (final[14],final[15],final[16],final[17],final[18]))
    saida.write('%s & %s & %s & %s & %s \\\\\\hline\n' % (final[19],final[20],final[21],final[22],final[23]))
    saida.write('\\end{tabular}\n')
    saida.write('\\end{document}\n')

    saida.close()

    # compila o arquivo .tex
    os.system('pdflatex --interaction=nonstopmode bingo.tex')

arquivo.close()

exit(0)
