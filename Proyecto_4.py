#!/usr/bin/env python
# coding: utf-8

# ¡Hola!
# 
# Me llamo Santiago y para mí es un gusto revisar tu proyecto el dia de hoy. Soy el reviewer que te estará acompañando y asesorando en el proceso de revisión el día de hoy.
# 
# Cuando vea un error iré realizando un proceso gradual de darte información, de solo informarte la primera vez a darte más datos acerca del mismo en las siguientes iteraciones que te puedan ayudar a tener una visión más amplia de la situación. Haré comentarios, desde observaciones hasta sugerencias prácticas que involucran temas generales y buenas prácticas en el área si así lo deseas. También puedes comentarme preguntas o discusiones que puedas tener con plena tranquilidad.
# 
# Respecto a los comentarios que yo realize: **No los elimines, muevas o modifiques por favor**.
# 
# Encontrarás mis comentarios con los colores verde, amarillo y rojo, así:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien. Todo se realizó correctamente.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Bien hecho aunque hay algunas sugerencias que te pueden ser útiles
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Requiere acciones o correciones, esta parte requiere tomar correciones debido a que hay algo que puede no funcionar como lo esperamos.
# </div>
# 
# Si deseas comentarme algo, puedes hacerlo sin problema usando el siguiente formato:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante.</b> <a class="tocSkip"></a>
#     
# Preguntas, discusiones o solo comentarios.
# </div>

# # ¿Cuál es la mejor tarifa?
# 
# Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
# Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.

# [Te proporcionamos algunos comentarios para orientarte mientras completas este proyecto. Pero debes asegurarte de eliminar todos los comentarios entre corchetes antes de entregar tu proyecto.]
# 
# [Antes de sumergirte en el análisis de datos, explica por tu propia cuenta el propósito del proyecto y las acciones que planeas realizar.]
# 
# [Ten en cuenta que estudiar, modificar y analizar datos es un proceso iterativo. Es normal volver a los pasos anteriores y corregirlos/ampliarlos para permitir nuevos pasos.]

# ## Inicialización

# In[332]:


# Cargar todas las librerías
import pandas as pd
import numpy as np
import math
from scipy import stats as st
import matplotlib.pyplot as plt
import seaborn as sns


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Bien la forma de traer las librerías.
# </div>

# ## Cargar datos

# In[333]:


# Carga los archivos de datos en diferentes DataFrames

calls = pd.read_csv('/datasets/megaline_calls.csv')
internet = pd.read_csv('/datasets/megaline_internet.csv')
messages = pd.read_csv('/datasets/megaline_messages.csv')
plans = pd.read_csv('/datasets/megaline_plans.csv')
users = pd.read_csv('/datasets/megaline_users.csv')


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Bien la carga de los datos.
# </div>

# ## Preparar los datos

# [Los datos para este proyecto se dividen en varias tablas. Explora cada una para tener una comprensión inicial de los datos. Si es necesario, haz las correcciones requeridas en cada tabla.]

# ## Tarifas

# In[334]:


# Imprime la información general/resumida sobre el DataFrame de las tarifas

print('El dataset calls tiene la siguiente información\n')
print(calls.info())
print('El dataset internet tiene la siguiente información\n')
print(internet.info())
print('El dataset messages tiene la siguiente información\n')
print(messages.info())
print('El dataset plans tiene la siguiente información\n')
print(plans.info())
print('El dataset users tiene la siguiente información\n')
print(users.info())


# In[335]:


# Imprime una muestra de los datos para las tarifas
print('El dataset calls tiene la siguiente información\n')
print(calls.head(5))
print('El dataset internet tiene la siguiente información\n')
print(internet.head(5))
print('El dataset messages tiene la siguiente información\n')
print(messages.head(5))
print('El dataset plans tiene la siguiente información\n')
print(plans.head(5))
print('El dataset users tiene la siguiente información\n')
print(users.head(5))


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]

# ## Corregir datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[336]:


calls['id'] = calls['id'].astype('int')
calls['call_date']=pd.to_datetime(calls['call_date'], format='%Y-%m-%d')
print(calls.info())


# In[337]:


internet['id'] = internet['id'].astype('int')
internet['session_date']=pd.to_datetime(internet['session_date'], format='%Y-%m-%d')
print(internet.info())


# In[338]:


messages['id'] = messages['id'].astype('int')
messages['message_date']=pd.to_datetime(messages['message_date'], format='%Y-%m-%d')
print(messages.info())


# In[339]:


