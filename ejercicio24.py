# Dado un número N determinar si es un número primo.
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo, porque",n, "es un divisor")
            return False
    print("Es primo")
    return True
es_primo(16)