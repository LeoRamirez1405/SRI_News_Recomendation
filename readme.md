# Sistema de Recomendaciones de Noticias

## Autores
- Naomi Lahera Champagne C411
- Leonardo Javier Ramírez Calatayud C411
- Loitzel Ernesto Morales Santiesteban C412

## Descripción del Problema
El proyecto tiene como objetivo proporcionar una oportunidad de práctica para desarrollar habilidades en el procesamiento de lenguaje natural (NLP). Se centra en la extracción de información estructurada de artículos de noticias en línea. Este proyecto permite explorar y aplicar técnicas de NLP para abordar desafíos específicos, como la identificación de titulares, autores, fechas de publicación, resúmenes de contenido y entidades relevantes en los artículos de noticias. Además, se plantea el desafío adicional de buscar noticias similares en una base de datos interna, lo que brinda la oportunidad de desarrollar habilidades en comparación de texto y análisis semántico. A través de este proyecto, los participantes podrán familiarizarse con diversas herramientas y técnicas de NLP, así como practicar la implementación de soluciones para problemas del mundo real en un entorno de desarrollo controlado.

## Consideraciones tomadas a la hora de desarrollar la solución

Extracción de Información de Noticias
Para garantizar la adquisición de datos relevantes, empleamos herramientas como Beautiful Soup y Newspaper3k. Beautiful Soup nos permite realizar un análisis robusto y flexible de la estructura HTML/XML de las páginas web para extraer la información deseada. Por otro lado, Newspaper3k facilitó la tarea de obtener el contenido específico de las noticias de diversos sitios web. Para suplir las carencias de Newspaper3k utilizamos expresiones regulares.

Construcción de la Matriz TF-IDF
Construimos una matriz TF-IDF para la generación de recomendaciones precisas y relevantes. A partir de una base de datos previamente recopilada, implementamos un proceso de transformación de documentos de texto en una representación numérica utilizando la técnica TF-IDF. Esto nos permitió calcular la importancia relativa de cada término en el contexto de las noticias recopiladas, lo que a su vez facilitó la identificación de temas y la generación de recomendaciones personalizadas para los usuarios.

Desarrollo del Frontend de la Aplicación
Para ofrecer una experiencia de usuario atractiva y amigable, optamos por Angular 17 para el desarrollo del frontend de la aplicación. Angular 17 rbinda un conjunto completo de herramientas y funcionalidades para la creación de interfaces de usuario modernas y dinámicas. Aprovechamos su capacidad para la creación de componentes reutilizables, su sistema de enrutamiento avanzado y su sólido soporte para la gestión de estados para construir una interfaz que facilitaría la navegación y la interacción de los usuarios con el sistema de recomendaciones.

## Ejecución del Proyecto
### Requisitos
- Python 3.x
- Bibliotecas de Python: `newspaper3k`, `Beautiful Soup`, `Sklearn`.
- Angular17 (para la interfaz visual)


### Instrucciones
Para ejecutar el proyecto, acceda a la interfaz visual proporcionada. Proporcione el enlace del artículo de noticias del cual desea extraer la información relevante. La interfaz procesará la solicitud y mostrará la información extraída de acuerdo con los requisitos del problema:

- Titulares
- Autores
- Fecha de publicación
- Resumen del contenido
- Entidades involucradas (personas, organizaciones y/o países)
- Propuesta de otras 3 noticias similares

Siga las instrucciones en la interfaz para ingresar el enlace del artículo y visualizar la información procesada.

## Explicación de la Solución Desarrollada

El desarrollo de la solución se divide en tres componentes principales, cada una diseñada para abordar un aspecto específico del problema de extracción de información de noticias en línea.

### Componente 1: Recopilación de Datos
Durante esta etapa inicial, el sistema utiliza diversas bibliotecas de Python, como `newspaper3k` y `Beautiful Soup`, para llevar a cabo el proceso de web scraping. Se proporciona un enlace al artículo de noticias del cual se desea extraer la información relevante. Luego, utilizando técnicas de web scraping, el sistema extrae el contenido del artículo de la página web correspondiente. Se utilizan expresiones regulares para identificar y extraer los elementos clave del artículo, como titulares, autores, fecha de publicación y contenido del artículo. Una vez recopilados, los datos se almacenan en una base de datos para su posterior procesamiento en las siguientes componentes del sistema.

### Componente 2: Recuperación de los datos
Para este momento tendremos precalculada una matriz de TfxIdf asociada a los documentos y un vectorizador que se encargará de llevar consigo el vocabulario asociado al corpus seleccionado junto con información importante de estas palabras la cual se utilizá para calcular el TfxIdf de la consulta, para todo lo anterior es que se utiliza la biblioteca `sklearn`. Una vez calculados TfxIdf tanto de la consulta como de las noticias almacenadas procedemos a realizar la recuperación de los documentos más similares a la misma y para ello utilizamos `cosSimilarity`, con ella seleccionamos los de mayor valor y estos serían los documentos devueltos.

### Componente 3: Desarrollo de la Interfaz Visual
En esta componente, se utiliza Angular para desarrollar una interfaz visual amigable para el usuario. Angular proporciona un entorno robusto y estructurado para crear aplicaciones web interactivas y dinámicas. Se diseñará una interfaz intuitiva que permita a los usuarios proporcionar el enlace del artículo de noticias del cual desean extraer información relevante. La interfaz mostrará de manera clara y organizada la información procesada, incluyendo titulares, autores, fecha de publicación, resumen del contenido, entidades involucradas y propuesta de noticias similares. Se prestará especial atención a la usabilidad y la experiencia del usuario para garantizar una navegación fluida y una comprensión fácil de la información presentada.

## Conocimiento Utilizado
Expresiones Regulares:
Aprendimos y utilizamos el funcionamiento de expresiones regulares para el análisis y la extracción de datos de manera precisa y eficiente. Estas herramientas nos permitieron identificar patrones específicos en el contenido de las noticias, facilitando así la extracción de información relevante de manera automatizada.

## Insuficiencias de la Solución y Mejoras Propuestas
Una de las insuficiencias de la solución actual es la limitación de las expresiones regulares utilizadas en el proceso de extracción de información. Si bien las expresiones regulares pueden ser efectivas en muchos casos, no son lo suficientemente generales para manejar todas las variaciones y formatos de los artículos de noticias en línea. Se reconoce que existen herramientas más poderosas, como los modelos de lenguaje de última generación (LLM), que podrían ofrecer una solución más robusta y precisa. Sin embargo, también se considera que estas herramientas pueden consumir una cantidad considerable de recursos computacionales. Por lo tanto, se propone explorar otras herramientas más simples y eficientes que puedan abordar el problema sin comprometer significativamente el rendimiento del sistema. La búsqueda de herramientas más adecuadas y eficientes será un área clave si se busca una mejora en futuras iteraciones.
Además, se ha observado que el autoresumen proporcionado por Newspaper3k no funciona correctamente el 100% de las veces. Esto puede afectar la calidad de las recomendaciones generadas, ya que la precisión y la relevancia del resumen son fundamentales para la comprensión del contenido de la noticia. Por lo tanto, se sugiere buscar algoritmos externos específicos para la tarea de autoresumen, que puedan mejorar la calidad y la consistencia de los resúmenes generados.