plans['plan_name'] = plans['plan_name'].astype('str')
print(plans.info())


# In[340]:


users['reg_date']=pd.to_datetime(users['reg_date'], format='%Y-%m-%d')
users['churn_date']=pd.to_datetime(users['churn_date'], format='%Y-%m-%d')
print(users.info())


# ## Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# ## Usuarios/as

# In[341]:


# Imprime la información general/resumida sobre el DataFrame de usuarios
print(users.info())
print(users.describe())


# In[342]:


# Imprime una muestra de datos para usuarios
print(users.head())


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]
# 
# 
# En cuanto a tipo de datos, ya se hicieron las correciones en los datos de fecha, asi mismo, tenemos datos ausentes que representan que el usuario sigue vigente con su plan

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[343]:


users.duplicated().sum()


# In[344]:


users.isna().sum()


# ### Enriquecer los datos

# ## Llamadas

# In[345]:


# Imprime la información general/resumida sobre el DataFrame de las llamadas
print(calls.info())
print(calls.describe())


# In[346]:


# Imprime una muestra de datos para las llamadas

print(calls.head())


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]
# 
# En cuanto a tipo de datos, ya se hicieron las correciones en los datos de fecha, asi mismo, no tenemos datos ausentes ni duplicados.
# 

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[347]:


calls.duplicated().sum()


# In[348]:


calls.isna().sum()


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[349]:


calls['month'] = calls['call_date'].dt.month
print(calls.head())


# ## Mensajes

# In[350]:


# Imprime la información general/resumida sobre el DataFrame de los mensajes
print(messages.info())


# In[351]:


messages.head()


# En cuanto a tipo de datos, ya se hicieron las correciones en los datos de fecha, asi mismo, no tenemos datos ausentes ni duplicados.

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[352]:


messages.duplicated().sum()


# In[353]:


messages.isna().sum()


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[354]:


messages['month'] = messages['message_date'].dt.month
print(messages)


# ## Internet

# In[355]:


# Imprime la información general/resumida sobre el DataFrame de internet
print(internet.info())
print(internet.describe())


# In[356]:


# Imprime una muestra de datos para el tráfico de internet
internet.head()


# En cuanto a tipo de datos, ya se hicieron las correciones en los datos de fecha, asi mismo, no tenemos datos ausentes ni duplicados.

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[357]:


internet.duplicated().sum()


# In[358]:


internet.isna().sum()


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[359]:


internet['month'] = internet['session_date'].dt.month

print(internet)


# In[360]:


plans['gb_per_month_included'] = (plans['mb_per_month_included'])/1024
print(plans.head())


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente todo este punto, sabías que datos transformar y como hacerlo, esto es un aspecto fundamental en analítica y ciencia de datos, adicionalmente hiciste verificaciones de duplicados y nulos lo cual es algo que si bien como te diste cuenta no representaba un problema es menester hacerlo en todo problema, también aprovechaste para añadir columnas útiles de una vez como el consumo en gb y el mes usando dt.month, muy bien Daniela!.
# </div>

# ## Estudiar las condiciones de las tarifas

# [Es sumamente importante entender cómo funcionan las tarifas, cómo se les cobra a los usuarios en función de su plan de suscripción. Así que te sugerimos imprimir la información de la tarifa para ver una vez más sus condiciones.]

# In[361]:


# Imprime las condiciones de la tarifa y asegúrate de que te quedan claras
print(plans.info())
print(plans.head())


# ## Agregar datos por usuario
# 
# [Ahora que los datos están limpios, agrega los datos por usuario y por periodo para que solo haya un registro por usuario y por periodo. Esto facilitará mucho el análisis posterior.]

# In[362]:


columns_calls ={
    'id':'id_calls'
    }
calls = calls.rename(columns=columns_calls )
print(calls)
columns_message ={
    'id':'id_message'
    }
messages = messages.rename(columns=columns_message )
print(messages)
columns_internet ={
    'id':'id_internet'
    }
internet = internet.rename(columns=columns_internet )
print(internet)


# In[363]:


# Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado.
calls_users = calls.groupby(['user_id','month']).count()
calls_users.rename(columns={'duration':'num_calls'}, inplace=True)
print(calls_users)


# In[364]:


# Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.
user_minute = calls.groupby(['user_id','month']).sum()
print(user_minute)


# In[365]:


user_minute['duration'] = np.ceil(user_minute['duration'])
print(user_minute)


# In[366]:


# Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado.
user_message = messages.groupby(['user_id','month']).count()
print(user_message)


# In[367]:


# Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado.
user_internet = internet.groupby(['user_id','month']).sum()
print(user_internet)


# In[368]:


user_internet['gb_used'] = user_internet['mb_used']/1024
user_internet['gb_used'] = np.ceil(user_internet['gb_used'])
print(user_internet)


# [Junta los datos agregados en un DataFrame para que haya un registro que represente lo que consumió un usuario único en un mes determinado.]

# In[369]:


# Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month
user_total = pd.concat([calls_users,user_minute,user_message,user_internet], axis='columns')
user_total = user_total.reset_index()
print(user_total)


# In[370]:


# Añade la información de la tarifa
columns_users ={
    'plan':'plan_name'
    }
users = users.rename(columns=columns_users )
plan_users = users.merge(plans, on='plan_name', how='outer')
print(plan_users)


# In[371]:


user_total = user_total.merge(plan_users, on='user_id')


# In[372]:


print(user_total.info())


# In[373]:


user_total=user_total.fillna(0)


# [Calcula los ingresos mensuales por usuario (resta el límite del paquete gratuito del número total de llamadas, mensajes de texto y datos; multiplica el resultado por el valor del plan de llamadas; añade la tarifa mensual en función del plan de llamadas). Nota: Dadas las condiciones del plan, ¡esto podría no ser tan trivial como un par de líneas! Así que no pasa nada si dedicas algo de tiempo a ello.]

# In[374]:


# Calcula el ingreso mensual para cada usuario

income_calls = (user_total['duration']-user_total['minutes_included'])
income_calls = np.where(income_calls<0,0,income_calls)*user_total['usd_per_minute']


income_messages = (user_total['id_message']-user_total['messages_included'])
income_messages = np.where(income_messages<0,0,income_messages)*user_total['usd_per_message']

income_internet = (user_total['gb_used']-user_total['gb_per_month_included'])
income_internet = np.where(income_internet<0,0,income_internet)*user_total['usd_per_gb']

user_total['income_user'] = (income_calls + income_messages + income_internet)+ user_total['usd_monthly_pay']
print(user_total['income_user'])


# In[375]:


user_total


# In[376]:


print(user_total.info())


# In[377]:


user_total.value_counts(user_total['plan_name']=='surf')


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien, tienes una excelente comprensión del problema, llegaste al objetivo de forma clara, calculaste la ganacia mes a mes para los gastos extra, esto es algo muy bien hecho, digo esto pues al estar esto bien cálculado todos los cálculos anteriores también!, solo un detalle, cuando calculas las llamadas, debido a que siempre las mantuviste excepto al final sin redondear puede haber imprecisión, pero particularmente me parece este un método más adecuado de solo hacer la aproximación al final, muy buen trabajo de nuevo Daniela.
# </div>

# ## Estudia el comportamiento de usuario

# [Calcula algunas estadísticas descriptivas para los datos agregados y fusionados que nos sean útiles y que muestren un panorama general captado por los datos. Dibuja gráficos útiles para facilitar la comprensión. Dado que la tarea principal es comparar las tarifas y decidir cuál es más rentable, las estadísticas y gráficas deben calcularse por tarifa.]
# 
# [En los comentarios hallarás pistas relevantes para las llamadas, pero no las hay para los mensajes e Internet. Sin embargo, el principio del estudio estadístico que se aplica para ellos es el mismo que para las llamadas.]

# ### Llamadas

# In[378]:


# Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.
calls_surf = user_total[user_total['plan_name']=='surf']
calls_surf = calls_surf.groupby('month').sum()
columnas_borrar = ['id_calls', 'call_date', 'num_calls', 'id_calls',
       'message_date','id_message', 'id_internet', 'mb_used',
       'gb_used', 'age', 'messages_included', 'mb_per_month_included',
       'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 'usd_per_message',
       'usd_per_minute', 'gb_per_month_included', 'income_user']
calls_surf = calls_surf.drop(columnas_borrar, axis=1)
calls_surf = calls_surf.reset_index()
print(calls_surf)
print(calls_surf.describe())


# In[379]:


mean_calls_surf = calls_surf['duration'].mean()
plt.figure(figsize=(10, 8))
sns.barplot(x='month', y='duration', data=calls_surf)
plt.axhline(mean_calls_surf, color='red', linestyle='dashed',linewidth=2, label='mean_calls_surf')


# In[380]:


# Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.
calls_ultimate = user_total[user_total['plan_name']=='ultimate']
calls_ultimate = calls_ultimate.groupby('month').sum()
columnas_borrar = ['id_calls', 'call_date', 'num_calls', 'id_calls',
       'message_date','id_message', 'id_internet', 'mb_used',
       'gb_used', 'age', 'messages_included', 'mb_per_month_included',
       'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 'usd_per_message',
       'usd_per_minute', 'gb_per_month_included', 'income_user']
calls_ultimate = calls_ultimate.drop(columnas_borrar, axis=1)
calls_ultimate = calls_ultimate.reset_index()
print(calls_ultimate)
print(calls_ultimate.describe())


# In[381]:


mean_calls_ultimate = calls_ultimate['duration'].mean()
plt.figure(figsize=(10, 8))
sns.barplot(x='month', y='duration', data=calls_ultimate)
plt.axhline(mean_calls_ultimate, color='red', linestyle='dashed',linewidth=2, label='mean_calls_ultimate')


# In[382]:


# Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.
user_total[user_total['plan_name']=='surf']['duration'].plot(kind='hist', bins=30)
user_total[user_total['plan_name']=='ultimate']['duration'].plot(kind='hist', bins=30, alpha=0.8)
plt.legend(['surf', 'ultimate'])
plt.show()


# [Calcula la media y la variable de la duración de las llamadas para averiguar si los usuarios de los distintos planes se comportan de forma diferente al realizar sus llamadas.]

# In[383]:


# Calcula la media y la varianza de la duración mensual de llamadas.
print(f'La media de la duracion de las llamadas del plan Surf es: {mean_calls_surf}')
print(f'La media de la duracion de las llamadas del plan Ultimate es: {mean_calls_ultimate}')


# In[384]:


variance_duration_surf= np.var(calls_surf['duration'])
variance_duration_ultimate= np.var(calls_ultimate['duration'])
print(f'La varianza de la duracion de las llamadas del plan Surf es: {variance_duration_surf}')
print(f'La varianza de la duracion de las llamadas del plan Ultimate es: {variance_duration_ultimate}')


# In[385]:


# Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas
x=calls_surf['duration']
y=calls_ultimate['duration']
caja_surf=plt.boxplot(x, vert=False, patch_artist=True, labels=['Calls'], boxprops=dict(facecolor='lightblue'))
caja_ultimate=plt.boxplot(y, vert=False, patch_artist=True, labels=['Calls'], boxprops=dict(facecolor='red'))
plt.title('Distribución de la duración mensual de llamadas')
plt.show()


# In[386]:


x1 = calls_surf['month']
y1 = calls_surf['duration']
x2 = calls_ultimate['month']
y2 = calls_ultimate['duration']
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(['Surf','Ultimate'])
plt.show()


# [Elabora las conclusiones sobre el comportamiento de los usuarios con respecto a las llamadas. ¿Su comportamiento varía en función del plan?]
# 
# Si, se observa que los usuarios con plan Surf suelen tener la mayor duración de llamadas a comparación de los usuarios con plan Ultimate, tambien vemos que la varianza es demasiada alta por lo que hay una mayor dispersion de los datos con respecto a su media.

# ### Mensajes

# In[387]:


# Comprara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan
message_surf = user_total[user_total['plan_name']=='surf']
message_surf = message_surf.groupby('month').sum()
message_surf = message_surf.reset_index()
columnas_borrar = ['id_calls', 'call_date', 'num_calls', 'id_calls',
       'duration','message_date', 'id_internet', 'mb_used',
       'gb_used', 'age', 'messages_included', 'mb_per_month_included',
       'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 'usd_per_message',
       'usd_per_minute', 'gb_per_month_included', 'income_user']
message_surf = message_surf.drop(columnas_borrar, axis=1)
print(message_surf.describe())
print(message_surf)


# In[388]:


message_surf.plot(kind='bar',x='month',y='id_message', color='orange')
plt.show()


# In[389]:


message_ultimate = user_total[user_total['plan_name']=='ultimate']
message_ultimate = message_ultimate.groupby('month').sum()
message_ultimate = message_ultimate.reset_index()
columnas_borrar = ['id_calls', 'call_date', 'num_calls', 'id_calls',
       'duration','message_date', 'id_internet', 'mb_used',
       'gb_used', 'age', 'messages_included', 'mb_per_month_included',
       'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 'usd_per_message',
       'usd_per_minute', 'gb_per_month_included', 'income_user']
