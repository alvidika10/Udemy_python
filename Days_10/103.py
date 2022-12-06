def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add, '-' : substract, 
    '*' : multiply, '/' : divide
}

def kalkulator():
    num1 = float(input('first number: '))
    for i in operations.keys():
        print(i)
    lanjut = True
    while lanjut:
        symbol = input('Choose a symbols: ')
        num2 = float(input('Next Number: '))
        answer = operations[symbol]
        jawaban = answer(num1, num2)
        print(f'{num1} {symbol} {num2} = {jawaban}')
        if input(f'Text "y" for calculate the answer {jawaban}, or text "n" for break and begin calculating from the beginning: ') == 'y':
            num1 = jawaban
        else:
            lanjut == False
            kalkulator()

kalkulator()

