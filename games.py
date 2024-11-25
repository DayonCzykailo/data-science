import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import kagglehub

# Download latest version
path = kagglehub.dataset_download("rush4ratio/video-game-sales-with-ratings")
# 'Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score', 'Critic_Count', 
# 'User_Score', 'User_Count', 'Developer', 'Rating']

print("Path to dataset files:", path)

data = pd.read_csv(path + "/Video_Games_Sales_as_at_22_Dec_2016.csv")

########################## some questions to answer:              ##########################
########################## 1. Which platform has the most games?  ##########################

data_filtered1 = data['Platform'].value_counts().to_frame().reset_index()
sns.barplot(x='Platform', y='count', data=data_filtered1, palette='viridis', hue='count'),
plt.title("Number of games per platform")
plt.show()
# print(data_filtered1.head(1))

########################## 2. Which platform has the highest sales?##########################

data_filtered2 = data.groupby('Platform')['Global_Sales'].sum().to_frame().reset_index()
sns.barplot(x='Platform', y='Global_Sales', data=data_filtered2, palette='viridis', hue='Global_Sales', order=data_filtered2.sort_values('Global_Sales', ascending=False).Platform),
plt.title("Total sales per platform")
plt.show()

########################## 3. Which genre has the most games?      ##########################

data_filtered3 = data['Genre'].value_counts().to_frame().reset_index()
sns.barplot(x='Genre', y='count', data=data_filtered3, palette='viridis', hue='count'),
plt.title("Number of games per genre")
plt.show()