message_ultimate = message_ultimate.drop(columnas_borrar, axis=1)
print(message_ultimate.describe())
print(message_ultimate)


# In[390]:


message_ultimate.plot(kind='bar', x='month', y='id_message', color='brown')
plt.show()


# In[391]:


plt.hist(message_surf['id_message'],bins=5)
plt.hist(message_ultimate['id_message'],bins=5, alpha=0.8)
plt.legend(['surf', 'ultimate'])
plt.show()


# In[392]:


x1 = message_surf['month']
y1 = message_surf['id_message']
x2 = message_ultimate['month']
y2 = message_ultimate['id_message']
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(['Surf','Ultimate'])
plt.show()


# [Elabora las conclusiones sobre el comportamiento de los usuarios con respecto a los mensajes. ¿Su comportamiento varía en función del plan?]

# ### Internet

# In[393]:


# Compara la cantidad de tráfico de Internet consumido por usuarios por plan
internet_surf = user_total[user_total['plan_name']=='surf']
internet_surf= internet_surf.groupby('month').sum()
internet_surf = internet_surf.reset_index()
columnas_borrar = ['id_calls', 'call_date', 'num_calls', 'id_calls',
       'duration', 'id_message', 'message_date','mb_used','age', 'messages_included', 'mb_per_month_included',
       'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 'usd_per_message',
       'usd_per_minute', 'gb_per_month_included', 'income_user','id_internet']
internet_surf = internet_surf.drop(columnas_borrar, axis=1)
print(internet_surf)
print(internet_surf['gb_used'].describe())


# In[394]:


internet_surf.plot(kind='bar',x='month',y='gb_used', color='orange')
plt.show()


# In[395]:


internet_ultimate = user_total[user_total['plan_name']=='ultimate']
internet_ultimate= internet_ultimate.groupby('month').sum()
internet_ultimate = internet_ultimate.reset_index()
columnas_borrar = ['id_calls', 'call_date', 'num_calls', 'id_calls',
       'duration', 'id_message', 'message_date','mb_used','age', 'messages_included', 'mb_per_month_included',
       'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 'usd_per_message',
       'usd_per_minute', 'gb_per_month_included', 'income_user','id_internet']
internet_ultimate = internet_ultimate.drop(columnas_borrar, axis=1)
print(internet_ultimate)
print(internet_ultimate['gb_used'].describe())


# In[396]:


internet_ultimate.plot(kind='bar',x='month',y='gb_used', color='brown')
plt.show()


# In[397]:


plt.hist(internet_surf['gb_used'],bins=5)
plt.hist(internet_ultimate['gb_used'],bins=5, alpha=0.8)
plt.legend(['surf', 'ultimate'])
plt.show()


# In[398]:


x1 = internet_surf['month']
y1 = internet_surf['gb_used']
x2 = internet_ultimate['month']
y2 = internet_ultimate['gb_used']
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(['Surf','Ultimate'])
plt.show()


# [Elabora las conclusiones sobre cómo los usuarios tienden a consumir el tráfico de Internet. ¿Su comportamiento varía en función del plan?]
# 
# Si, de acuerdo con el grafico los usuarios con plan Surf son los que más internet consumen gb, la tendencia es que tanto para los usuarios Surf y Ultimate, el uso de los gb va aumentando conforme pasan los meses.

# ## Ingreso

# [Del mismo modo que has estudiado el comportamiento de los usuarios, describe estadísticamente los ingresos de los planes.]

# In[399]:


user_total


# In[400]:


income_surf = user_total[user_total['plan_name']=='surf']
income_surf = income_surf.groupby(['month']).sum()
columns_borrar=['id_calls', 'call_date', 'num_calls', 'id_calls','message_date', 'id_internet', 'mb_used','age', 'messages_included', 'mb_per_month_included', 'minutes_included',
        'usd_per_gb', 'usd_per_message', 'usd_per_minute',
       'gb_per_month_included','duration' , 'id_message',  'gb_used']
income_surf = income_surf.drop(columns_borrar, axis=1)
print(income_surf)
print(income_surf.describe())

varianza = np.var(income_surf['income_user'])
print('La varianza es:\n')
print(varianza)


# In[401]:


income_surf = income_surf.reset_index()
y = income_surf['income_user']
x = income_surf['month']
surf=sns.barplot(x=x,y=y)
plt.show()


# In[402]:


