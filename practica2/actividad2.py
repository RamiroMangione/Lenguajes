import csv, json
from pathlib import Path as path
from datetime import datetime

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
contadordias = {}
fechas = []
contadorCampeones = {}
contadorChamps = {}
contadorC = {}
countcampeon = {}

ruta = path('practica2/actividad_2.csv')
with ruta.open('r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fecha = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M')
        fechas.append(fecha)
        dia = dias[fecha.weekday()]
        if dia in contadordias:
            contadordias[dia] += 1
        else:
            contadordias[dia] = 1

print('(punto3): los dias con mas entrenamientos son: ')
max_count = max(contadordias.values())
for dia, count in contadordias.items():
    if count == max_count:
        print(f'{dia} con {count} veces')

minfecha = min(fechas)
maxfecha = max(fechas)
diferencia = (maxfecha - minfecha).days
print(f'(punto 4): entre el primer entrenamiento: {minfecha} y el ultimo: {maxfecha} pasaron {diferencia} dias')



with ruta.open('r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        campeon = row['campeon']
        if campeon in contadorCampeones:
            contadorCampeones[campeon] += 1
        else:
            contadorCampeones[campeon] = 1
max_count_campeon = max(contadorCampeones.values())
print('(punto 5): los campeones mas entrenados son: ')
for campeon, countc in contadorCampeones.items():
    if countc == max_count_campeon:
        print(f'{campeon} con {countc} veces')


print('(punto 6): ')
divisor = diferencia / 7
for dia, count in contadordias.items():
    promedio = count / divisor
    print(f'el promedio de entrenamientos de los {dia} es de: {promedio} veces')



with ruta.open('r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fecha = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M')
        fechas.append(fecha)
        dia = dias[fecha.weekday()]
        champ = row['campeon']
        if dia == 'sabado' or dia == 'domingo':
            if champ in contadorChamps:
                contadorChamps[champ] += 1
            else:
                contadorChamps[champ] = 1
max_count_champ = max(contadorChamps.values())
print('(punto 7): los campeones mas entrenados los fines de semana son: ')
for champ, countchamp in contadorChamps.items():
    if countchamp == max_count_champ:
        print(f'{champ} con {countchamp} veces')

ruta_salida = path('practica2/salida')
ruta_salida.mkdir(exist_ok=True)
ruta = path('practica2/actividad_2.csv')
with ruta.open('r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        c = row['campeon']
        if c in contadorC:
            contadorC[c] += 1
        else:
            contadorC[c] = 1
ruta = path('practica2/salida/actividad_2.csv')
with ruta.open('w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['campeon', 'cantidad de entrenamientos'])
    for c, countc2 in contadorC.items():
        writer.writerow([c, countc2])
print('(punto 8): archivo actividad_2.csv creado en la carpeta salida')


ruta = path('practica2/actividad_2.csv')
with ruta.open('r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fecha = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M')
        fechas.append(fecha)
        dia = dias[fecha.weekday()]
        champ = row['campeon']
        if dia in countcampeon:
            if champ in countcampeon[dia]:
                countcampeon[dia][champ] += 1
            else:
                countcampeon[dia][champ] = 1
        else:
            countcampeon[dia] = {champ: 1}


data = path('practica2/salida/actividad_2.json')
with data.open('w', encoding='utf-8') as file:
    json.dump(contadordias, file, indent=4)
info = {
    'total de registros': sum(contadordias.values()),
    'dias': {
        dia: {
            'total entrenamientos': count,
            'campeones': {champ: countcampeon[dia].get(champ, 0) for champ in contadorCampeones}
        } for dia, count in contadordias.items()
    }
    }
with data.open('w', encoding='utf-8') as file:
    json.dump(info, file, indent=4)
with data.open('r', encoding='utf-8') as file:
    datos = json.load(file)
print('(punto 9): archivo json creado en la carpeta salida')