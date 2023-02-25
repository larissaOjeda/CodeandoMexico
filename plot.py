import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math as math
import requests
repo_url = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json' 
#Archivo GeoJSON
mx_regions_geo = requests.get(repo_url).json()


###################### INDIGENAS ###########################

df = pd.read_csv('indig.csv')


fig = px.choropleth(data_frame=df,
			geojson=mx_regions_geo,
			locations=df['Estado'],
			featureidkey='properties.name',
			color=df['Total'],
			color_continuous_scale="burg",
			scope="north america",
		)


fig.update_geos(fitbounds="locations",
		visible=False)

fig.update_layout(title="Población indígena en México (2020)",
			font=dict(size=25,))

updatemenus = list([dict(buttons=list()),
			dict(direction='down',
			showactive=True)])
#fig.show()		


#cdu_colorscale= [[0.0, ‘rgb(224, 224, 224)’],
#[0.35, ‘rgb(192, 192, 192)’],
#[0.5, ‘rgb(160, 160, 160)’],
#[0.6, ‘rgb(128, 128, 128)’],
#[0.7, ‘rgb(96, 96, 96)’],
#[1.0, ‘rgb(64, 64, 64)’]]



######################## AFROMEXICANOS #########################

df = pd.read_csv('afro.csv')


fig = px.choropleth(data_frame=df,
			geojson=mx_regions_geo,
			locations=df['Estado'],
			featureidkey='properties.name',
			color=df['Total'],
			color_continuous_scale="burg",
			scope="north america",
		)

fig.update_geos(fitbounds="locations",
		visible=False)

fig.update_layout(title="Población afromexicana en México (2020)",
			font=dict(size=25,))
#fig.show()		










df = pd.read_csv('mortchi.csv')

new_mo = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

df['mes_ocurr'] = pd.Categorical(df['mes_ocurr'], categories=new_mo,ordered=True)

df_mes = df
df_mes['mes_count'] = df_mes.groupby('mes_ocurr')['mes_ocurr'].transform('count')
df_mes['mes_ocurr'] = pd.Categorical(df_mes['mes_ocurr'],categories=new_mo,ordered=True)
df_mes = df_mes.groupby('mes_ocurr')['mes_ocurr'].count().reset_index(name="Total")
print(df_mes)

fig = px.bar(df_mes, x='mes_ocurr',y='Total', title="Número de muertes por mes en Chiapas, 2021",
		labels=dict(mes_ocurr="Mes",y="Total"))

fig.show()
#df_mes.groupby(['mes_ocurr'])["sexo"].count().reset_index(name="count")
#print(df_mes[['sexo']])

df = pd.read_csv('pobreza.csv')

fig = go.Figure()

fig.add_trace(go.Bar(x=df['Estado'],y=df['2016'], name="2016"))

fig.add_trace(go.Bar(x=df['Estado'],y=df['2018'], name="2018"))

fig.add_trace(go.Bar(x=df['Estado'],y=df['2020'], name="2020"))

newnames={'trace0':'2016','trace1':'2018','trace2':'2020'}


fig.update_layout(
	updatemenus=[
		dict(
			active=0,
			buttons=list([
				dict(label="Todos",
					method="update",
					args=[{"visible":[True,True,True]},
						{"title":"Porcentaje de pobreza por estado en población menor a 18 años"}]),
				dict(label="2016",
					method="update",
					args=[{"visible":[True,False,False]},
						{"title":"Porcentaje de pobreza por estado en población menor a 18 años<br>2016"}]),
				dict(label="2018",
					method="update",
					args=[{"visible":[False,True,False]},
						{"title":"Porcentaje de pobreza por estado en población menor a 18 años<br>2018"}]),	
				dict(label="2020",
					method="update",
					args=[{"visible":[False,False,True]},
						{"title":"Porcentaje de pobreza por estado en población menor a 18 años<br>2020"}]),
			]),
		),
	]
)

fig.update_layout(
	title_text="Porcentaje de pobreza por estado en población menor a 18 años",
)

fig.show()
