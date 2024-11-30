import pandas as pd

df_equipe_vendas = pd.DataFrame({'Vendedor': [ 'Luíza', 'Bia', 'Rodrigo', 'Allan', 'Evaldo'],
                                 'Vendas Antes (R$)': [252.72, 203.91, 307.32, 185.78, 220.5],
                                 'Vendas Depois (R$)': [285.1, 223.15, 324.41, 202.23, 240.63]})

df_equipe_vendas.columns = ['vendedor', 'vendas_antes', 'vendas_depois']

    # Defina a natureza das amostras. Temos um caso de amostra independente ou pareada? R: Pareada
    # Formule uma hipótese para o primeiro caso da Zoop Megastore.
        # Hipótese Nula (H0): A média das diferenças entre as observações é igual a zero.
        # Hipótese Alternativa (H1): A média das diferenças é diferente de zero.
    # Aplique um teste paramétrico para tomar a decisão da hipótese.
    
from scipy.stats import ttest_rel
stats, p_value = ttest_rel(df_equipe_vendas['vendas_antes'], df_equipe_vendas['vendas_depois'])

if p_value < 0.05: # alpha = 0.05, se refere ao nivel 95% de confiança, esse valor é tabelado
    print('Rejeitar H0, pois P-Value =', p_value)
else:
    print('Não rejeitar H0, pois P-Value =', p_value)
    
    # Pelos resultados anteriores, a hipótese nula formulada é rejeitada ou não rejeitada? Explique o que justifica sua decisão.
        # R: rejeitada, pois o p-value é menor que 0.05, ou seja, a probabilidade de ocorrer o resultado observado é menor que 5%.
    
import pandas as pd

df_filiais = pd.DataFrame({'Filial Centro-Norte': [3.2, 2.9, 2.0, 3.3, 3.1],
                           'Filial Sul': [3.8, 4.0, 4.7, 4.9, 4.8]})

df_filiais.columns = ['centro_norte', 'sul']

    # Defina a natureza das amostras. Temos um caso de amostra independente ou pareada? R: Independente
    # Formule uma hipótese para o segundo caso da Zoop Megastore.
        # Hipótese Nula (H0): A média das vendas entre as filiais é igual.
        # Hipótese Alternativa (H1): A média das vendas entre as filiais é diferente.
    # Aplique um teste paramétrico para tomar a decisão da hipótese.
from scipy.stats import ttest_ind

stats, p_value = ttest_ind(df_filiais['centro_norte'], df_filiais['sul'])

# p_value quanto mais proximo de zero, mais proximo de serem diferentes,
# p_value quanto mais proximo de 1, mais proximo de serem iguais

if p_value < 0.05: # alpha = 0.05, se refere ao nivel 95% de confiança, esse valor é tabelado
    print('Rejeitar H0, pois P-Value =', p_value)
else:
    print('Não rejeitar H0, pois P-Value =', p_value)

    # Pelos resultados anteriores, a hipótese nula formulada é rejeitada ou não rejeitada? Explique o que justifica sua decisão.
    # R: rejeitada, pois o p-value é menor que 0.05, ou seja, a probabilidade de ocorrer o resultado observado é menor que 5%.