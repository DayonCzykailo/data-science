# Libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def averange(data: list) -> float:
    return sum(data) / len(data)


dados = pd.read_csv('./databases/csv/dados_vida_lampada.csv')

dados = dados.sample(120)

# Coletar a média para cada tamanho de amostra
medias = [dados[0:i]['duracao'].mean() for i in range(1, 120)]

medias.sort()

# plot
plt.figure(figsize=(16,6))
plt.title('O efeito do tamanho da amostra\n Média: {}'.format(averange(medias)))
plt.xlabel('Quantidade de amostras')
plt.ylabel('Média de duracao')
#plt.bar(range(1, 120), medias)
plt.hist(medias, bins=30)
plt.show()