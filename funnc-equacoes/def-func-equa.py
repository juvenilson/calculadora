def soma(num1, num2,):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def divi(num1, num2):
    if num2 == 0:
        return "Erro na divisão por zero!"
    elif num1 == 0:
        return 0
    else:
        return num1 / num2
