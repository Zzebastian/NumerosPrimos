
textos = {'Esp': {}, 'Eng': {}}

textos['Esp'] = {'elegir': '\033[0mElija el idioma de operación, solo se admiten español (\033[32m1\033[0m) e ingles (\033[32m2\033[0m).',
                 'error eleccion': '\033[0mSolo se pueden elegir \033[32m1\033[0m o \033[32m2\033[0m',
                 'inicial' : '\033[0mElija el número a partir del cual desea obtener los primos',
                 'error en inicial': '\033[0mEl número inicial debe ser mayor o igual a "1", el valor por defecto es: ',
                 'final' : '\033[0mElija el número hasta el cual dese obtener los primos',
                 'error en final': '\033[0mEl número final debe ser mayor que el número inicial, el valor por defecto es: ',
                 'error' : '\033[0mHubo un error en la elección del número, el valor por defecto es',
                 }

textos['Eng'] = {"elegir": "\033[0mSelect the operating language, only Spanish (Esp) and English (Eng) are supported.\033[0m",
                 "error eleccion": "\033[0mOnly Esp or Eng can be selected.\033[0m",
                 
}
idiomaElegido = {'1': 'Esp', '2': 'Eng'}


opcionesValidas = {'Esp': {}, 'Eng': {}, 'elegir':['1', '2'], }

opcionesValidas['error'] = ''
for key in textos:
    opcionesValidas['error'] += textos[key]['error eleccion'] + '\n'