income_ultimate = user_total[user_total['plan_name']=='ultimate']
income_ultimate = income_ultimate.groupby(['month']).sum()
income_ultimate.reset_index()
columns_borrar=['id_calls', 'call_date', 'num_calls', 'id_calls','message_date', 'id_internet', 'mb_used','age', 'messages_included', 'mb_per_month_included', 'minutes_included',
       'usd_monthly_pay', 'usd_per_gb', 'usd_per_message', 'usd_per_minute',
       'gb_per_month_included','duration' , 'id_message',  'gb_used']
income_ultimate = income_ultimate.drop(columns_borrar, axis=1)

print(income_ultimate)
print(income_ultimate.describe())

varianza = np.var(income_ultimate[['income_user']])
print('La varianza es:\n')
print(varianza)


# In[403]:


income_ultimate = income_ultimate.reset_index()
y = income_ultimate['income_user']
x = income_ultimate['month']
ultimate=sns.barplot(x=x,y=y)
plt.show()


# In[404]:


x1 = income_surf['month']
y1 = income_surf['income_user']
x2 = income_ultimate['month']
y2 = income_ultimate['income_user']
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(['Surf','Ultimate'])
plt.show()


# [Elabora las conclusiones sobre cómo difiere el ingreso entre los planes.]
# 
# La varianza de los ingresos por usuario esta relativamente alta, por lo que su dispersion con respecto a la media es alta. 
# Se puede ver en el diagrama de lineas que el plan Surf es el que tiene mayores ingresos mientras que el plan Ultimate tiene un crecimiento no tan alto pero constante.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Un espectacular análisis gráfico Daniela, entendiste el punto de un análisis de este tipo, hiciste un estudio bastante amplio para cada caso, usaste diversas gráficas y aportaste conclusiones acertadas respecto al desarrollo del proyecto, de nuevo poco que añadir más allá de elogiar este tipo de esfuerzos.
# </div>

# ## Prueba las hipótesis estadísticas

# [Prueba la hipótesis de que son diferentes los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf.]

# [Elabora las hipótesis nula y alternativa, escoge la prueba estadística, determina el valor alfa.]

# In[405]:


user_total


# In[406]:


# Prueba las hipótesis
income_hipotesis_surf = user_total[user_total['plan_name']=='surf']
columns_borrar=['id_calls', 'call_date', 'num_calls', 'id_calls',
       'duration', 'id_message', 'message_date', 'id_internet', 'mb_used',
       'gb_used', 'first_name', 'last_name', 'age', 'city', 'reg_date',
       'plan_name', 'churn_date', 'messages_included', 'mb_per_month_included',
       'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 'usd_per_message',
       'usd_per_minute', 'gb_per_month_included', 'month', 'user_id']
income_hipotesis_surf = income_hipotesis_surf.drop(columns_borrar, axis=1)
print(income_hipotesis_surf)


# In[407]:


income_hipotesis_ultimate = user_total[user_total['plan_name']=='ultimate']
columns_borrar=['id_calls', 'call_date', 'num_calls', 'id_calls',
       'duration', 'id_message', 'message_date', 'id_internet', 'mb_used',
       'gb_used', 'first_name', 'last_name', 'age', 'city', 'reg_date',
       'plan_name', 'churn_date', 'messages_included', 'mb_per_month_included',
       'minutes_included', 'usd_monthly_pay', 'usd_per_gb', 'usd_per_message',
       'usd_per_minute', 'gb_per_month_included', 'month', 'user_id']
income_hipotesis_ultimate = income_hipotesis_ultimate.drop(columns_borrar, axis=1)
print(income_hipotesis_ultimate)


# In[408]:


income_surf_mean = np.mean(income_hipotesis_surf['income_user'])
income_ultimate_mean = np.mean(income_hipotesis_ultimate['income_user'])
print(f'El promedio de los ingresos del plan Surf es: {income_surf_mean}\n')
print(f'El promedio de los ingresos del plan Ultimate es: {income_ultimate_mean}\n')


# [Prueba la hipótesis de que el ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.]

# In[409]:


user_total['city']


# In[410]:


ny_nj = 'NY-NJ'
user_ny = user_total[user_total['city'].str.contains(ny_nj, case=False)]

columns_borrar=['id_calls', 'call_date', 'num_calls', 'id_calls', 'duration',
       'id_message', 'message_date', 'id_internet', 'mb_used', 'gb_used',
       'age', 'messages_included', 'mb_per_month_included', 'minutes_included',
       'usd_monthly_pay', 'usd_per_gb', 'usd_per_message', 'usd_per_minute',
       'gb_per_month_included','user_id', 'month', 'first_name', 'last_name', 'city', 'reg_date',
       'plan_name', 'churn_date']
