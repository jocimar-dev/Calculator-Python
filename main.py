def inicio():
    print('''
Bem-vindo a Calculadora Snake
''')


inicio()
...


def calculate():
    operation = input('''
  Digite a operação que você quer fazer:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Insira o primeiro número: '))
    number_2 = int(input('Insira o segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você digitou um operador inválido, favor tentar novamente.')


def again():
    calcular_de_novo = input('''
Você deseja fazer um novo cálculo?
Se sim digite "S" se não "N".
''')

    if calcular_de_novo.upper() == 'S':
        calculate()
    elif calcular_de_novo.upper() == 'N':
        print('Valeu!.')
    else:
        again()


...
calculate()
