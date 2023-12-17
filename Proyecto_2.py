#!/usr/bin/env python
# coding: utf-8

# # Hola Daniela!
# 
# Mi nombre es David Bautista, soy code reviewer de Tripleten y hoy tengo el gusto de revisar tu proyecto.
# 
# Cuando vea un error la primera vez, lo señalaré. Deberás encontrarlo y arreglarlo. La intención es que te prepares para un espacio real de trabajo. En un trabajo, el líder de tu equipo hará lo mismo. Si no puedes solucionar el error, te daré más información en la próxima ocasión.
# 
# Encontrarás mis comentarios más abajo - por favor, no los muevas, no los modifiques ni los borres.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# 
# <div class="alert alert-block alert-danger">
#     
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
#     
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# 
# Puedes responderme de esta forma: 
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# </div>
# 
# ¡Empecemos!

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypotheses)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
#     * [3.2 Hipótesis 2: preferencias musicales los lunes y los viernes](#week)
#     * [3.3 Hipótesis 3: preferencias de género en Springfield y Shelbyville](#genre)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; y otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar las hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba tres hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 2. Los lunes por la mañana, los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre los viernes por la noche.
# 3. Los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap.
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar las hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos
#  2. Preprocesamiento de datos
#  3. Prueba de hipótesis
# 
# 
# ### Desafío
# 
# En este proyecto, preparamos un pequeño reto para ti. Incluimos un nuevo tipo de estructura de datos: las marcas temporales. Las marcas temporales son muy comunes y merecen una atención adicional. Más adelante en el programa, aprenderás mucho sobre ellas. Sin embargo, por ahora las trataremos como simples strings. Necesitamos marcas temporales en este proyecto para poner a prueba una de nuestras hipótesis. No te preocupes, te ayudaremos con esto. Tu nivel de conocimientos actual será suficiente para abordarlo.
# 
# Por ejemplo, digamos que tenemos dos marcas temporales: `dt1 = "12:00:00"` y `dt2 = "06:00:00"`. Queremos comparar estas dos marcas temporales y ver cuál es posterior.
# 
# Podemos compararlas mediante los operadores de comparación estándar (`<`, `>`, `<=`, `>=`, `==`, `!=`). Ejecuta la siguiente celda de código para comparar dos marcas temporales:
# 

# In[24]:


# Comparar los objetos datetime

dt1 = "12:00:00"
dt2 = "06:00:00"

if dt1 < dt2:
    print("La marca temporal 2 es posterior")
else:
    print("La marca temporal 1 es posterior")


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo con el reto, recuerda que para todo los proyectos que realices es importante genera un contexto donde se comente que trata el caso y cuáles con los objetivos a cumplir, además es indispensable que se genere una tabla de contenido con el fin de mantener el orden en la entrega.
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos en Y.Music y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[25]:


# importar pandas
import pandas as pd


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#    
# Buen trabajo importando la librería ``pandas``
# </div>

# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[26]:


# Leer el archivo y almacenarlo en df
df = pd.read_csv("/datasets/music_project_en.csv")


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Cargaste correctamente la base de datos
# </div>

# Muestra las 10 primeras filas de la tabla:

# In[27]:


# Obtener las 10 primeras filas de la tabla df
df.head(10)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Empleas correctamente el método ``.head()``</div>

# Obtén la información general sobre la tabla con un comando:

# In[28]:


# Obtener información general sobre los datos en df
df.info()


# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Todas almacenan el mismo tipo de datos: `object` (objeto).
# 
# Según la documentación:
# - `' userID'` — identificador del usuario o la usuaria;
# - `'Track'` — título de la canción;
# - `'artist'` — nombre del artista;
# - `'genre'` — género musical;
# - `'City'` — ciudad del usuario o la usuaria;
# - `'time'` — hora exacta en la que se reprodujo la canción;
# - `'Day'` — día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas; otros, en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. Existen datos NaN
# 4. 'userID'podría manejarse como 'user_ID'
# 
# 
# 

