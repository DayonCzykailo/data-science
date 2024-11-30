import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
    # Soma de todos os valores amostrais: 1000.5896;
    # Quantidade de amostras: 10;
    # Média: 1000.5896 / 10 = 100.05896.
    #
    # Coleta um unico registro (exemplo) 99.4197, subtraímos 100.05896 e anotamos o valor resultante,
    #  99.4197 - 100.05896 = -0.63926.
    # Em seguida, elevamos o resultado ao quadrado, (-0.63926)² = 0.4089.
    # Repetimos o processo para todos os registros e somamos todos os valores obtidos, 117.584.
    # Dividimos o resultado pelo número de amostras menos 1, 117.584 / (10 - 1) = 13.065. // isso é a variância amostral
    # Por fim, calculamos a raiz quadrada do resultado, √13.065 = 3.614.
    # 
    # Calculando o erro padrão amostral, 3.614 / √10 = 1.143.
    # Desvio padrão amostral: 3.614;
    # Número de amostras: 10;
    # Erro padrão amostral: 3.614 / sqrt(10) = 1.143

amostra_10_pesos = pd.DataFrame({'Peso das barras de chocolate (g)': [99.4197, 101.821, 98.5708, 100.63, 94.7449, 99.3241, 97.6067, 100.679, 108.739, 99.0544]})
dp = amostra_10_pesos['Peso das barras de chocolate (g)'].std()

sns.kdeplot(amostra_10_pesos['Peso das barras de chocolate (g)'], linewidth=2, fill= True, label=f'Desvio padrão = {dp:.3f}')
plt.legend()

plt.ylabel('Frequência')
plt.title('Distribuição suave pesos de barra amostrais')
plt.show()
