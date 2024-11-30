# Libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

dados = pd.read_csv('./databases/csv/dados_vida_lampada.csv')

avarange = dados['duracao'].mean()
trust_level, z_critic = 0.95, 1.96
deviation_default = 105
sample_size = dados['duracao'].count()

interval = stats.norm.interval(trust_level, loc=avarange, scale=deviation_default/np.sqrt(sample_size))

sns.set_theme(style="ticks")

sns.pairplot(dados)
plt.show()