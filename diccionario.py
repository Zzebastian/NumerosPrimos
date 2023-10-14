
textos = {'Esp': {}, 'Eng': {}}

textos['Esp'] = {'elegir': '\033[0mElija el idioma de operación, solo se admiten español (\033[32m1\033[0m) e ingles (\033[32m2\033[0m).',
                 'error eleccion': '\033[0mSolo se pueden elegir \033[32m1\033[0m o \033[32m2\033[0\n\033[0mOnly \033[32m1\033[0m or \033[32m2\033[0m can be chosen.',
                 'inicial' : '\033[0mElija el número a partir del cual desea obtener los primos',
                 'error en inicial': '\033[0mEl número inicial debe ser mayor o igual a "1", el valor por defecto es: ',
                 'final' : '\033[0mElija el número hasta el cual dese obtener los primos',
                 'error en final': '\033[0mEl número final debe ser mayor que el número inicial, el valor por defecto es: ',
                 'error' : '\033[0mHubo un error en la elección del número, el valor por defecto es',
                 'guardar' : '\033[0¿Desea guardar el conjunto creado en un archivo?\nIngrese "Enter" para guardar, o  "\033[32mn\033[0m" para evitarlo',
                 'error guardar' : 'Ingrese "Enter" para guardar, o  "\033[32mn\033[0m" para evitarlo',
                 'guardado' : 'Proceso de guardado finalizado'
                 }

textos['Eng'] = {
                'elegir': '\033[0mChoose the operating language, only Spanish (\033[32m1\033[0m) and English (\033[32m2\033[0m) are supported.',
                'error eleccion': '\033[0mOnly \033[32m1\033[0m or \033[32m2\033[0m can be chosen.',
                'inicial': '\033[0mChoose the number from which you want to get the primes',
                'error en inicial': '\033[0mThe initial number must be greater than or equal to "1", the default value is: ',
                'final': '\033[0mChoose the number up to which you want to get the primes',
                'error en final': '\033[0mThe final number must be greater than the initial number, the default value is: ',
                'error': '\033[0mThere was an error in the choice of the number, the default value is',
                }


idiomaElegido = {'1': 'Esp', '2': 'Eng'}


opcionesValidas = {'Esp': {}, 'Eng': {}, 'elegir':['1', '2'], }

opcionesValidas['error'] = ''
for key in textos:
    opcionesValidas['error'] += textos[key]['error eleccion'] + '\n'