# ### Tus observaciones <a id='data_review_conclusions'></a>
# 
# `Escribe tus observaciones aquí:
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?
#         Se tienen datos NaN, con el metodo info(), podemos ver que el tipo de dato es 'object'
#         
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestras tres hipótesis o necesitamos más información?
#         Si se tiene la informacion necesaria para probar las hipotesis
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?'
#         Al tener datos NaN habria que revisar si se pueden reemplazar o se eliminan, en las 10 primeras filas no reconozco que existan valores duplicados, seria cosa de utilizar el metodo correspondiente para verificarlo y al ser datos 'object' pero teniendo el tiempo podria usarse como float64 `

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Tus respuestas son  correctas, buen trabajo en esta sección!</div>

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla:

# In[29]:


# La lista de encabezados para la tabla df
print(df.columns)


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * todos los caracteres deben ser minúsculas;
# * elimina los espacios;
# * si el nombre tiene varias palabras, utiliza snake_case.

# Pon todos los caracteres en minúsculas y muestra el encabezado de la tabla de nuevo:

# In[30]:


new_col_names=[]
for old_name in df:
    name_lowered = old_name.lower()
    name_stripped = name_lowered.strip()
    new_col_names.append(name_stripped)

df.columns=new_col_names
print(df.columns)


# In[31]:


columns_new = {
    'userid':'user_id'
}

df.rename(columns = columns_new,inplace=True)


# In[ ]:





# Aplica snake_case al encabezado userID y muestra el encabezado de la tabla:

# In[ ]:





# Comprueba el resultado. Muestra los encabezados una vez más:

# In[32]:


print(df.columns)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo Daniela, cuando no emplees una celda de código es preferible que la elimines para que el proyecto se vea más organizado.
# </div>

# [Volver a Contenidos](#back)

# ### MissValores ausentes <a id='missing_values'></a>
# Primero, encuentra el número de valores ausentes en la tabla. Para ello, utiliza dos métodos pandas:

# In[33]:


print(df.isna().sum())


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Para hacer esto, crea la lista `columns_to_replace`, recórrela con un bucle `for` y reemplaza los valores ausentes en cada columna:

# In[34]:


# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'

columns_to_replace=['track','artist','genre']
for ausentes in columns_to_replace:
    df[ausentes].fillna('unknown', inplace=True)


# Asegúrate de que la tabla no contiene más valores ausentes. Cuenta de nuevo los valores ausentes.

# In[35]:


print(df.isna().sum())


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Utilizaste el bucle ``for`` de manera correcta para lidear con los valores nulos.</div>

# [Volver a Contenidos](#back)

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla usando un comando:

# In[36]:


# Contar duplicados explícitos
print(df.duplicated().sum())


# Llama al método `pandas` para deshacerte de los duplicados explícitos:

# In[37]:


# Eliminar duplicados explícitos
df.drop_duplicates(inplace=True)


# Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[38]:


# Comprobación de duplicados
print(df.duplicated().sum())


# In[39]:


df = df.drop_duplicates().reset_index(drop=True) 


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Buen trabajo en esta sección, pero recuerdes que siempre elimines duplicados esto puede generar problemas en la indexación de la tabla. Para resolver este problema, puedes seguir este ejemplo:~
#     
# ```python
# df = df.drop_duplicates().reset_index(drop=True)    
# ```    
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto    
# </div>

# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para hacerlo:
# * recupera la columna deseada del dataFrame;
# * llama al método que te devolverá todos los valores de columna únicos;
# * aplica un método de ordenamiento a tu resultado.
# 

# In[40]:


# Inspeccionando los nombres de géneros únicos
print(df['genre'].unique())


# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, declara la función `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=` — la lista de duplicados;
# * `correct_genre=` — el string con el valor correcto.
# 
# La función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplaza cada valor de la lista `wrong_genres` con el valor en `correct_genre`. Utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos y reemplazarlos con el género correcto en la lista principal.

# In[41]:


