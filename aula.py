import random
from collections import Counter
from matplotlib import pyplot as plt
import math

def quantidade_de_usuarios_na_rede():
  return 100

def gera_amizades (numero_conexoes_desejado, qtde_usuarios_na_rede):
  conexoes = []
  for _ in range (numero_conexoes_desejado):
    while True:
      u1 = random.randint (0, qtde_usuarios_na_rede - 1)
      u2 = random.randint(0, qtde_usuarios_na_rede - 1)
      if u1 != u2 and not((u1, u2) in conexoes):
        conexoes.append((u1, u2))
        break
  return conexoes

def quantidade_de_amigos (amizades):
  #[(1, 2), (3, 5), (1, 7), (8, 5)] => [1, 3, 1, 8] => {1:2, 3:1, 8:1}
  a = Counter (i for i, _ in amizades)
  #[(1, 2), (3, 5), (1, 7), (8, 5)] => [2, 5, 7, 5] => {2:1, 5:2, 7:1}
  b = Counter (i for _, i in amizades)
  #{1:2, 3:1, 8:1, 2:1, 5:2, 7:1}
  tudo = a + b
  #{1:2, 3:1, 8:1, 2:1, 5:2, 7:1} => [2, 1, 1, 1, 2, 1] => {2:2, 1:4}
  return Counter (x for x in tudo.values())

def gera_histograma_contagem_amigos(quantidade_de_amigos, qtde_usuarios_na_rede):
  xs = range(qtde_usuarios_na_rede)
  ys = [quantidade_de_amigos[x] for x in xs]
  plt.bar(xs, ys)
  plt.axis ([0, qtde_usuarios_na_rede, 0, qtde_usuarios_na_rede /4])
  plt.title("Histograma da Contagem de Amigos")
  plt.xlabel ("# de amigos")
  plt.ylabel ("# de usuários")
  plt.show()


def gera_histograma_contagem_amigos_test ():
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  amizades = gera_amizades(1000, qtde_usuarios_na_rede)
  qtde_amigos = quantidade_de_amigos(amizades)
  gera_histograma_contagem_amigos(qtde_amigos, qtde_usuarios_na_rede)


def mostra_primeiro_e_segundo_maiores (qtde_amigos):
  print (qtde_amigos)
  lista = sorted(qtde_amigos.values())
  print ("Maior: " + str(lista[len(lista) - 1]))
  print("Segundo maior: " + str(lista[-2]))


def mostra_primeiro_e_segundo_maiores_test ():
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  amizades = gera_amizades (1000, qtde_usuarios_na_rede)
  qtde_amigos = quantidade_de_amigos(amizades)
  mostra_primeiro_e_segundo_maiores (qtde_amigos)

def media_qtde_amigos (qtde_amigos):
  #{5: 2, 8: 2, 3: 5} => [10, 16, 15]
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  return sum (so_qtdes) / sum (x for x in qtde_amigos.values())

def media_qtde_amigos_test ():
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  amizades = gera_amizades(500, qtde_usuarios_na_rede)
  qtde_amigos = quantidade_de_amigos(amizades)
  print (media_qtde_amigos (qtde_amigos))


def mediana_qtde_amigos (qtde_amigos):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  ordenada = sorted (so_qtdes)
  meio = len (ordenada) // 2
  return ordenada[meio] if meio % 2 == 1 else (ordenada[meio - 1] + ordenada[meio]) / 2

def quantil (qtde_amigos, percentual = 0.5):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  indice = int(percentual * len (so_qtdes))
  return sorted(so_qtdes)[indice]

def moda_qtde_amigos (qtde_amigos):
  moda = max (qtde_amigos.values())
  return [x for x, count in qtde_amigos.items() if count == moda]

def amplitude_dos_dados (qtde_amigos):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  return max(so_qtdes) - min (so_qtdes)

def diferencas_em_relacao_a_media (qtde_amigos):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  media = media_qtde_amigos (qtde_amigos)
  return [x - media for x in so_qtdes]

def soma_dos_quadrados (diferencas):
  return sum (x**2 for x in diferencas)

def variancia (qtde_amigos):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  return soma_dos_quadrados(diferencas_em_relacao_a_media(qtde_amigos)) / (len (so_qtdes) - 1)

def desvio_padrao (qtde_amigos):
  return math.sqrt(variancia(qtde_amigos))

#1 Escreva uma função que constrói um histograma
#  que mostra a quantidade de amigos que pessoas de 
# cada sexo têm.

