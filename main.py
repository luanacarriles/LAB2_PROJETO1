import random
def media_7_numeros():
    numeros= [random.randint(1,100) for _ in range(7)]
    media= sum(numeros) / len(numeros)
    return numeros, media 