# Función para reemplazar duplicados implícitos
def replace_wrong_genres(df,column,wrong_genres,correct_genre):
    for wrong_genre in wrong_genres:
        df[column]=df[column].replace(wrong_genre,correct_genre)
    return df


# Llama a `replace_wrong_genres()` y pásale argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[42]:


# Eliminar duplicados implícitos
duplicates = ['hip','hop','hip-hop']
name='hiphop'
df = replace_wrong_genres(df,'genre',duplicates,name)


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[43]:


# Comprobación de duplicados implícitos
print(df['genre'].unique())


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Te recomiendo emplear el método ``.unique()`` para corrobar que no existan duplicados implícitos!~~
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2 </b> <a class="tocSkip"></a>
#     
# Buen trabajo Daniela </div>

# [Volver a Contenidos](#back)

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Primeramente, por lo que veo puedo decir que estamos haciendo un proceso ETL, donde el primer paso es la extraccion de los datos, los cuales los obtuvimos desde un archivo de tipo CVS, gracias a la libreria pandas pudimos obtener el DF de este.
# El segundo paso seria obtener la información del archivo, para esto se utilizo el metodo .info(), y observamos que las columnas tienen errores de sintaxis. Este paso dentro del proceso ETL es la transformación, aqui se abordara de manera en que cambiemos algunas cosas de nuestro DF o en general limpiemos nuestros datos para poder trabajar en ellos. Para esto se cambiaron los nombres de las columnas, se buscaron datos NaN y datos duplicados para despues borrarlos (se usaron varios metodos como: drop.duplicates, duplicated, sum, count, isna, fillna). Con el metodo unique() se observa que en la columna genre se tienen datos iguales pero escritos de manera diferente por lo que haremos una funcion que nos corrija estos nombres y quede homogeneo`

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Has realizado un buen trabajo con los duplicados explícitos e implícitos!   
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypotheses'></a>

# ### Hipótesis 1: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La primera hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[44]:


# Contando las canciones reproducidas en cada ciudad
df.groupby('city').count()


# Al agrupar por ciudad se observa que la ciudad de Shelbyville es la que tiene mayor usuarios por lo tanto tiene mayores reproducciones de canciones y generos.

# In[45]:


track_day = df.groupby('day')['track'].count()
print(track_day)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Te recomiendo que además de agrupar por ciudad lo hagas por la variable ``track`` (Agrupa por día y por reproducciones). Crea una variable que almacene el número de canciones reproducidad en cada ciudad. Tampoco olvides realizar tus observaciones.~
#     
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#   
# # Importante
#  
# ~~Debes agrupar por la variable ``track``  para esta sección en general.~~
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a>
#   
# ~~Creo que hubo una confusión em la explicación que te di, el ideal es agrupar los dias par apoder contar la variable ``track``. te mostrare como:~~
# 
# ```python
# df.groupby('day')['track'].count()    
# ```
#     
# ~~Esa tabla que hiciste agrupando ``track`` esta mal, debes eliminarla.~~
# </div>

# Ahora agrupa los datos por día de la semana y encuentra el número de canciones reproducidas el lunes, miércoles y viernes.
# 

# In[46]:


# calculando las canciones reproducidas en cada uno de los tres días
df.groupby(by='day').count()


# In[47]:


track_city = df.groupby('city')['track'].count()

print(track_city)


# `Comenta tus observaciones aquí`

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Te recomiendo que además de agrupar por ciudad lo hagas por la variable ``track`` (Agrupa por ciudad y por reproducciones). Crea una variable que almacene las canciones reproducidad en cada día. Tampoco olvides realizar tus observaciones.~
#     
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# ~~Buen trabajo pero te faltan las observaciones~~  
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #4</b> <a class="tocSkip"></a>
#   
# Buen trabajo Daniela.
# </div>

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la `number_tracks()` para calcular el número de canciones reproducidas en un determinado día y ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'`.
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[48]:


