#!/usr/bin/env python
# coding: utf-8

# Hola Daniela!
# 
# Mi nombre es Miguel Gutierrez y revisare tu proyecto ! Para darte un contexto, trabajo como cientifico de datos en Mercado Libre. Asi que seras revisado por alguien que aplica a diario todo este tipo de tecnicas en su vida laboral ! Espero una vez finalizes este bootcamp, tambien lo apliques ! Buena suerte !
# 
# Cuando vea un error la primera vez, lo señalare. Dejare que encuentres la solucion. Tambien en el texto hare algunas observaciones de como podrias mejorar el codio y tambien hare comentarios de tus percepciones sobre el tema. Si no pueds manejar la tarea, te dare una pista precisa en la siguiente iteraciones y algunos ejemplos practicos. Estare abierto a cualquierda duda y discusion respecto al tema. En general los comentarios de advertencia tu decides si tomarlos o no. No es necesario que acates todos los cambios de advertencia.
# 
# Encontraras mis comentarios en el siguiente formato - *Por favor no mueves, modifiques o elimines los comentarios*.
# 
# Podras encontrar mis comentarios en verde, amarillo o rojo como estos:
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Excelente. Todo esta perfecto.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Comentarios. Algunas recomendaciones.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Necesita ser arreglado. El bloque requiere algunas correciones. El trabajo no podra ser acceptado si tiene comentarios en rojo.
# </div>
# 
# Puedes responderme utilizando este tipo de comentario:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta estudiante.</b> <a class="tocSkip"></a>
# </div>

# # ¡Llena ese carrito!

# # Introducción
# 
# Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash.
# El conjunto de datos que te hemos proporcionado tiene modificaciones del original. Redujimos el tamaño del conjunto para que tus cálculos se hicieran más rápido e introdujimos valores ausentes y duplicados. Tuvimos cuidado de conservar las distribuciones de los datos originales cuando hicimos los cambios.
# 
# Debes completar tres pasos. Para cada uno de ellos, escribe una breve introducción que refleje con claridad cómo pretendes resolver cada paso, y escribe párrafos explicatorios que justifiquen tus decisiones al tiempo que avanzas en tu solución.  También escribe una conclusión que resuma tus hallazgos y elecciones.
# 

