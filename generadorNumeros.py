import os
os.system('cls')

from diccionario import *

primosRango = [2, 3]

def opcionMultiple(text, opciones = ['s', 'n'], siError ='Solo "s" y "n" son opciones válidas') :
  while True:
    opcion = str(input(text).strip())
    if opcion.lower() not in opciones:
      print(siError)
    else:
      break
  return (opcion)
#
def elegirIdioma():
  for key in textos:
    print(textos[key]['elegir'])
  
  lan = opcionMultiple('->\033[32m ',opcionesValidas['elegir'],opcionesValidas['error'])
  idioma = idiomaElegido[lan]
  return idioma
# 
def crearPrimos(idioma):
  global primosRango

  print(textos[idioma]['inicial'])
  try:
    inicio = int(input('->\033[32m '))
    print('\033[0m')
    if inicio < 1:
      inicio = 1  
      print(textos[idioma]['error en inicial'], inicio)

  except ValueError:
    inicio = 1
    print(textos[idioma]['error'], inicio)
  

  print(textos[idioma]['final'])
  try:
    fin = int(input('->\033[32m '))
    print('\033[0m')
    if fin <= inicio:
      fin = 2*inicio
      print(textos[idioma]['error en final'], fin)

  except ValueError:
    fin = 100
    print(textos[idioma]['error'], fin)

  for I in range(inicio, fin+1):
    verif = esprimo(I, primosRango)
    if verif == True:
      primosRango.append(I)
#
def esprimo(I, primos = [2,3]):

  # Verifica que el número no pretenezca a una lista de primos
  if max(primos) >= I:
    if I in primos:
      return True
    else:
      return False

  # Verifica que el número no sea divisible por un número contenido en la lista de primos
  if max(primos) >= I**0.5:
    for PR in primos:
      mod = I % PR
      if mod == 0:
        return False
    return True

  divisor = max(primos) + 2
  while True:
    mod = I % divisor
    if mod == 0:
      return False
    
    # Detiene la iteración si el divisor llega al punto tal qué es superior a la raiz cuadrada del supuesto primo
    if divisor >= I**0.5:
      return True
    
    divisor += 2

#
#         CONTINUAR POR ACÁ
# print(textos['Esp']['elegir'])
# print(textos['Eng']['elegir'])
# lan = opcionMultiple('->\033[32m ',opcionesValidas['elegir'],opcionesValidas['error'])

# crearPrimos(lan)
# print(primosRango)


# # opcionMultiple('->\033[32m ',opcionesValidas['elegir'],opcionesValidas['error'])