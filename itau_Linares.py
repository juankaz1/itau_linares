
import pandas as pd
import numpy as np

#leemos los datos
detasa = pd.read_csv('Detalle_Tasa.csv')
tipoen = pd.read_csv('Tipo_entidad.csv')
enti = pd.read_csv('Entidades.csv')
tipocred = pd.read_csv('Tipo_Credito.csv')
plazos = pd.read_csv('Plazos.csv')


detasa.head()
tipoen.head()
enti.head()
tipocred.head()
plazos.head()

# version rpta 1

df = detasa[['Id_entidad_financiera', 'Nombre_Tipo_Entidad', 'cod_sub_tipo', '(8)Tasa_efectiva_promedio_ponderada']]
df = df.sort_values(by=['(8)Tasa_efectiva_promedio_ponderada'], ascending=False).head(5)
df = df.sort_values(by=['Nombre_Tipo_Entidad', 'Id_entidad_financiera', 'cod_sub_tipo'])


# esto era para hallar los 5 con mayor tasa de cada clasificacion
#df = df.groupby(['Id_entidad_financiera','Nombre_Tipo_Entidad', 'cod_sub_tipo']).head(5)


df = df.merge(enti, how='left', on='Id_entidad_financiera') 

tipe = tipocred[['cod_sub_tipo', 'descripcion_tipo' ]]
df = df.merge(tipe, how='left', on='cod_sub_tipo') 

df


#    Hasta ahi va el punto 1


dk = detasa[['Id_entidad_financiera', 'Nombre_Tipo_Entidad', 'cod_sub_tipo', '(8)Tasa_efectiva_promedio_ponderada', '(10)Montos_desembolsados', '(11)Número_de_créditos_desembolsados']]
dk = dk.merge(tipe, how='left', on='cod_sub_tipo') 
dk1 = dk.groupby(['Nombre_Tipo_Entidad', 'descripcion_tipo' ]).agg({'(8)Tasa_efectiva_promedio_ponderada':'mean', '(10)Montos_desembolsados':'sum', '(11)Número_de_créditos_desembolsados':'sum'})


dk1

#     Hasta aqui va el punto 2


detasa['Fecha_Corte'] = pd.to_datetime(detasa['Fecha_Corte'])
detasaoct = detasa[ detasa['Fecha_Corte'].dt.month == 10]


#a
dk2 = detasaoct.groupby(['(3)Tamaño_de_empresa' ]).agg({'(8)Tasa_efectiva_promedio_ponderada':'mean', '(10)Montos_desembolsados':'sum'})

dk2

#b
dk3 = detasaoct[detasaoct['(1)Tipo_de_persona']=='Natural']

dk3 = dk3.groupby(['(6) Producto de crédito' ]).agg({'(8)Tasa_efectiva_promedio_ponderada':'mean', '(10)Montos_desembolsados':'sum'})

dk3


#c

detasaoct.groupby(['(7) Plazo de crédito' ])['(8)Tasa_efectiva_promedio_ponderada'].agg(['mean','count'])

#d
#solo estan los del mes oct
detasaoct.groupby(['(2)Sexo', '(5)Tipo_de_garantía' ]).agg({'(10)Montos_desembolsados':'sum', '(11)Número_de_créditos_desembolsados':'sum'})


# Hasta aqui va el punto 3





casi1[['Fecha_Corte', 'Nombre_Tipo_Entidad', ]]

casi1 = detasa.merge(tipoen, how='left', on='Nombre_Tipo_Entidad') 
casi2 = casi1.merge(enti, how='left', on='Id_entidad_financiera')
plazos = plazos.rename(columns = {'Plazo_credito':'(7) Plazo de crédito'})
casi3 = casi2.merge(plazos, how='left', on='(7) Plazo de crédito')
final = casi3.groupby(['Fecha_Corte', 'Tipo_Entidad', 'Nombre_Tipo_Entidad', 'Id_entidad_financiera', 'Entidad_financiera', '(1)Tipo_de_persona', '(3)Tamaño_de_empresa', 'Cod_Plazo', '(7) Plazo de crédito' ]).agg( {'(9)Margen_adicional_a_la_variación_para_créditos_en_UVR':['max', 'min'], '(8)Tasa_efectiva_promedio_ponderada': ['mean','max', 'min'],  '(10)Montos_desembolsados': ['sum', 'min', 'max'],    '(11)Número_de_créditos_desembolsados':'sum'})

final



#    Hasta aqi el punto 4





