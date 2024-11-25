import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Download latest version
#path = kagglehub.dataset_download(handle="ammaraahmad/immigration-to-canada")
#print("Path to dataset files:", path)

#data = pd.read_csv(path + "/canadian_immegration_data.csv")
data = pd.read_csv("C:/Users/dayon/.cache/kagglehub/datasets/ammaraahmad/immigration-to-canada/versions/1/canadian_immegration_data.csv")
years = [str(year) for year in range(1980, 2014)]

data = data.set_index('Country') # set the index to be the first column

south = data.loc[['Brazil', 'Argentina', 'Colombia', 'Peru'], years] # get the data for Brazil (df.loc[['Brazil', 'Argentina'], anos])
south = south.transpose() # transpose the data

fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].plot(south.index, south['Brazil'])
axs[0, 0].set_title("Brazil Immegration to Canada")
axs[0, 0].set_xlabel('Year')
axs[0, 0].set_ylabel('Number of immegration')
axs[0, 0].xaxis.set_major_locator(plt.MaxNLocator(10))
axs[0, 0].grid()

axs[0, 1].plot(south.index, south['Argentina'])
axs[0, 1].set_title("Argentina Immegration to Canada")
axs[0, 1].set_xlabel('Year')
axs[0, 1].set_ylabel('Number of immegration')
axs[0, 1].xaxis.set_major_locator(plt.MaxNLocator(10))
axs[0, 1].grid()

axs[1, 0].plot(south.index, south['Colombia'])
axs[1, 0].set_title("Colombia Immegration to Canada")
axs[1, 0].set_xlabel('Year')
axs[1, 0].set_ylabel('Number of immegration')
axs[1, 0].xaxis.set_major_locator(plt.MaxNLocator(10))
axs[1, 0].grid()

axs[1, 1].plot(south.index, south['Peru'])
axs[1, 1].set_title("Peru Immegration to Canada")
axs[1, 1].set_xlabel('Year')
axs[1, 1].set_ylabel('Number of immegration')
axs[1, 1].xaxis.set_major_locator(plt.MaxNLocator(10))
axs[1, 1].grid()

for ax in axs.ravel():
    ax.set_ylim(0, 7000) # set the y axis limit for all plots


plt.savefig('south_american_immegration_to_canadian.png',  dpi=300, bbox_inches='tight', format='png')
#plt.show()