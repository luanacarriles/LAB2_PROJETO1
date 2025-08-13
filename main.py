import random 

def media_7_numero():
    mumeros = [random.randit(1, 100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    return numeros, media

numeros_sorteados, media = media_7_numero()
print('Numeros sorteados:', numeros_sorteados)
print(f'Média dos 7 números sorteados: {media:.2f}')