# ## Diccionario de datos
# 
# Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.
# 
# - `instacart_orders.csv`: cada fila corresponde a un pedido en la aplicación Instacart.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'user_id'`: número de ID que identifica de manera única la cuenta de cada cliente.
#     - `'order_number'`: el número de veces que este cliente ha hecho un pedido.
#     - `'order_dow'`: día de la semana en que se hizo el pedido (0 si es domingo).
#     - `'order_hour_of_day'`: hora del día en que se hizo el pedido.
#     - `'days_since_prior_order'`: número de días transcurridos desde que este cliente hizo su pedido anterior.
# - `products.csv`: cada fila corresponde a un producto único que pueden comprar los clientes.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'product_name'`: nombre del producto.
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
# - `order_products.csv`: cada fila corresponde a un artículo pedido en un pedido.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'add_to_cart_order'`: el orden secuencial en el que se añadió cada artículo en el carrito.
#     - `'reordered'`: 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.
# - `aisles.csv`
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'aisle'`: nombre del pasillo.
# - `departments.csv`
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
#     - `'department'`: nombre del departamento.

# # Paso 1. Descripción de los datos
# 
# Lee los archivos de datos (`/datasets/instacart_orders.csv`, `/datasets/products.csv`, `/datasets/aisles.csv`, `/datasets/departments.csv` y `/datasets/order_products.csv`) con `pd.read_csv()` usando los parámetros adecuados para leer los datos correctamente. Verifica la información para cada DataFrame creado.
# 

# ## Plan de solución
# 
# Escribe aquí tu plan de solución para el Paso 1. Descripción de los datos.

# In[261]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[262]:


orders = pd.read_csv('/datasets/instacart_orders.csv', sep=";")# leer conjuntos de datos en los DataFrames
products = pd.read_csv('/datasets/products.csv', sep=";")
aisles = pd.read_csv('/datasets/aisles.csv', sep=";")
departments = pd.read_csv('/datasets/departments.csv', sep=";")
order_product = pd.read_csv('/datasets/order_products.csv', sep=";")


# In[263]:


print(orders.info())# mostrar información del DataFrame


# In[264]:


print(products.info())# mostrar información del DataFrame


# In[265]:


print(aisles.info())# mostrar información del DataFrame


# In[266]:


print(departments.info())# mostrar información del DataFrame


# In[267]:


print(order_product.info())# mostrar información del DataFrame


# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 1. Descripción de los datos.
# 
# Al inicio importamos las librerías que vamos a utilizar, posterior a esto, clasificamos cada archivo CSV de acuerdo a la información que contiene. De aqui salen 5 variables que estaremos utilizando y usando el método .info(), sabremos que tipo de datos e información contiene el archivo:
# "orders" - tiene 6 columnas separadas por ";" y los tipos de datos que se tienen son float e int;
# "products"- tiene 4 columnas separadas por ";" y los tipos de datos que se tienen son float y object;
# "aisles"- tiene 2 columnas separadas por ";" y dos tipos de datos int y object;
# "departments" - tiene 2 columnas separadas por ";" y dos tipos de datos int y object;
# "order_product - tiene 4 columnas separadas por ";" y dos tipos de datos int y float"
# 
# Con esta información y sabiendo que los datos apesar de mostrar que son numeros o caracteres, pueden llegar a ser datos categoricos y para eso tendremos que preprocesarlos para adecuarlos al tipo de dato que necesitamos.

# # Paso 2. Preprocesamiento de los datos
# 
# Preprocesa los datos de la siguiente manera:
# 
# - Verifica y corrige los tipos de datos (por ejemplo, asegúrate de que las columnas de ID sean números enteros).
# - Identifica y completa los valores ausentes.
# - Identifica y elimina los valores duplicados.
# 
# Asegúrate de explicar qué tipos de valores ausentes y duplicados encontraste, cómo los completaste o eliminaste y por qué usaste esos métodos. ¿Por qué crees que estos valores ausentes y duplicados pueden haber estado presentes en el conjunto de datos?

# ## Plan de solución
# 
# Escribe aquí tu plan para el Paso 2. Preprocesamiento de los datos.
# 
# Cambiaria los tipos de datos, por ejemplo, en el DF de "Orders" tenemos la columna "order_id" la cual nos muestra un tipo de datos integer, no esta mal, sin embargo, es una columna a la cual el tipo de dato no se ajusta, en un futuro no sera necesario realizar alguna operación con este dato (suma,resta,etc) nos podría funcionar mas como un dato categorico.
# 
# Cambiando los tipos de datos, podemos empezar a evaluar que es lo que se tiene, buscando datos ausentes o duplicados, con la ayuda de los metodos duplicated(), fillna(), drop_duplicates() o replace().

# ## Encuentra y elimina los valores duplicados (y describe cómo tomaste tus decisiones).

# ### `orders` data frame

# In[268]:


# Revisa si hay pedidos duplicados
print(orders.head(10)) #Para conocer como estan compuestas las columnas
orders['order_id'].duplicated().sum() #user order_id porque esta columna identifica de manera unica cada pedido, por lo que si hay algun duplicado, debería de mostrarse


# ¿Tienes líneas duplicadas? Si sí, ¿qué tienen en común?

# In[269]:


# Basándote en tus hallazgos, se tienen 15 valores duplicados
# Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.
print(orders[(orders['order_dow'] == 3) & (orders['order_hour_of_day'] == 2)])


# ¿Qué sugiere este resultado? 
# Se tienen 121 filas y 6 columnas donde nos muestran las ordenes que se hicieron el día miercoles a las 2:00 am

# In[270]:


# Elimina los pedidos duplicados
orders = orders.drop_duplicates().reset_index(drop=True)


# In[271]:


# Vuelve a verificar si hay filas duplicadas
orders.duplicated().sum()


# In[272]:


# Vuelve a verificar únicamente si hay IDs duplicados de pedidos
orders['order_id'].duplicated().sum()


# Con el método duplicated() descubrimos que teniamos 15 filas con valores duplicados, por lo que se utilizo el método drop_duplicates junto con reset_index(drop=True) para eliminar los valores duplicados y reiniciar el index de las filas.

# ### `products` data frame

# In[273]:


print(products.head())


# In[274]:


# Verifica si hay filas totalmente duplicadas
products.duplicated().sum()


# In[275]:


# Verifica únicamente si hay IDs duplicadas de productos
products['product_id'].duplicated().sum()


# In[276]:


# Revisa únicamente si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)
products['product_name'].str.upper().duplicated().sum()


# In[277]:


# Revisa si hay nombres duplicados de productos no faltantes
products['product_name'].str.upper().isna().sum()


# Se verifico que no existiran duplicados dentro de las columnas pero se descubrio que se tienen valores ausentes en la columna product_name 

# ### `departments` data frame

# In[278]:


print(departments.head(5))


# In[279]:


# Revisa si hay filas totalmente duplicadas
departments.duplicated().sum()


# In[280]:


# Revisa únicamente si hay IDs duplicadas de productos
departments['department_id'].duplicated().sum()


# In[281]:


departments.isnull().sum()


# No se encontraron valores duplicados ni ausentes, por lo que podemos trabajar con estos datos

# ### `aisles` data frame

# In[282]:


print(aisles.head(5))


# In[283]:


# Revisa si hay filas totalmente duplicadas
aisles.duplicated().sum()


# In[284]:


# Revisa únicamente si hay IDs duplicadas de productos
aisles['aisle_id'].duplicated().sum()


# In[285]:


aisles.isnull().sum()


# No se encontraron valores duplicados ni ausentes, por lo que podemos trabajar con estos datos

# ### `order_products` data frame

# In[286]:


print(order_product.head(10))


# In[287]:


# Revisa si hay filas totalmente duplicadas
order_product.duplicated().sum()


# In[288]:


# Vuelve a verificar si hay cualquier otro duplicado engañoso
order_product['order_id'].value_counts()


# dentro de la columna "order_id" se encuentran duplicados

# ## Encuentra y elimina los valores ausentes
# 
# Al trabajar con valores duplicados, pudimos observar que también nos falta investigar valores ausentes:
# 
# * La columna `'product_name'` de la tabla products.
# * La columna `'days_since_prior_order'` de la tabla orders.
# * La columna `'add_to_cart_order'` de la tabla order_productos.

# ### `products` data frame

# In[289]:


print(products.head(5))


# In[290]:


# Encuentra los valores ausentes en la columna 'product_name'
products['product_name'].isnull().sum()


# Dentro de la columna "product name" se tienen 1258 valores ausentes

# In[291]:


#  ¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?
print(products.query('product_name != " " and aisle_id == 100'))


# Con estos hallazgos podemos afirmar que la columna "product_name" y sus valores ausentes estan relacionados con el pasillo ID 100, ya que son 1258 filas con valores ausentes y que anteriormente nos dio la misma cantidad sin necesidad de filtrarlo por el ID del pasillo.

# In[292]:


# ¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?
print(products.query('product_name != " " and department_id == 21'))


# Con estos hallazgos podemos afirmar que la columna "product_name" y sus valores ausentes estan relacionados con el departamento ID 21, ya que son 1258 filas con valores ausentes y que anteriormente nos dio la misma cantidad sin necesidad de filtrarlo por el ID del pasillo y departamento.
# 
# Se podria decir que el department con ID 21 y el pasillo con ID 100, estan relacionados con los valores ausentes de la columna "product_name"

# In[293]:


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.
print(products.query('aisle_id == 100 and department_id == 21'))


# Con esta información, podemos afirmar que en el pasillo con ID 100 y en el departamento con ID 21, se encuentran los valores ausentes de la columna "product_name"

# In[294]:


# Completa los nombres de productos ausentes con 'Unknown'
products = products.fillna('Unknown')
print(products.query('aisle_id == 100 and department_id == 21'))


# Se utiliza el metodo fillna() para cambiar los valores ausentes en product_name por "Unknown" y asi, eliminar estos valores ausentes.

# ### `orders` data frame

# In[295]:


print(orders.head(5))


# In[296]:


# Encuentra los valores ausentes
orders.isnull().sum()


# In[297]:


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?
orders['days_since_prior_order'].isna().sum()


# No se tienen valores ausentes, sin embargo, el metodo isna() nos muestra valores ausentes dentro de la columna days_since_prior_order, esto debido a que dentro de esta columna se encuentran tipos de datos float que nos dice cuantos dias han pasado desde que el cliente realizo su pedido. Podemos suponer que los valores ausentes de esta columna quieren decir que no han pasado dias desde el ultimo pedido.

# ### `order_products` data frame

# In[298]:


print(order_product) #nota para el revisor: me gusta visualizar las columnas para darme una idea de lo que contiene el DF antes de empezar a hacer el análisis


# In[299]:


# Encuentra los valores ausentes
order_product.isna().sum()


# In[300]:


# ¿Cuáles son los valores mínimos y máximos en esta columna?
print(order_product['add_to_cart_order'].min())
print(order_product['add_to_cart_order'].max())


# Se observa que dentro de la columna "add_to_cart_order" se tienen valores ausentes, esto puede ser debido a que no se tiene el orden secuencial en el que se añadió cada artículo en el carrito, pero de igual forma, analizando esta columna con el valor minimo y maximo, observamos que el orden va del 1, siendo este el minimo al 64, siendo este el maximo.

# In[301]:


# Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'
nan_pedidos = order_product[(order_product['add_to_cart_order'].isna())]
print(nan_pedidos)


# In[302]:


# ¿Todos los pedidos con valores ausentes tienen más de 64 productos?
# Agrupa todos los pedidos con datos ausentes por su ID de pedido.
# Cuenta el número de 'product_id' en cada pedido y revisa el valor mínimo del conteo.
nan_pedidos = order_product.groupby('order_id')
print(nan_pedidos)
print()
count_pedido = order_product['product_id'].value_counts().min()
print(count_pedido)


# El valor minimo que se tiene es 1 dentro de la columna "product_id"

# In[303]:


# Remplaza los valores ausentes en la columna 'add_to_cart? con 999 y convierte la columna al tipo entero.
order_product['add_to_cart_order']=order_product['add_to_cart_order'].fillna(999).astype('int')
print(order_product)


# In[304]:


print(order_product.isna().sum()) #para verificar que ya no se tengan valores ausentes 


# In[305]:


print(order_product.info()) #para verificar que se haya cambiado el tipo de dato


# Dentro del dataset de "order_products" podemos encontrar en la columna "add_to_cart_order" valores ausentes. Para trabajar con este dataset, se debera reemplazar los valores ausentes, en este caso por 999 y cambiar el tipo de dato de float a integer, esto porque esta columna se trabajara como un tipo de dato categorico

# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 2. Preprocesamiento de los datos
# 
# El preprocesamiento de datos nos ayuda a poder trabajar con datos mas limpios, es decir, trabajamos los datos que estan duplicados y ausentes. Para los datos que tuvimos duplicados, primeramente se localizaron, lo cual implica hacer uso del metodo  duplicated(), sabiendo donde se encuentran nuestros datos podemos optar como eliminarlos con drop_duplicated() seguido de reset_index() para que no afecte el indice de las columnas o reemplazar los valores duplicados. Se utilizo la segunda opcion, reemplazar los valores duplicados por la palabra "Unknown". 
# Para los valores ausentes, se trabajo casi de la misma manera. Se localizaron los valores ausentes que se tenian en las columnas, despues se realizo un llenado con el metodo fillna(), cambiando los valores por 999 que aparecian como NaN y posterior a esto, para trabajar la columna como un tipo de dato categorico, se cambio el tipo de dato de float a integer. 

# <div class="alert alert-block alert-success">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Veo todo ok procesaste correctamente los datos y miraste correctamente los valores ausentes
# </div>

# # Paso 3. Análisis de los datos
# 
# Una vez los datos estén procesados y listos, haz el siguiente análisis:

# # [A] Fácil (deben completarse todos para aprobar)
# 
# 1. Verifica que los valores en las columnas `'order_hour_of_day'` y `'order_dow'` en la tabla orders sean razonables (es decir, `'order_hour_of_day'` oscile entre 0 y 23 y `'order_dow'` oscile entre 0 y 6).
# 2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
# 3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
# 4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, y comenta sobre los valores mínimos y máximos.

# ### [A1] Verifica que los valores sean sensibles

# In[306]:


print(orders['order_hour_of_day'].min())
print(orders['order_hour_of_day'].max())


# In[307]:


print(orders['order_dow'].min())
print(orders['order_dow'].max())


# Las columnas 'order_dow' y 'order_hour_of_day' oscilan dentro de los rangos establecidos.
# Se usaron los metodos min() y max() para verificar que no pasaran de sus rangos.

# ### [A2] Para cada hora del día, ¿cuántas personas hacen órdenes?

# In[308]:


print(orders.head(5))


# In[309]:


print(orders.info())


# In[310]:


print(orders['order_hour_of_day'].value_counts().sort_values())
orders_day=orders['order_hour_of_day'].value_counts().sort_values()
orders_day.plot(x='order_hour_of_day', kind='bar')
plt.show()


# In[311]:


print(orders['order_hour_of_day'].value_counts().describe())


# <div class="alert alert-block alert-danger">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Te falta generar la grafica **HECHO**
# </div>

# Se observa que durante la hora 4:00 am es donde hay menos solicitudes de pedidos, sin embargo, las 10 am es cuando mas pedidos se estan solicitando. El método describe() nos ayudara a darnos una idea general de como esta compuesta nuetra información, por ejemplo, podemos ver que la media de pedidos que se realizan durante 24 horas es de 19,956. 

# ### [A3] ¿Qué día de la semana compran víveres las personas?

# In[312]:


print(orders['order_dow'].value_counts().sort_values())
orders_week=orders['order_dow'].value_counts().sort_values()
orders_week.plot(x='order_dow', kind='bar')
plt.show()


# In[313]:


print(orders['order_dow'].value_counts().describe())


# Las personas suelen comprar mas víveres el día domingo. Esto puede deverse a que el domingo es día de descanso, y aprovechan el día para realizar actividades del hogar como limpiar pero tambien para ir al super y comprar su despensa para la semana. 
# 
# La media esta en 6,8421 personas, viendo nuestro datos, la media se encuentra aproximadamente en el dia 2 (Martes), mi hipotesis en este caso es que tal vez los días martes suele haber ciertos beneficios en los supermercados como los martes de frescura. 

# <div class="alert alert-block alert-danger">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Te falta generar la grafica **HECHO**
# </div>

# ### [A4] ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.

# In[314]:


#Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, y comenta sobre los valores mínimos y máximos.
print(orders['days_since_prior_order'].describe())


# In[315]:


print(orders['days_since_prior_order'].value_counts().sort_values())
orders_wait=orders['days_since_prior_order'].value_counts().sort_values()
orders_wait.plot(x='days_since_prior_order', kind='bar')
plt.show()


# Por los valores minimos y maximos, va desde el 0 dias hasta 30, sin embargo, con la media podemos darnos una idea de que tardan aprox 11 dias en realizar nuevamente un pedido.

# <div class="alert alert-block alert-danger">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Te falta generar la grafica **HECHO**
# </div>

# # [B] Intermedio (deben completarse todos para aprobar)
# 
# 1. ¿Existe alguna diferencia entre las distribuciones `'order_hour_of_day'` de los miércoles y los sábados? Traza gráficos de barra de `'order_hour_of_day'` para ambos días en la misma figura y describe las diferencias que observes.
# 2. Grafica la distribución para el número de órdenes que hacen los clientes (es decir, cuántos clientes hicieron solo 1 pedido, cuántos hicieron 2, cuántos 3, y así sucesivamente...).
# 3. ¿Cuáles son los 20 principales productos que se piden con más frecuencia (muestra su identificación y nombre)?

# ### [B1] Diferencia entre miércoles y sábados para  `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# In[316]:


