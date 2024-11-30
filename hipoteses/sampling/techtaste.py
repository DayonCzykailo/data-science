import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Conjunto de dados TechTaste
df_techtaste = pd.DataFrame({'avaliacoes': [38, 44, 33, 42, 47, 33, 36, 39, 42, 36, 39, 34, 42, 42, 36, 43, 31, 35, 36, 41, 42, 30, 25, 38, 47, 36, 32, 45, 44, 45, 37, 48, 37, 36, 44, 49, 31, 45, 45, 40, 36, 50, 38, 34, 36, 42, 46, 49, 36, 34, 38, 31, 53, 40, 57, 40, 36, 42, 26, 50, 32, 43, 35, 37, 42, 30, 36, 43, 40, 43, 44, 52, 37, 51, 35, 47, 40, 50, 37, 49]})
qnt_amostras = 20#df_techtaste['avaliacoes'].count()
df_amostra = df_techtaste.sample(qnt_amostras)
media_amostral = df_amostra['avaliacoes'].mean()


### Calcule o desvio padrão amostral das avaliações.
desvio_padrao_amostal = df_amostra['avaliacoes'].std()
print(f'O desvio padrão amostral das avaliações é: {desvio_padrao_amostal:.2f}')

### Calcule o erro padrão amostral da média para as avaliações dos clientes.
erro_padrao_amostal = desvio_padrao_amostal / np.sqrt(qnt_amostras)
print(f'O erro padrão amostral da média para as avaliações dos clientes é: {erro_padrao_amostal:.2f}')

### Utilizando um gráfico de histograma, analise visualmente a distribuição das avaliações dos clientes.
sns.kdeplot(df_techtaste['avaliacoes'], linewidth=2, fill= True)
plt.show()

### Observe o formato da distribuição gerado no histograma. Ele se assemelha a uma distribuição normal?
### Com um nível de confiança de 90%, calcule o intervalo de confiança para a média das avaliações.

# Nível de confiança de 90%: O valor de z_critico para 90% de confiança é 1,645.
# Nível de confiança de 95%: O valor de z_critico para 95% de confiança é 1,96.
nivel_confianca, z_critico = 0.95, 1.96
margem_erro = z_critico * erro_padrao_amostal
graus_liberdade = qnt_amostras - 1 # Graus de liberdade
limite_inferior = media_amostral - margem_erro
limite_superior = media_amostral + margem_erro
print(f'O intervalo de confiança para a média das avaliações dos clientes é: ({limite_inferior:.2f}, {limite_superior:.2f})')

### A largura do intervalo de confiança seria afetada se o nível de confiança fosse aumentado para 95%? SIM