# <creando la función number_tracks()>
# Declararemos la función con dos parámetros: day=, city=.
# Deja que la variable track_list almacene las filas df en las que
# el valor del nombre de la columna ‘day’ sea igual al parámetro day= y, al mismo tiempo,
# el valor del nombre de la columna ‘city’ sea igual al parámetro city= (aplica el filtrado consecutivo
# con la indexación lógica).
# deja que la variable track_list_count almacene el número de valores de la columna 'user_id' en track_list
# (igual al número de filas en track_list después de filtrar dos veces).
# permite que la función devuelva un número: el valor de track_list_count.

# La función cuenta las pistas reproducidas en un cierto día y ciudad.
# Primero recupera las filas del día deseado de la tabla,
# después filtra las filas de la ciudad deseada del resultado,
# luego encuentra el número de canciones en la tabla filtrada,
# y devuelve ese número.
# Para ver lo que devuelve, envuelve la llamada de la función en print().


# comienza a escribir tu código aquí
def number_tracks(day,city):
    track_list = df[(df['day']== day) & (df['city']== city)]
    track_list_count = track_list['user_id'].count()
    return (track_list_count)


#  <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Buen trabajo creando la función, sin embargo te recomiendo que anides las condiciones, te dejo una guía:~
# ```python
# col_name = df[(df['column']==column) & (df['column2']== column2)]
# ```
# </div>
# 
#  <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2 </b> <a class="tocSkip"></a>
#     
# Genial
# </div>

# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[49]:


# El número de canciones reproducidas en Springfield el lunes
tracks_monday_spr=number_tracks('Monday','Springfield')


# In[50]:


# El número de canciones reproducidas en Shelbyville el lunes
tracks_monday_shell=number_tracks('Friday','Shelbyville')


# In[51]:


# El número de canciones reproducidas en Springfield el miércoles
tracks_wednesday_spr=number_tracks('Wednesday','Springfield')


# In[52]:


# El número de canciones reproducidas en Shelbyville el miércoles
tracks_wednesday_shell=number_tracks('Wednesday','Shelbyville')


# In[53]:


# El número de canciones reproducidas en Springfield el viernes
tracks_friday_spr=number_tracks('Friday','Springfield')


# In[54]:


# El número de canciones reproducidas en Shelbyville el viernes
tracks_friday_shell=number_tracks('Friday','Shelbyville')


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Puedes crear variables para cada valor calculado. Por ejemplo para el número de canciones reproducidas en Shelbyville el dia viernes puedes crear una variable llamada ``tracks_friday_shell``~ </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2 </b> <a class="tocSkip"></a>
#     
# Muy buen trabajo Daniela!</div>

# Utiliza `pd.DataFrame` para crear una tabla, donde
# * Los encabezados de la tabla son: `['city', 'monday', 'wednesday', 'friday']`
# * Los datos son los resultados que conseguiste de `number_tracks()`

# In[55]:


# Tabla con los resultados

number=[
    ['Springfield',tracks_monday_spr,tracks_wednesday_spr,tracks_friday_spr],
    ['Shelbyville',tracks_monday_shell,tracks_wednesday_shell,tracks_friday_shell]
]

hipotesis1=['city', 'monday', 'wednesday', 'friday']

            
tabla_resultados = pd.DataFrame(data = number,columns = hipotesis1)

print(tabla_resultados)


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# ~En lugar de digitar manualmente el número de reproducciones por día y por ciudad, emplea las variables que te sugerí que crearas para crear la tabla.~
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2 </b> <a class="tocSkip"></a>
# 
# Buen trabajo!
# </div>
# 

# **Conclusiones**
# 
# `Considero que podria ser parcialmente aceptada, ya que si podemos afirmar que depende de la ciudad y el dia, la actividad de los usuarios cambia, sin embargo, no hay una gran diferencia, en este caso, los dias miercoles en Springfield la actividad es menor a comparacion de los dias lunes y viernes, y para Shelbyville es casi lo mismo, solo que aqui el miercoles es cuando mas actividad se tiene y lunes y viernes se mantiene constante`

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#    
# Buenas conclusiones!
# </div>

# [Volver a Contenidos](#back)

