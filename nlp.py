# -*- coding: utf-8 -*-
"""Frequency-based algorithm for summarization

## Text pre-processing
"""

import re
import nltk
import string

original_text = """A inteligência artificial é uma inteligência similar à humana. 
                    É definida como o estudo de agentes artificiais com inteligência. 
                    É a Ciência e Engenharia de produzir máquinas com inteligência. 
                    A habilidade de resolver problemas e possuir inteligência. 
                    Essa técnica está relacionada ao comportamento inteligente. 
                    Por exemplo, envolve a construção de máquinas para raciocinar. 
                    Aprender com erros e acertos. 
                    A inteligência artificial é utilizada para reproduzir situações do cotidiano."""

original_text = re.sub(r'\s+', ' ', original_text)

nltk.download('punkt')
nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('portuguese')

string.punctuation

def preprocessamento(text):
  text_formatado = text.lower()
  tokens = []
  for token in nltk.word_tokenize(text_formatado):
    tokens.append(token)

  tokens = [palavra for palavra in tokens if palavra not in stopwords and palavra not in string.punctuation]
  text_formatado = ' '.join([str(elemento) for elemento in tokens if not elemento.isdigit()])

  return text_formatado

text_formatado = preprocessamento(original_text)

"""## Frequência das palavras"""

frequencia_palavras = nltk.FreqDist(nltk.word_tokenize(text_formatado))
frequencia_maxima = max(frequencia_palavras.values())

for palavra in frequencia_palavras.keys():
  frequencia_palavras[palavra] = (frequencia_palavras[palavra] / frequencia_maxima)


"""## Tokenização de sentenças"""
lista_sentencas = nltk.sent_tokenize(original_text)

"""## Geração do resumo (nota para as sentenças)"""

nota_sentencas = {}
for sentenca in lista_sentencas:
  #print(sentenca)
  for palavra in nltk.word_tokenize(sentenca.lower()):
    #print(palavra)
    if palavra in frequencia_palavras.keys():
      if sentenca not in nota_sentencas.keys():
        nota_sentencas[sentenca] = frequencia_palavras[palavra]
      else:
        nota_sentencas[sentenca] += frequencia_palavras[palavra]


import heapq
melhores_sentencas = heapq.nlargest(3, nota_sentencas, key=nota_sentencas.get)


resumo = ' '.join(melhores_sentencas)


"""## Visualização do resumo"""

from IPython.core.display import HTML
text = ''

display(HTML(f'<h1>Text summary based on frequency (highlighted):</h1>'))
for sentenca in lista_sentencas:
  if sentenca in melhores_sentencas:
    text += str(sentenca).replace(sentenca, f"<mark>{sentenca}</mark>")
  else:
    text += sentenca
display(HTML(f"""{text}"""))