orders[orders['order_dow']==3]['order_hour_of_day'].plot(kind='hist')

plt.show() 


# In[317]:


orders[orders['order_dow']==6]['order_hour_of_day'].plot(kind='hist')
plt.show() 


# In[318]:


orders[orders['order_dow']==3]['order_hour_of_day'].plot(kind='hist', bins=20)
orders[orders['order_dow']==6]['order_hour_of_day'].plot(kind='hist',bins=20, alpha=0.7)
plt.legend(['Miercoles', 'Sabados'])
plt.show() 


# Realmente no existe mucha variación en cuanto a las ordenes hechas el miercoles y sabado en un horario especifico, podemos observar que los dos dias tienen un crecimiento gradual similar en un horario de 7 am - 9 am hasta el repunte que se tiene durante las 3 de la tarde y de ahi va decayendo

# ### [B2] ¿Cuál es la distribución para el número de pedidos por cliente?

# In[319]:


orders['order_number'].plot(kind='hist', bins=10)

plt.show() 


# In[320]:


print(orders.head())


# Se observa que la tendencia es 1-10 pedidos por cliente y disminuye gradualmente.

# ### [B3] ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?

# In[321]:


products_merge = order_product.merge(products, on='product_id')
print(products_merge)


# In[322]:


products_20=products_merge.groupby('product_name')['product_id'].sum()
print(products_20)


