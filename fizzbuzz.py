"""
Regras do jogo Fizzbuzz
1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para todos os outros dizer o número
"""

def multiple_of(base, num):
    return num % base ==0


def robot(pos):
    say = str(pos)

    if multiple_of(3, pos) and multiple_of(5, pos):
        say = 'fizzbuzz'
    elif multiple_of(5, pos):
        say = 'buzz'
    elif multiple_of(3, pos):
        say = 'fizz'

    return say

    
if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'

#M2A07 - 

