import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import plotly.express as px
import plotly.graph_objects as go
repo_url = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json' 
#Archivo GeoJSON
mx_regions_geo = requests.get(repo_url).json()
pruebas = pd.read_csv('pruebas_1.csv', encoding = 'latin-1')

Hombres = pruebas[(pruebas.Sexo == 'Hombres')] 
Mujeres = pruebas[(pruebas.Sexo == 'Mujeres')] 
Total = pruebas[(pruebas.Sexo == 'Total')]

lista = ['Preescolar', 'Primaria', 'Secundaria', 'Preparatoria', 'Sin_escolaridad']
lista_sexo = ['Hombres', 'Mujeres', 'Total']
lista_df = [Hombres, Mujeres, Total]
lista_indices = [0,1,2,3,4,5,6,7,8,9]

fig = go.Figure()

fig = px.choropleth(data_frame=pruebas,
                geojson = mx_regions_geo,
                locations = pruebas['Entidad_federativa'],
                featureidkey = 'properties.name',
                color = pruebas['Preescolar'], 
                locationmode = 'geojson-id',
#                colorbar_title = 'Potly',
#                coloraxis = 'coloraxis',
                animation_frame='Sexo'
    )

fig.update_geos(fitbounds="locations", visible=False)

fig.show()

fig = go.Figure()
layout = dict(title_text = 'Escolaridad', geo_scope = 'north america')
index = 0
index2 = 5

COLS = 2
ROWS = 1

for x in lista:
    #layout=dict(title_text= 'Escolaridad', geo_scope = 'north america')
    geo_key = 'geo'+str(index+1) if index != 0 else 'geo'
    fig.add_trace(go.Choropleth(
                geojson = mx_regions_geo,
                locations = Hombres['Entidad_federativa'],
                featureidkey = 'properties.name',
                z = Hombres[x], 
                geo = geo_key,
                locationmode = 'geojson-id',
                name = 'hombres',
                colorbar_title = 'Potly',
                coloraxis = 'coloraxis'
    ))

    layout[geo_key] = dict(scope = 'north america', domain = dict(x = [], y = []))
    
    layout[geo_key]['domain']['x'] = [float(0)/float(COLS), float(1)/float(COLS)]
    layout[geo_key]['domain']['y'] = [float(0)/float(ROWS), float(1)/float(ROWS)]
    
    
    index = index + 1
    geo_key = 'geo'+str(index+1) if index != 0 else 'geo'
    fig.update_layout(layout)
    
    fig.add_trace(
        go.Choropleth(
                geojson = mx_regions_geo,
                locations = Mujeres['Entidad_federativa'],
                featureidkey = 'properties.name',
                z = Mujeres[x], 
                geo = geo_key,
                locationmode = 'geojson-id',
                name = 'mujeres',
                colorbar_title = 'Potly',
                coloraxis = 'coloraxis'
    ))
    
    layout[geo_key] = dict(scope = 'north america', domain = dict(x = [], y = []))
    
    
    layout[geo_key]['domain']['x'] = [float(1)/float(COLS), float(2)/float(COLS)]
    layout[geo_key]['domain']['y'] = [float(0)/float(ROWS), float(1)/float(ROWS)]
    print(f'geo_key: {geo_key}')
    print(layout)
    index = index + 1
    fig.update_layout(layout)
    fig.update_geos(fitbounds="locations", visible=False)
    fig.show()
    



lista_contador = [False for x in range(10)]
lista_contador2 = [False for x in range(10)]
lista_contador3 = [False for x in range(10)]
lista_contador4 = [False for x in range(10)]
lista_contador5 = [False for x in range(10)]
lista_contador6 = [False for x in range(10)]

lista_contador[0] = True
lista_contador[1] = True
lista_contador2[2] = True
lista_contador2[3] = True
lista_contador3[4] = True
lista_contador3[5] = True
#lista_contador4[6] = True
#lista_contador4[7] = True
lista_contador5[8] = True
lista_contador5[9] = True


l_cont1 = [False for x in range(5)]
l_cont2 = [False for x in range(5)]
l_cont3 = [False for x in range(5)]
l_cont4 = [False for x in range(5)]
l_cont5 = [False for x in range(5)]

l_cont1[0] = True
l_cont2[1] = True
l_cont3[2] = True
l_cont4[3] = True
l_cont5[4] = True

print(lista_contador)
print(lista_contador2)
print(lista_contador3)
print(lista_contador4)
print(lista_contador5)
print(l_cont1)
print(l_cont2)
print(l_cont3)
print(l_cont4)
print(l_cont5)


fig.update_layout (updatemenus=[
   dict(
        active = 0, 
        buttons = list([
                        dict(label = f'Preescolar' ,
                        method = "update",
                        args = [{"visible": lista_contador},
                            {"title":"Preescolar"}]),
                        dict(label = 'Primaria' ,
                        method = "update",
                        args = [{"visible": lista_contador2},
                            {"title":"Primaria"}]),
                        dict(label = 'Secundaria' ,
                        method = "update",
                        args = [{"visible": lista_contador3},
                            {"title":"Secundaria"}]),
                        dict(label = 'Preparatoria' ,
                        method = "update",
                        args = [{"visible": lista_contador4},
                            {"title":"Preparatoria"}]),
                        dict(label = 'Sin_escolaridad' ,
                        method = "update",
                        args = [{"visible": lista_contador5},
                            {"title":"Sin escolaridad"}]),
                           ]))])


fig.show()