# In[323]:


print(products_20.sort_values(ascending=False).head(20))


# Tuvimos que hacer uso del método merge() para poder unir dos datasets, order_product y products, esto para obtener los nombres de los productos junto con su id gracias a la llave primaria "product id". El dataset order_product nos da la información necesaria para saber cuantas veces se pidio un producto y el dataset products nos dara el nombre de ese producto al estar relacionado 1:1 con "product_id". Con lo anterior, agrupando y ordenando los valores de mayor a menos, podemos encontrar los 20 productos mas pedidos, y encontramos que el mas pedido es el producto "Banana"

# <div class="alert alert-block alert-success">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Perfecto, veo todo ok ! 
# </div>

# # [C] Difícil (deben completarse todos para aprobar)
# 
# 1. ¿Cuántos artículos suelen comprar las personas en un pedido? ¿Cómo es la distribución?
# 2. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?
# 3. Para cada producto, ¿cuál es la tasa de repetición del pedido (número de repeticiones de pedido/total de pedidos?
# 4. Para cada cliente, ¿qué proporción de los productos que pidió ya los había pedido? Calcula la tasa de repetición de pedido para cada usuario en lugar de para cada producto.
# 5. ¿Cuáles son los 20 principales artículos que la gente pone primero en sus carritos (muestra las IDs de los productos, sus nombres, y el número de veces en que fueron el primer artículo en añadirse al carrito)?

