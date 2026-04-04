# Actividad 2.1: Investigación de Arquitecturas de Datos

## Descripción: Investiga las diferentes arquitecturas de almacenamiento de datos.

**Instrucciones:**
1. Investiga qué son los Data Warehouses y Data Lakes.

### Data Warehouses
Un data warehpuse es un repositorio unificado para todo los datos que recogen los diversos  sistemas de una empresa. El repositorio puede ser físico o lógico y hace hincapié en la captura de datos de diversas fuentes sobre todo para fines analiticos y de acceso, basicamente esto permite a los ejecutivos de negocios organizar, comprender y utilizar sus datos para tomar decisiones estratégicas.

### Data Lakes

Un data lake es un repositorio de almacenamiento que conntienen una gran cantidad de datos en bruto y que se mantiene allí hasta que sea necesario. A diferencia de un data warehouse jerárquico que almacena datos en ficheros o carpetas, un data lake utiliza arquitectura plana para almacenar los datos, por otra parte, cuando se presenta una cuestión de negocios que debe ser resuelta, podemos analizar ese conjunto de datos más pequeño para ayudar a obtener una respuesta.

2. Compara las características de cada uno

|Data Warehouses|Data Lake
|---------------|---------
|Almacena datos estrcucuturados y procesados|Almacena grandes volúmenes de datos crudos, osea estructurados y no estructurados|
|Es mas costoso ya que en Data Werehouse requiere que los datos sean procesados, limpios y estrcuturados antes de ser almacenados, lo que aumenta los costos de computación y mantenimiento.|Es menos costoso principalmente porque permite almacenar grandes volúmenes de datos en su estado natural, osea en bruto, sin necesidad de transformarlos, limpiarlos o estrcuturarlos previamente.|
|Este lado nos ayuda a optimizar mejor las consultas rápidas y reportes, tambien, para inteligencia de negocios.|Por otro lado, en esta parte es totalmente ideal para machine learning y analitica avanzada.

3. Investiga qué es un Data Mart

Un data mart es un sistema de almacén de datos que contiene informacion especifica de la unidad empresarial de una organizaciónz . Contiene una parte pequeña y especifica de los datos que la empresa almacena en un sistema de almacenamiento más grande,esto tambien da, datos resumidos que las partes interesadas clave pueden utilizar para tomar decisiones informadas rápidamente.Por por otro lado, con un data mart, los equipos puede acceder a los datos y obtener información más rápidamente, ya que no tienen que dedicar tiempo a bucar en un almacén de datos más complejo o consignar manualmente datos de diferentes origenes.

4. Crea un diagrama mostrando las diferencias
<img width="1536" height="1024" alt="Diagrama (Diferencia de Datas)" src="https://github.com/user-attachments/assets/a0c27c36-2c53-45f8-bd19-e4c4fd246029" />