def define_sexo(quantidade_de_usuarios_na_rede):
  amizade_sexo = []
  for _ in range (quantidade_de_usuarios_na_rede):
    if (random.randint(0, 1) == 0):
      amizade_sexo.append(('masculino'))
    else:
      amizade_sexo.append(('feminino'))
  return amizade_sexo 

def conta_amizade_sexo(amizades, sexo):
  total_amigos_sexo = []
  masculino = 0
  feminino = 0

  for i in amizades:
    if sexo[i[0]] == 'masculino':
      masculino += 1
    else:
      feminino += 1
    if sexo[i[1]] == 'masculino':
      masculino += 1
    else:
      feminino += 1

  total_amigos_sexo.append(masculino)
  total_amigos_sexo.append(feminino)
  return total_amigos_sexo

def histograma_sexo_das_amizades(quantidade_de_amigos, qtde_usuarios_na_rede):
  sexo = define_sexo(qtde_usuarios_na_rede)
  amizade = conta_amizade_sexo(quantidade_de_amigos, sexo)
  total = amizade[0] + amizade[1] 
  xs = (0, 1)
  ys = [amizade[x] for x in xs]
  plt.bar(xs, ys)
  plt.axis(['masculinio', 'feminino', 0, total])
  plt.yticks ([100 * i for i in range (total//100)])
  plt.xticks ([i for i in range(-1,3)])
  plt.xlabel ("Sexo")
  plt.ylabel ("# de amigos")
  plt.title ("Quantidades de amigos por sexo")
  plt.show()

def histograma_sexo_das_amizades_test():
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  quantidade_de_amigos = gera_amizades(1000, qtde_usuarios_na_rede)
  histograma_sexo_das_amizades(quantidade_de_amigos, qtde_usuarios_na_rede)

""" 2 Escreva uma função que constrói um histograma que mostra a 
quantidade de amigos que pessoas de cada idade têm. """

def define_idade(quantidade_de_usuarios_na_rede):
  idade_usuario = []
  for _ in range (quantidade_de_usuarios_na_rede):
    idade_usuario.append(random.randint(12, 120))
  return idade_usuario 

def troca_chave(quantidade_de_amigos, idades):
  chave_trocada= {}
  for x in quantidade_de_amigos:
    chave_trocada[idades[x]] = quantidade_de_amigos[x]
  return Counter(chave_trocada)

def histograma_quantidade_de_amigos_por_idade(quantidade_de_amigos, qtde_usuarios_na_rede, idade_maxima, idade_minima):
  xs = range(idade_minima, idade_maxima)
  ys = [quantidade_de_amigos[x] for x in xs]
  plt.bar(xs, ys)
  plt.axis ([10, idade_maxima, 0, qtde_usuarios_na_rede /4])
  plt.title("Histograma da Contagem de Amigos pela Idade")
  plt.xlabel ("# idade")
  plt.ylabel ("# de amigos")
  plt.show()

def histograma_quantidade_de_amigos_por_idade_test():
  idade_minima = 12
  idade_maxima = 120
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  idades = define_idade(qtde_usuarios_na_rede)
  amizades = gera_amizades(1000, qtde_usuarios_na_rede)
  qtde_de_amigos = quantidade_de_amigos(amizades)
  amizade_idade = troca_chave(qtde_de_amigos, idades)
  histograma_quantidade_de_amigos_por_idade(amizade_idade, qtde_usuarios_na_rede, idade_maxima, idade_minima)

"""3 Escreva uma função que calcula a variância e o desvio padrão da idade das 
pessoas do sexomasculino que tenham pelo menos 22 anos
"""

def desvio_e_variancia_padrao_masculino_vinte_e_dois_anos():
  idade_maxima = 22
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  idades = define_idade(qtde_usuarios_na_rede)
  sexo = define_sexo(qtde_usuarios_na_rede)
  users = []
  for i in range(qtde_usuarios_na_rede):
    if sexo[i] == 'masculino' and idades[i] >= idade_maxima:
      users.append(idades[i])
  a = Counter (i for i in users)
  desvio = desvio_padrao(a)
  vari = variancia(a)
  return 'variancia = {vari}\ndesvio padrão = {desvio}'.format(vari=vari, desvio=desvio)

def main ():
  #mostra_primeiro_e_segundo_maiores_test()
  #media_qtde_amigos_test()
  #gera_histograma_contagem_amigos_test()
  histograma_sexo_das_amizades_test()
  histograma_quantidade_de_amigos_por_idade_test()
  print(desvio_e_variancia_padrao_masculino_vinte_e_dois_anos())
  
  
main()