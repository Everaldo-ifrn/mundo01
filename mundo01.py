from math import sqrt, hypot, trunc, sin, cos, tan, radians

import random

#import pygame

def desafio001():
 return 'Olá Mundo!'


def desafio002(nome):
  return f'Seja bem-vindo, {nome}!'


def desafio003(n1, n2):
  return f'A soma de {n1} mais {n2} é {n1 + n2}'


def desafio004(algo):
  print(f'O tipo primitivo é {type(algo)}')
#Ver qual é o tipo primitivo 
  print(f'É numérico? {algo.isnumeric()}')
#Ver se tem só numérico
  print(f'E alfabético? {algo.isalpha()}')
#Ver se tem só letras
  print(f'Está maiúsculo? {algo.isupper()}')
#Ver se tem só tem letras maiúsculas 
  print(f'Está menúsculo? {algo.islower()}')
#Ver se tem só letras menusculas
  print(algo.isascii())

  print(f'É um número decimal? {algo.isdecimal()}')
#Ver se é numero decimal
  print(f'É digito? {algo.isdigit()}')
#ver se é digito
  print(algo.isidentifier())

  print(algo.isprintable())

  print(f'Só tem espacos? {algo.isspace()}')
#Ver se só tem espaço 
  print(f'Está capitalizado? {algo.istitle()}')
#Ver se a primeria letra está maiúscula
  print(f'É alfanumerico? {algo.isalnum()}')
#Ver se tem números e se tem letras


def desafio005(n):
  return f'O antecessor de {n} é {n - 1} \nE o sucessor de {n} é {n + 1}'


def desafio006(n):
  print(f'O dobro de {n} é {n * 2}')
  print(f'O triplo de {n} é {n * 3}')
  print(f'A raiz quadradade de {n} é {n ** (1/2):.2f}')


def desafio007(nota_1, nota_2):
  return f'Sua media vale: {(nota_1 + nota_2) / 2}'


def desafio008(m):
  cm = m * 100
  mm = m * 1000
  print(f'Em centimetros são: {cm}cm')
  print(f'Em milimetros são: {mm}mm')


def desafio009(n):
  print(f'{n} X {0} = {n * 0}')
  print(f'{n} X {1} = {n * 1}')
  print(f'{n} X {2} = {n * 2}')
  print(f'{n} X {3} = {n * 3}')
  print(f'{n} X {4} = {n * 4}')
  print(f'{n} X {5} = {n * 5}')
  print(f'{n} X {6} = {n * 6}')
  print(f'{n} X {7} = {n * 7}')
  print(f'{n} X {8} = {n * 8}')
  print(f'{n} X {9} = {n * 9}')
  print(f'{n} X {10} = {n * 10}')


def desafio010(dinheiro):
  return f'Com esse R${dinheiro} você pode comprar US${ dinheiro / 3.27:.2f}'


def desafio011(largura, altura):
  area = altura * largura
  print(f'A área dessa parede é {area}m^2')
  print(f'Você vai precisa de {area / 1 * altura / 2} litros para pintá-la.')
  tinta = area / 2
  print(f'Vai precisar de {tinta}L de tinta para pintar essa parede.')

  
def desafio012(valor):   
  return f'Com desconto de 5% esta saindo por R$ {valor - (valor * 5 / 100)}'


def desafio013(salario):
  return f'Seu salário com 15% de aumento ficou R${salario + (salario * 15 / 100)}'


def desafio014(c):
  return f'Essa temperatura em fahrenheit é {9 * c / 5 + 32}F'


def desafio015(km, dias):
  return f'Você vai ter que pagar R${(dias * 60) + (km * 0.15)}'


def desafio016(n):
  return f'O número {n} em sua porção inteira fica: {trunc(n)}'
  

def desafio017(co, ca):
  return f'A hipotenusa é: {hypot(co, ca):.2f}'


def desafio018(angulo):
  print(f'O seno de {angulo} é {sin(radians(angulo)):.2f}')
  print(f'O cosseno de {angulo} é {cos(radians(angulo)):.2f}')
  print(f'A tangente de {angulo} é {tan(radians(angulo)):.2f}')


def desafio019(alunos):
  return f'O aluno que vai apagar o quadro é: {random.choice(alunos)}'


def desafio020(grupo):
  random.shuffle(grupo)
  return f'A ordem será {grupo}'


#def desafio021():
#  pygame.init()
#  pygame.mixer.music.load('musica.mp3.mp3')
#Não está funcionando!!!


def desafio022(nome_completo):
  print(f'Seu nome completo com todas as letras maiúsculas fica: {nome_completo.upper()}')
  print(f'Seu nome completo com todas as letras minúsculas fica: {nome_completo.lower()}') 
  trocando = nome_completo.replace(' ', '')
  print(f'Seu nome completo tem {len(trocando)} letras')  
  dividido = nome_completo.split()
  print(f'O seu primeiro nome tem {len(dividido[0])} letras')


def desafio023(n):
  print(f'A unidade é {n // 1 % 10}')
  print(f'A dezena é {n // 10 % 10}')
  print(f'A centena é {n // 100 % 10}')
  print(f'A milhar é {n // 1000 % 10}')


def desafio024(cidade):
  return f'Essa cidade começa com Santo? {cidade.startswith("SANTO")}'


def desafio025(nome):
  return f'O seu nome tem Silva? {"SILVA" in nome.upper()}'
  

def desafio026(frase):
  print(f'Nessa frase a letra A aparece {frase.count("A")} vezes')
  print(f'A primeira posição que o A aparece é {frase.find("A")}')
  print(f'A ultima posição que o A aparece é {frase.rfind("A")}')


def desafio027(nome_completo):
  dividido = nome_completo.split()
  print(f'Seu primeiro nome é {dividido[0]}')
  print(f'Seu último nome é {dividido[-1]}')


def desafio028(n):
  num = random.randint(0,5)
  if num == n:
    return 'Parabéns, você venceu!!!'
  else:
    return f'Que pena você perdeu, o número era {num}'


def desafio029(velocidade):
  if velocidade > 80.0:
    print('Você foi multado. Passou do limite de 80km/h')
    multa = (velocidade - 80.0) * 7.0
    print(f'Sua multa é de R${multa:.2f}')
  print('Você esta numa velocidade correta, continue assim!')


def desafio030(num):
  if  num % 2 == 0 :
    return f'{num} é um número par'
  else:
    return f'{num} é um número ímpar'


def desafio031(distancia):
  if distancia <= 200: 
   return f'Você vai pagar de passagem R${0.50 * distancia:.2f}'
  else:
    return f'Você vai pagar de passagem R${0.45 * distancia:.2f}'


def desafio032(ano):
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    return 'Esse ano é bissexto'
  else:
    return 'Esse ano não é bissexto'

   
def desafio033(n1, n2, n3):
  if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
  elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}') 
  else:
    print(f'O maior número é {n3}')
  if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')
  elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
  else:
    print(f'O menor número é {n3}')


def desafio034(salario):
  if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
  else:
    aumento = salario + (salario * 10/100)
  return f'O aumento vai ser R${aumento:.2f}'


def desafio035(r1, r2, r3):
  if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r2 > r3:
    return 'Sim, elas podem formar um triângulo'
  else:
    return 'Não, elas não podem formar um triângulo'