user_ny = user_ny.drop(columns_borrar, axis=1)
user_ny_mean = user_ny['income_user'].mean()
print(user_ny)
print(f'El promedio de ingresos para los habitantes de NY-NJ es de: {user_ny_mean}')


# In[411]:


ny_nj = 'NY-NJ'
user_other = user_total[~user_total['city'].str.contains(ny_nj, case=False)]

columns_borrar=['id_calls', 'call_date', 'num_calls', 'id_calls', 'duration',
       'id_message', 'message_date', 'id_internet', 'mb_used', 'gb_used',
       'age', 'messages_included', 'mb_per_month_included', 'minutes_included',
       'usd_monthly_pay', 'usd_per_gb', 'usd_per_message', 'usd_per_minute',
       'gb_per_month_included','user_id', 'month', 'first_name', 'last_name', 'city', 'reg_date',
       'plan_name', 'churn_date']
user_other = user_other.drop(columns_borrar, axis=1)
user_other_mean = user_other['income_user'].mean()

print(user_other)
print(f'El promedio de ingresos para los habitantes de NY-NJ es de: {user_other_mean}')


# [Elabora las hipótesis nula y alternativa, escoge la prueba estadística, determina el valor alfa.]

# In[412]:


# Prueba las hipótesis
# Ingreso promedio del plan Surf es igual al ingreso promedio del plan Ultimate

alpha=0.05
results = st.ttest_ind(user_ny,income_hipotesis_ultimate)
print('valor p: ', results.pvalue) 

if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")


# In[413]:


# Ingreso promedio de surf es diferente al plan ultimate

alpha=0.05
results = st.ttest_ind(user_ny,user_other)
print('valor p: ', results.pvalue) 

if results.pvalue < alpha:
    print("Rechazamos la hipótesis alternativa")
else:
    print("No podemos rechazar la hipótesis alternativa")


