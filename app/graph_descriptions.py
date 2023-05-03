RELEASE_YEAR_TEXT = "La columna “release_year” muestra los directores de los shows, esta es una columna numérica cuyos valores son los años en los que se lanzaron los shows. El 0% de los datos de esta columna es nulo y tiene 90 valores únicos. En la siguiente grafica se muestra el histograma de la distribución de los años. Observamos que la mayoría de las películas en la plataforma fueron lanzadas en los últimos años (después del 2010)."

RATING_TEXT = "La columna “rating” muestra los diferentes públicos objetivos de los shows, esta es una columna categórica. El 1% de los datos de esta columna es nulo y tiene 9 valores únicos. En la siguiente grafica de torta se muestra el porcentaje de cada rating. Observamos que la mayoría de las películas tiene clasificación TV-G y TV-PG."

DURATION_TEXT = "La columna “duration” muestra la duración de los shows. Para algunos la duración esta en minutos para otros en cantidad de temporadas. El 0% de los datos de esta columna es nulo y tiene 158 valores únicos. En la siguiente dos graficas se muestra la distribución de las duraciones en segundos y por temporadas. Observamos que la mayoría de los shows duran entre 80 y 120 minutos y es curioso que también haya una gran cantidad de shows con duración entre 5 y 9 minutos."

LISTED_IN_TEXT = "La columna “listed_in” muestra las categorías en las que los shows se encuentran listados dentro de la plataforma, esta es una columna categórica cuyos valores son textos que corresponden a los nombres de las diferentes categorías separados por coma. El 0% de los datos de esta columna es nulo y tiene 329 valores únicos. En la siguientes 2 graficas se muestra el top 10 de categorías conjuntas y el top 10 de categorías individuales. Observamos que las categorías más populares son familia, animación y comedia."

DESCRIPTION_TEXT = "La columna “description” muestra un texto con la descripción de los shows, esta es una columna categórica cuyos valores son textos que corresponden a las descripciones de los títulos . El 0% de los datos de esta columna es nulo y tiene 1448 valores únicos. En la siguiente grafica se muestra un diagramad e nube de palabras creado con la descripción de todos los shows. Se observa que las palabras mas comunes dentro de las descripciones son “see”, “details” y “advisory”."

DIRECTOR_TEXT = "La columna “director” muestra los directores de los shows. Esta es una columna categórica cuyos valores son textos que corresponden a los nombres de los directores separados por coma. El 33% de los datos de esta columna es nulo y tiene 609 valores únicos. En la siguiente gráfica se muestra el top 10 de los directores que más dirigieron los shows. Observamos que Jack Hannah es la persona que dirigió la mayor cantidad de shows con 17 shows dirigidos."

TYPE_TEXT = "La columna “type” muestra tipos de show, esta es una columna categórica cuyos valores son ‘Movie’ o ‘Tv Show’. No hay valores nulos en esta columna. El siguiente diagrama de torta muestra el porcentaje de cada tipo de show. Observamos que hay una mayor cantidad de películas que de TV shows."

CAST_TEXT = "La columna “cast” muestra los actores principales de los shows, esta es una columna categórica cuyos valores son textos que corresponden a los nombres de los actores separados por coma. El 13% de los datos de esta columna es nulo y tiene 1193 valores únicos. En la siguiente gráfica se muestra el top 10 de los actores que más participaron en shows. Observamos que Jim Cummings es la persona que participó en la mayor cantidad de shows con 33 shows."

COUNTRY_TEXT = "La columna “country” muestra los países en los que se grabaron los shows, esta es una columna categórica cuyos valores son textos que contienen países separados por coma. El 15% de los datos de esta columna es nulo y hay 89 valores únicos. El siguiente gráfico representa cada uno de los países de la lista por medio de puntos. El color de los puntos varía de acuerdo con la cantidad de películas realizadas por país. Observamos que Estados Unidos es por mucho el país en el que se han grabado más películas. Una mejora posible para este gráfico podría ser utilizar una escala logarítmica para asignar el color a los puntos y que de esta manera se vea mejor la diferencia de colores."

TITLE_TEXT = "La columna “titles” muestra los títulos de los shows, esta es una columna categórica que no tiene valores nulos y en la que todos los valores son distintos. Se identificó que hay algunas películas que pertenecen a la misma saga. El siguiente gráfico representa el top 30 de la cantidad de películas que pertenecen a una misma saga. Para obtener este top se utilizó un algoritmo de búsqueda de patrones que funciona bien en ciertos casos, aunque podría ser mejorado ya que Up y Out no son sagas."

DESCRIPTION_TEXT = "La columna “description” muestra un texto con la descripción de los shows, esta es una columna categórica cuyos valores son textos que corresponden a las descripciones de los títulos. El 0% de los datos de esta columna es nulo y tiene 1448 valores únicos. En la siguiente gráfica se muestra un diagrama de nube de palabras creado con la descripción de todos los shows. Se observa que las palabras más comunes dentro de las descripciones son “see”, “details” y “advisory”."

INTRODUCTION_TEXT = "El siguiente es un análisis de los datos del archivo disney_plus_titles.csv. En la primera parte del análisis se exploraron los datos utilizando un notebook de Python. A continuación, se presentan los resultados del análisis junto con los gráficos más relevantes por cada columna. Es importante destacar que, para complementar este análisis, sería necesario explorar las diferentes relaciones entre las variables."