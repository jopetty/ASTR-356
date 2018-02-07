from astropy.table import Table
import numpy as np
from matplotlib import pyplot as plt

names = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']
data = Table.read('imdb_top_10000.txt', format = 'ascii', delimiter = '\t', names = names, data_start = 0)

new_genres = set()
for row in data:
	new_genres.update(row['genres'].split('|'))

for g in new_genres:
	data[g] = False

for row in data:
	row['runtime'] = float(row['runtime'][:-6]) if float(row['runtime'][:-6]) != 0.0 else np.nan
	row['title'] = row['title'][:-7]
	for g in new_genres:
		row[g] = g in row['genres'].split('|')

plt.xticks(rotation=70)
plt.hist(data['runtime'], bins=20)
plt.show()