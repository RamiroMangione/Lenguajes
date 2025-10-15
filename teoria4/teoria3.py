import csv,json
from pathlib import Path as path


pelis = [
    {'titulo': 'El Padrino', ' de estreno': 1972, 'pais de origen': 'Estados Unidos', 'actores principales': ['Marlon Brando', 'Al Pacino', 'James Caan']},
    {'titulo': 'Parasite','año de estreno': 2019,'pais de origen': 'Corea del Sur','actores principales': ['Song Kang-ho', 'Lee Sun-kyun', 'Cho Yeo-jeong']},
    {'titulo': 'The Dark Knight','año de estreno': 2008,'pais de origen': 'Estados Unidos','actores principales': ['Christian Bale', 'Heath Ledger', 'Aaron Eckhart']},
    {'titulo': 'el secreto de sus ojos','año de estreno': 2009,'pais de origen': 'Argentina','actores principales': ['Ricardo Darín', 'Soledad Villamil', 'Pablo Rago', 'guillermo francella']}
]
data = path('peliculas.json')
with data.open('w', encoding='utf-8') as file:
    json.dump(pelis, file, indent=4)


with data.open('r', encoding='utf-8') as file:
    datos = json.load(file)
print('peliculas: ',datos[0])

filtrados = []
count = 0
countpop = 0
ruta = path('teoria4/songs_normalize.csv')
with ruta.open('r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['artist'] == 'Drake':
            filtrados.append(row['song'])
            count += 1
            if int(row['popularity']) > 69:
                countpop += 1

print('canciones de drake: ',filtrados)
print('cantidad de canciones de drake: ',count)
print('cantidad de canciones de drake con popularidad de minimo 70: ',countpop)