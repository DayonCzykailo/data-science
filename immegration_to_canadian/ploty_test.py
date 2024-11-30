import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("C:/Users/dayon/.cache/kagglehub/datasets/ammaraahmad/immigration-to-canada/versions/1/canadian_immegration_data.csv")
years = [str(year) for year in range(1980, 2014)]

data = data.set_index('Country') 

fig = px.line(data.loc['Brazil', years], title="Brazilian immegration to Canada", labels={'index': 'Year', 'value': 'Number of immegration'})
# fig.write_html('immegration_to_canadian/immegration.html') # save the plot as a html file
fig.show()