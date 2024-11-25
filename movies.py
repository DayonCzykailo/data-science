import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# fonte: https://www.kaggle.com/tmdb/tmdb-movie-metadata
tmdb = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/tmdb_5000_movies.csv")
# ['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language',
#        'original_title', 'overview', 'popularity', 'production_companies',
#        'production_countries', 'release_date', 'revenue', 'runtime',
#        'spoken_languages', 'status', 'tagline', 'title', 'vote_average',
#        'vote_count']

# sns.displot(tmdb['vote_average'], kde=True)
# plt.title("Média de votos em filmes no TMDB 5000")
# plt.show()

#data_filtered = tmdb.query("revenue > 0")

# its show the mean of vote_average of each original_language
#data_filtered = tmdb.groupby('original_language')['vote_average'].mean()

# reset_index() is used to convert the result into a dataframe
data_filtered = tmdb['original_language'].value_counts().to_frame().reset_index()
data_filtered.columns = ['original_language', 'total']


print(data_filtered)

# sns.barplot(x='original_language', y='total', data=data_filtered)
# plt.show()

notas_do_toy_story = tmdb.query("filmeId==1")["nota"]
notas_do_jumanji = tmdb.query("filmeId==2")["nota"]

media_do_toy_story = notas_do_toy_story.mean()
media_do_jumanji = notas_do_jumanji.mean()

print(media_do_toy_story, media_do_jumanji)

mediana_do_toy_story = notas_do_toy_story.median()
mediana_do_jumanji = notas_do_jumanji.median()

print(f"Média do Toy Story {media_do_toy_story}")
print("Mediana do Toy Story {mediana_do_toy_story }" )
print(f"Média do Jumanji {media_do_jumanji }")
print("Mediana do Jumanji {mediana_do_jumanji }" ) 