# Conclusiones
# 
# Después de terminar el proyecto, enumerare y explicare como fui resolviéndolo.
# Primera parte. Extracción y Transformación de datos
# 1.	Se cargaron las librerías que necesitaríamos durante la realización del proyecto. En este caso fueron varias, tales como:
#     a.	Pandas
#     b.	Numpy
#     c.	Scipy
#     d.	Matplotlib
#     e.	Seaborn
# 2.	Se cargaron los datos de cada dataset con la ayuda de la librería de pandas. Se visualizo la información de cada dataset para conocer sus atributos y posterior a eso, se realizaron algunos cambios para poder trabajar con los datos, esencialmente se cambiaron los tipos de datos de algunos datasets.
# 3.	Se empezó por analizar el dataset de Usuarios (users)
#     a.	Se busco que no hubiera datos NULL/NAN, lo cual nos arrojó que no existían esos datos dentro de nuestro dataset.
# 4.	Seguido del dataset de Llamadas (calls)
#     a.	Se busco que no hubiera datos NULL/NAN, lo cual nos arrojó que no existían esos datos dentro de nuestro dataset.
#     b.	Se especifico con el método dt.month una nueva columna que solo nos mostrara el mes
# 5.	Siguiendo con el dataset de Mensajes (messages)
#     a.	Se busco que no hubiera datos NULL/NAN, lo cual nos arrojó que no existían esos datos dentro de nuestro dataset.
#     b.	Se especifico con el método dt.month una nueva columna que solo nos mostrara el mes
# 6.	Por último el dataset de Internet (internet)
#     a.	Se busco que no hubiera datos NULL/NAN, lo cual nos arrojó que no existían esos datos dentro de nuestro dataset.
#     b.	Se especifico con el método dt.month una nueva columna que solo nos mostrara el mes
#     c.	Se realizaron las conversiones en la columna “mb_per_month_inclueded” y se genero una nueva columna para que los megas se conviertan en gigas llamada “gb_per_month_inclueded”
#     
# Segunda Parte. Análisis de los datos
# 1.	Se cambiaron algunos nombres de columnas para que no interfiriera con el análisis, exista confusiones, nos muestre un error o haya alguna duplicidad.
# 2.	Se crearon nuevas variables para cada dataset que estaremos analizando (Llamadas, Mensajes e Internet) y así agrupar por “month” y “user_id”.
# 3.	Con el método np.ceil  que nos ofrece la librería de numpy, se hicieron las conversiones numéricas para redondear los datos necesarios de cada dataset.
# 4.	Con el método pd.concat de la libreria de pandas, se creo un nuevo dataset que uniera los datasets ya transformados de Llamadas, Mensajes e Internet llamada user_total.
# 5.	Para poder unir user_total y poder saber que tipo de planes tienen los usuarios, se tuvo que hacer lo siguiente:
#     a.	Usar el método merge para unir el dataset de users y el de plans, con la ayuda de la llave que tienen en común, “plans”. Con esto, se crea un nuevo dataset llamado plan_users.
#     b.	Se usará nuevamente la función de merge pero para combinar plan_users con user_total.
#     c.	Los registros que tengan algún tipo de dato NULL o NAN, se usará fillna( ) para poner estos datos en cero.
# 6.	Se calcula el ingreso mensual para cada usuario.
#     a.	Se usa el método np.where que nos da la librería de Numpy para que si existen resultados negativos, nos lo ponga en cero.
#     
# Tercera Parte. Visualización de los datos
# 1.	Se compara la duración promedio de llamadas por cada plan y cada mes. 
#     a.	Esto nos muestra que las llamadas van en aumento conforme pasan los meses, tanto para los usuarios con plan Surf y los usuarios de plan Ultimate, otra cosa que podemos ver es que los usuarios Surf tienden a tener duraciones de llamadas más altas (53121.58) que los usuarios Ultimate(24402.5) gracias a la media de cada uno. 
# 2.	Se compara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan.
#     a.	Esto nos muestra que los mensajes van en aumento conforme pasan los meses, tanto para los usuarios con plan Surf y los usuarios de plan Ultimate, otra cosa que podemos ver es que los usuarios Surf mandan más mensajes (4084.5) que los usuarios Ultimate(2253.08) gracias a la media de cada uno. 
# 3.	Se compara la cantidad de tráfico de internet consumido por los usuarios de cada plan.
#     a.	Esto nos muestra que el consumo de internet va en aumento conforme pasan los meses, tanto para los usuarios con plan Surf y los usuarios de plan Ultimate, otra cosa que podemos ver es que los usuarios Surf consumen más internet (2185.25) que los usuarios Ultimate(1038.41) gracias a la media de cada uno. 
# 4.	Se comparan los ingresos de los dos planes.
#     a.	El ingreso medio del plan Surf es de 7908.51 y el ingreso medio del plan Ultimate es de 4338.84.
# 
# Para esta parte, se concluye que hay muchos más usuarios utilizando y pagando el plan surf, esto debido a que es un plan económico comparándolo con el plan Ultimate. Sin embargo, a pesar de eso, son los que más consumen tanto llamadas, mensajes e internet, por lo que llegan a pagar más de lo que originalmente deberían. Esto hace, en mi opinión, que el plan Ultimate sea el más viable para un usuario, esto a pesar de que es el más caro, pero no se tiende a pagar un extra por consumo excesivo.
# 
# 
# Cuarta Parte. Prueba las hipótesis estadísticas.
# Se elaboraron dos hipótesis, nula y alternativa. 
# La hipótesis nula nos dice lo siguiente:
# -	El promedio de los ingresos del plan Surf es igual a los ingresos del plan Ultimate. 
# La hipótesis alternativa nos dice lo siguiente:
# -	El promedio de los ingresos del plan Surf es diferente a los ingresos del plan Ultimate. 
# 
# La hipótesis nula nos dice lo siguiente:
# -	El promedio de los ingresos de una población, en este caso, NY-NJ es igual a los ingresos de otras regiones
# La hipótesis alternativa nos dice lo siguiente:
# -	El promedio de los ingresos de una población, en este caso, NY-NJ es diferente a los ingresos de otras regiones
# 
# En ambos casos se rechaza la hipótesis nula y nos quedamos con la hipótesis alternativa. 
# Las medias o promedio que se tiene en los ingresos del plan Surf y Ultimate son diferentes. Lo mismo sucede con la segunda hipótesis, el promedio o media de los ingresos de NY-NJ son diferentes con los ingresos de los usuarios de las otras regiones.
# 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Otra vez, un excelente trabajo y una excelente finalización, aunque un pequeño detalle, no es necesario crear una lista con todas las columnas que quieres borrar, si quieres seleccionar una columna y usar un df en lugar de una serie (aunque para la prueba de hipótesis es mejor una serie) es solo usar df = df[['column']] en lugar de hacerle drop a todas las columnas y quedarte con la que te interesa pues se puede volver un proceso bastante tedioso.
# </div>