# ### [C1] ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?

# In[362]:


pedidos_merge = order_product.merge(orders, on='order_id')
print(pedidos_merge)


# In[363]:


pedidos_merge=pedidos_merge.groupby('order_id').count()
print(pedidos_merge)


# In[364]:


pedidos_merge=pedidos_merge['product_id'].value_counts().sort_values()
pedidos_merge.plot(x='product_id', kind='hist')
plt.show()


# In[326]:


pedidos_merge['product_id'].describe()


# In[327]:


#¿cual grafica? en las instrucciones no pide graficar


# <div class="alert alert-block alert-danger">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Te falta generar la grafica ! **HECHO** Tienes razon, estaba teniendo como base una solucion que muestra la solucion en grafica
# </div>

# Se uso el método merge() para juntar dos datasets, order_product y orders, esto para unir mediante la llave primaria "order_id" a los datasets y poder encontrar cuantos articulos suelen pedir en un pedido. Despues, mediante el metodo describe() podemos ver los datos estadisticos, donde la media de articulos que se piden es de 10, el minimo de pedidos es 1 y el maximo es 127.

# ### [C2] ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

# In[328]:


articulos_20 = order_product.merge(products, on='product_id')
print(articulos_20)


# In[329]:


articulos_20=articulos_20.groupby('product_name')['reordered'].count()


