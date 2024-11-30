import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import kagglehub

# Download latest version
#path = kagglehub.dataset_download(handle="ammaraahmad/immigration-to-canada")
# ['Country', 'Continent', 'Region', 'DevName', '1980', '1981', '1982','1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991',
# '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000','2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
# '2010', '2011', '2012', '2013', 'Total']
#print("Path to dataset files:", path)

#data = pd.read_csv(path + "/canadian_immegration_data.csv")
data = pd.read_csv("C:/Users/dayon/.cache/kagglehub/datasets/ammaraahmad/immigration-to-canada/versions/1/canadian_immegration_data.csv")
years = [str(year) for year in range(1980, 2014)]

data = data.set_index('Country') # set the index to be the first column

# brazil = data.loc['Brazil', years] # get the data for Brazil (df.loc[['Brazil', 'Argentina'], years])
# brazil_dict = {'year': brazil.index.tolist(), 'imigrate': brazil.values.tolist()} # create a dictionary with the data
# brazil_data = pd.DataFrame(brazil_dict) # create a dataframe with the dictionary

# plt.figure(figsize=(10, 5)) # set the figure size in inches (Polegadas)
# plt.plot(brazil_data['year'], brazil_data['imigrate']) # plot the data
# plt.xlabel('Year') # set the x axis label
# plt.xticks([str(year ) for year in range(1980, 2014, 5)]) # set the x axis ticks to be every 5 years
# plt.ylabel('Number of immegration') # set the y axis label
# plt.yticks([count for count in range(0, 3000, 500)]) # set the y axis ticks to be every 500
# plt.title("Brazilian immegration to Canada")
# plt.show()

# fig, ax = plt.subplots(figsize=(10, 5)) # create a figure and a set of subplots, fig is the figure and ax is the axis
# ax.plot(brazil_data['year'], brazil_data['imigrate'])
# ax.set_title("Brazilian immegration to Canada")
# ax.set_xlabel('Year')
# ax.set_ylabel('Number of immegration')
# ax.xaxis.set_major_locator(plt.MaxNLocator(10)) # set the x axis ticks to be every 10 years

# more than one plot
# fig, axs = plt.subplots(1, 2, figsize=(15, 10)) # create a figure and a set of subplots, fig is the figure and ax is the axis
# axs[0].plot(brazil_data['year'], brazil_data['imigrate'])
# axs[0].set_title("Brazilian immegration to Canada")
# axs[0].set_title("Brazilian immegration to Canada")
# axs[0].set_xlabel('Year')
# axs[0].set_ylabel('Number of immegration')
# axs[0].xaxis.set_major_locator(plt.MaxNLocator(10))
# axs[0].grid()

# axs[1].boxplot(brazil_data['imigrate'])
# axs[1].set_title("Brazilian immegration to Canada")
# axs[1].set_ylabel('Number of immegration')
# axs[1].grid()

# plt.show()

sns.set_theme()
sns.set_palette('Dark2')

fig, ax = plt.subplots(figsize=(10, 5))
ax = sns.lineplot(data.loc['Brazil', years], label='Brasil', lw=3)
ax = sns.lineplot(data.loc['Argentina', years], label='Argentina', lw=3)
ax = sns.lineplot(data.loc['Peru', years], label='Peru', lw=3)
ax = sns.lineplot(data.loc['Colombia', years], label='Colômbia', lw=3)

ax.set_title('Imigração dos maiores países da América do Sul\npara o Canadá de 1980 a 2013', loc='left', fontsize=20)
ax.set_xlabel('Ano', fontsize=14)
ax.set_ylabel('Número de imigrantes', fontsize=14)

ax.xaxis.set_major_locator(plt.MultipleLocator(5))

ax.legend(title='Países', loc='upper right', bbox_to_anchor=(1.18, 1.02))

plt.show()