# ### Hipótesis 2: música al principio y al final de la semana <a id='week'></a>

# Según la segunda hipótesis, el lunes por la mañana y el viernes por la noche, los ciudadanos de Springfield escuchan géneros diferentes a los que disfrutan los usuarios de Shelbyville.

# Cree dos tablas con los nombres proporcionados en los dos bloques de código siguientes:
# * Para Springfield — `spr_general`
# * Para Shelbyville — `shel_general`

# In[67]:


# cree la tabla spr_general a partir de las filas df
# donde el valor en la columna 'city' es 'Springfield'
spr_general = df[df['city']== 'Springfield']


# In[68]:


# crea shel_general a partir de las filas df
# donde el valor en la columna 'city' es 'Shelbyville'

shel_general  = df[df['city']== 'Shelbyville']


# Escribe la función `genre_weekday()` con cuatro parámetros:
# * Una tabla para los datos (`df`)
# * El día de la semana (`day`)
# * La primera marca de tiempo, en formato (`time1`)
# * La última marca de tiempo, en formato (`time2`)
# 
# La función debería devolver información de los 15 géneros más populares de un día determinado en un período entre dos marcas de fecha y hora.
# Aplique la misma lógica de filtrado consecutivo, pero esta vez utilice cuatro filtros y luego cree una nueva columna con los respectivos recuentos de reproducción.
# Ordene el resultado de mayor a menor y devuélvalo.

# In[69]:


# 1) Deja que la variable genre_df almacene las filas que cumplen varias condiciones:
#    - el valor de la columna 'day' es igual al valor del argumento day=
#    - el valor de la columna 'time' es mayor que el valor del argumento time1=
#    - el valor en la columna 'time' es menor que el valor del argumento time2=
#    Utiliza un filtrado consecutivo con indexación lógica.

# 2) Agrupa genre_df por la columna 'genre', toma una de sus columnas,
#    y use el método size() para encontrar el número de entradas para cada una de
#    los géneros representados; almacena los Series resultantes en
#    la variable genre_df_count    

# 3) Ordena genre_df_count en orden descendente de frecuencia y guarda el resultado
#    en la variable genre_df_sorted


# 4) Devuelve un objeto Series con los primeros 15 valores de genre_df_sorted - los 15
#    géneros más populares (en un determinado día, en un determinado periodo de tiempo)

# Escribe tu función aquí
def genre_weekday(df,day,time1,time2):
    genre_df = df[(df['day']== day) & (df['time'] < time2) & (df['time'] > time1)] 
    genre_df_count = genre_df.groupby('genre')['genre'].count() 
    genre_df_sorted = genre_df_count.sort_values(ascending=False)          
    return genre_df_sorted[:15]


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~De nuevo puedes anidar las condiciones para la función en una sola línea de código como te lo indique anteriormente. Te dejo una guía:~
# ```python
# df = df[(condicion_1) & (condicion_2) & (condicion_3)]
# ```
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2 </b> <a class="tocSkip"></a>
#     
# Mucho mejor!
# 
# </div>

# Compara los resultados de la función `genre_weekday()`para Springfield y Shelbyville el lunes por la mañana (de 7 a 11) y el viernes por la tarde (de 17:00 a 23:00). Utilice el mismo formato de 24 horas que el conjunto de datos (por ejemplo, 05:00 = 17:00:00):

# In[70]:


# llamando a la función para el lunes por la mañana en Springfield (utilizando spr_general en vez de la tabla df)
genre_weekday(spr_general,'Monday','07:00','11:00')


# In[60]:


# llamando a la función para el lunes por la mañana en Shelbyville (utilizando shel_general en vez de la tabla df)
genre_weekday(shel_general,'Monday','07:00','11:00')


# In[61]:


# llamando a la función para el viernes por la tarde en Springfield
genre_weekday(spr_general,'Friday','17:00','23:00')


# In[62]:


# llamando a la función para el viernes por la tarde en Shelbyville
genre_weekday(shel_general,'Friday','17:00','23:00')


