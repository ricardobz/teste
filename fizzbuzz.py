"""
Regras do jogo Fizzbuzz
1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para todos os outros dizer o número
"""
from functools import partial


multiple_of = lambda base, num : num % base == 0
multiple_of_5 = partial (multiple_of, 5)
multiple_of_3 = partial (multiple_of, 3)


def robot(pos):
    say = str(pos)

    if multiple_of_5(pos) and multiple_of_3(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3( pos):
        say = 'fizz'

    return say