# In[330]:


print(articulos_20.sort_values(ascending=False).head(20))


# Banana es el producto mas vendido y el que mas se vuelve a pedir. 

# ### [C3] Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?

# In[331]:


product_pedido=order_product.groupby('product_id').count()
print(product_pedido)


# In[332]:


print(product_pedido['reordered'].mean())


# In[333]:


product_pedido=product_pedido.sort_values('reordered',ascending=False)
print(product_pedido)


# In[334]:


print(product_pedido['reordered'].describe())


# <div class="alert alert-block alert-danger">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Debes sacar el numero de proporcion de que se re-ordene un producto y es numero entre 0 y 1 ! Puede agrupar por producto y luego sacar el promedio de la variable reordered. Igual no borres ya lo que hiciste que tambien es de muy buena informacion y esta altamente relacionado ! **HECHO**
# </div>

# La proporcion o la media de cada producto es de casi 59, esto quiere decir, que cada producto vuelve a pedirse al menos 100 veces.

# ### [C4] Para cada cliente, ¿qué proporción de sus productos ya los había pedido?

# In[335]:


cliente_pedido = order_product.merge(orders, on='order_id')
print(cliente_pedido)


# In[336]:


print(cliente_pedido['reordered'].mean())


# In[337]:


cliente_pedido=cliente_pedido.groupby('user_id')['reordered'].count()
print(cliente_pedido)