# **Conclusión**
# 
# `Considero, nuevamente que esta hipótesis es parcialmente aceptada. Los datos muestran que al menos los primero 4 generos que encabezan para las dos ciudad son:
# pop            
# rock           
# electronic     
# dance          
# no se tiene una variable diferente, es decir, pop se mantiene siempre en el 1er lugar y no baja de rango o se sustituye por algun otro genero como rap o classical, por lo que no se podria afirmar al 100% que depende del dia y hora, el genero es diferente`

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo
# </div>

# [Volver a Contenidos](#back)

# ### Hipótesis 3: preferencias de género en Springfield y Shelbyville <a id='genre'></a>
# 
# Hipótesis: Shelbyville ama la música rap. A los residentes de Springfield les gusta más el pop.

# Agrupa la tabla `spr_general` por género y encuentra el número de canciones reproducidas de cada género con el método `count()`. Después, ordena el resultado en orden descendente y guárdalo en `spr_genres`.

# In[73]:


# Escribe una línea de código que:
# 1. agrupe la tabla spr_general por la columna 'genre';
spr_genres=spr_general.groupby('genre')['genre'].count().sort_values(ascending=False)


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Nuevamente puedes anidar los métodos para la función en una sola línea de código como te lo indique anteriormente.~
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor # 2 </b> <a class="tocSkip"></a>
#  
# # Importante
#     
# ~~Revisa cuidadosamente tu script, no obtienes el output esperado.~~</div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #  3</b> <a class="tocSkip"></a>
#  
# ~~Verifica como estas realizando los agrupamientos y sobre que tablas.~~</div>

# Muestra las 10 primeras filas de `spr_genres`:

# In[75]:


# mostrar las 10 primeras filas de spr_genres
spr_genres.head(10)


# Ahora haz lo mismo con los datos de Shelbyville.
# 
# Agrupa la tabla `shel_general` por género y encuentra el número de canciones reproducidas de cada género. Después, ordena el resultado en orden descendente y guárdalo en la tabla `shel_genres`:
# 

# In[76]:


# Escribe una línea de código que:
# 1. agrupe la tabla shel_general por la columna 'genre';
shel_genres=shel_general.groupby('genre')['genre'].count().sort_values(ascending=False)

# 3. ordene el Series resultante en orden descendente y lo guarde en shel_genres.


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Nuevamente puedes anidar los métodos para la función en una sola línea de código como te lo indique anteriormente. ~~
# </div>

# Muestra las 10 primeras filas de `shel_genres`:

# In[77]:


# Muestra las 10 primeras filas de shel_genres
shel_genres.head(10)


# [Volver a Contenidos](#back)

# `Para este caso, seria rechazada totalmente, la hipótesis nos dice "En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap", pero en Springfield prefieren el genero world y en Shelbyville se tienen varios generos como rock, alternative, folk, no figura dentro de estos datos el rap.`

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #4</b> <a class="tocSkip"></a>
#   
# Buen trabajo Daniela.
# </div>

# # Conclusiones <a id='end'></a>

# `En conclusion final
# 1. Shelbyville es la ciudad que tiene mas usuarios por ende;
# 2. Mas reproducciones, los generos pop, dance, electronic son los mas escuchados en ambas ciudades;
# 3. las reproducciones si varian por día pero no es una variación significativa.`

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Esta sección te pide conclusiones respecto a las 3 hipótesis.~</div>

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General
# 
# ~~Hola Daniela, te felicito en general realizaste un muy trabajo, deje unos comentarios para que los tengas en cuenta en una próxima entrega. Pronto finalizarás tu proyecto, que estés bien!~~
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #2
# 
# ~~Hola Daniela, tienes algunos inconvientes con los códigos de la hipótesis 3 revisalos cuidadosamente y no vemos en una próxima entrega!~~
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #3
# 
# ~~Hola Daniela, he dejado nuevos comentarios etiquetados con el #3 para que los puedas tener en cuenta.~~
# </div>
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #4
# 
# Hola Daniela, te felicito por la culminación del proyecto.
# </div>
