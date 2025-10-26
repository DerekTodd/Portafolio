Laboratorio 5.1: Trabajar con DynamoDB

En este laboratorio se implementó y gestionó una tabla **Amazon DynamoDB** mediante la **Consola de Administración de AWS**, el entorno de desarrollo **AWS Cloud9 (Visual IDE)** y el uso del **SDK para Python (boto3)**.\
El objetivo principal fue aprender a crear una tabla, insertar y modificar registros, realizar consultas, y agregar un **índice secundario global (GSI)** para mejorar las capacidades de búsqueda.

🔹 Tarea 1: Preparación del Laboratorio

Conexión al Visual IDE

1. Desde el menú **Servicios**, se buscó y seleccionó **Visual IDE (Cloud9)**.
1. Se abrió el entorno de desarrollo asociado al laboratorio.
### **Descarga y extracción de archivos requeridos**
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-200-ACCDEV-2-91558/03-lab-dynamo/code.zip -P /home/ec2-user/environment

unzip code.zip
### **Actualización de versiones de Python y AWS CLI**
chmod +x ./resources/setup.sh && ./resources/setup.sh

Esto permitió configurar las dependencias necesarias para la ejecución de scripts Python que interactúan con DynamoDB.

![](Aspose.Words.fe706cae-583d-4d98-9eb3-a280f72ff643.001.png)

🔹 Tarea 2: Creación de una Tabla DynamoDB Usando el SDK para Python
### Creación de la tabla
1. Se abrió la consola de **DynamoDB** desde **Servicios > DynamoDB**.
1. En el panel de navegación, se seleccionó **Tablas**.
1. En el entorno **Cloud9**, se editó el script create\_table.py reemplazando <FMI\_1> por el nombre de la tabla:

\# Nombre de la tabla

table\_name = "FoodProducts"

4. Se ejecutó el script:

cd python\_3

python3 create\_table.py

![](Aspose.Words.fe706cae-583d-4d98-9eb3-a280f72ff643.002.png)
## 🔹 Tarea 3: Trabajo con Datos de DynamoDB – Expresiones de Condición
### Inserción de un nuevo registro
Archivo JSON utilizado: resources/not\_an\_existing\_product.json

Comando ejecutado:

aws dynamodb put-item \

--table-name FoodProducts \

--item file://../resources/not\_an\_existing\_product.json \

--region us-east-1
### Verificación del registro
1. En la **Consola de DynamoDB**, se abrió el **Explorador de ítems**.
1. Se seleccionó la tabla **FoodProducts** y se ejecutó un **Escaneo** para visualizar los datos.

![](Aspose.Words.fe706cae-583d-4d98-9eb3-a280f72ff643.003.png)

## 🔹 Tarea 4: Agregar y Modificar un Ítem Individual Usando el SDK
1. Se editó el archivo conditional\_put.py ubicado en python\_3/.
1. Se reemplazaron los marcadores <FMI> por los valores correspondientes (nombre de la tabla y atributos).
1. Se guardó el archivo y se ejecutó el script para insertar o modificar un ítem condicionado por la existencia de una clave primaria.

![](Aspose.Words.fe706cae-583d-4d98-9eb3-a280f72ff643.004.png)
## 🔹 Tarea 5: Agregar Múltiples Ítems Usando el SDK y Procesamiento por Lotes
### Limpieza de la tabla
1. En el **Explorador de ítems**, se eliminaron todos los registros existentes mediante **Acciones > Eliminar ítem(s)**.
1. Se escribió Delete para confirmar.
### Actualización del script de carga por lotes
1. En test\_batch\_put.py, se reemplazaron los marcadores:
   1. <FMI\_1> → FoodProducts
   1. <FMI\_2> → product\_name
1. Se guardó y ejecutó el script:

python3 test\_batch\_put.py
### Ejecución del script principal
1. En batch\_put.py, se reemplazó <FMI> con FoodProducts.
1. Se ejecutó el script para insertar varios ítems simultáneamente:

python3 batch\_put.py

![](Aspose.Words.fe706cae-583d-4d98-9eb3-a280f72ff643.005.png)





**🔹 Tarea 6: Consultar la Tabla Usando el SDK**
### Obtener todos los ítems
1. Se editó el archivo get\_all\_items.py, reemplazando <FMI\_1> con FoodProducts.
1. Se ejecutó:

python3 get\_all\_items.py
### Obtener un ítem específico
1. En get\_one\_item.py, se reemplazó <FMI\_1> con el nombre de la **clave primaria** (product\_name).
1. Se ejecutó:

python3 get\_one\_item.py

![](Aspose.Words.fe706cae-583d-4d98-9eb3-a280f72ff643.006.png)



















**🔹 Tarea 7: Agregar un Índice Secundario Global (GSI)**
### Creación del índice
1. En el archivo add\_gsi.py, se reemplazó <FMI\_1> con el tipo de clave HASH.
1. Se ejecutó:

python3 add\_gsi.py
### Monitoreo del estado del índice
1. En la **Consola de DynamoDB**, se verificó que el índice apareciera en la pestaña **Índices** de la tabla **FoodProducts**.
1. Se esperó hasta que el estado cambiara de *Creating* a *Active*.
### Consulta con filtro sobre el GSI
1. En scan\_with\_filter.py, se reemplazaron:
   1. <FMI\_1> → special\_GSI
   1. <FMI\_2> → tags
1. Se ejecutó:

python3 scan\_with\_filter.py

![](Aspose.Words.fe706cae-583d-4d98-9eb3-a280f72ff643.007.png)
## 🔹 Conclusión
Este laboratorio permitió aprender el ciclo completo de uso de **Amazon DynamoDB**:

- Creación de tablas mediante **boto3**.
- Inserción y actualización de datos usando **expresiones condicionales**.
- Carga masiva de registros con **Batch Write**.
- Consulta de datos con scripts Python personalizados.
- Implementación de **índices secundarios globales (GSI)** para ampliar la capacidad de consulta.

DynamoDB demostró ser una base de datos **NoSQL altamente escalable**, adecuada para aplicaciones modernas que requieren baja latencia y alta disponibilidad sin necesidad de gestión manual de infraestructura.