# In[338]:


cliente_pedido.describe()


# Cada cliente tiene una media de 30 pedidos que ya ha comprado con anterioridad.

# <div class="alert alert-block alert-danger">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Debes sacar el numero de proporcion de que se re-ordene un producto por usuario y es numero entre 0 y 1 ! Puede agrupar por usuario y luego sacar el promedio de la variable reordered. Igual no borres ya lo que hiciste que tambien es de muy buena informacion y esta altamente relacionado ! **HECHO**
# </div>

# ### [C5] ¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?

# In[339]:


primer_producto = order_product.merge(products, on='product_id')
print(primer_producto)


# In[340]:


primer_producto = primer_producto.query('add_to_cart_order == 1')[['product_id','product_name','add_to_cart_order']]
print(primer_producto)


# In[341]:


primer_producto = primer_producto.groupby('product_name').count()
print(primer_producto)


# In[365]:


print(primer_producto.head(20))


# Radiant Super Tampons es el articulo top de los productos que se piden y se vuelven a pedir por un cliente, asi como, es el producto que ponen primero en sus carritos.

# <div class="alert alert-block alert-danger">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Debes seleccionar aquellos que la orden es 1 en el orden y luego hacer el conteo por producto y seleccionar el top 20 **HECHO**
# </div>

# ### Conclusion general del proyecto:

# Se revisaron los datasets, donde se encontraron duplicados y valores ausentes. Trabajando con los metodos correspondientes pudimos hacer una limpieza de estos datos y poder tener datasets preprocesados. Una vez los datos esten limpios, podemos empezar a hacer un analisis de la información, para esto se utilizaran las ayudas visuales, podemos ver que los dias miercoles y sabado no varian tanto entre ellos para las ordenes que hacen los clientes. 
# Despues de graficar la informacion solicitada, hacer podemos seguir analizando los datos, respondiendo preguntas de negocio para poder llegar a un objetivo.
# Encontramos que el producto Banana es de los mas comprados, recomprados y que es el producto que primeramente se pone en el carrito.
# Los clientes tienden a comprar al menos 10 productos cada que visitan hacen un pedido, donde banana es el producto estrella de la tienda.
# Despues de todo, podemos seguir analizando la informacion, por ejemplo, conocer departamento es el que mas vende, cuales clientes son los que menos pedidos han hecho o que producto es el que mas se vende un dia jueves. 
# 
# En general, el proyecto estuvo complejo, ya que la informacion que se vio en el sprint 3 fue demasiada pero apesar de eso, muy educativo poder realizar este tipo de proyectos.
# Realmente me hubiera gustado usar mas las graficas que encontrar una tendencia de los productos, y tambien poder haber utilizado los datasets aisles o departments.
# 

# <div class="alert alert-block alert-success">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Todo ok atendiste las correciones y ya se ve mas ameno el resultaod. Buenas conclusiones finales tambien, resume los insight encontrados
# </div>

# In[ ]:




