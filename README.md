# Smart Inventory Manager

## Descripción del Proyecto

**Smart Inventory Manager** es un sistema inteligente de gestión de inventarios basado en tecnologías IoT y computación en la nube. Su objetivo es optimizar la administración de inventarios mediante la automatización del escaneo de productos y el uso de modelos predictivos de Machine Learning para prever la demanda futura.

El sistema permite el escaneo de productos mediante RFID (simulado con Python), el almacenamiento seguro de datos en la nube (AWS S3) y la predicción de la demanda a partir de un modelo de regresión lineal. Además, incorpora medidas de seguridad como autenticación JWT y cifrado de datos para garantizar la integridad de la información.

### Funcionalidades Principales

- **Escaneo de productos mediante RFID**: Simulado con Python para la captura automática de datos de inventario.
- **Almacenamiento en la nube (AWS S3)**: Garantiza alta disponibilidad, seguridad y fácil acceso a los datos.
- **Modelo de Machine Learning**: Implementa una regresión lineal para predecir la demanda futura de productos.
- **Autenticación JWT**: Asegura el acceso a los datos mediante un sistema de autenticación basado en tokens.
- **Seguridad y cifrado**: Los datos se almacenan con cifrado AES256 en la nube.
- **Interoperabilidad IT/OT**: Facilita la integración entre sistemas de TI y dispositivos operativos.

---

# Ciclo de vida del dato (5b)

## ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?

En el proyecto **Smart Inventory Manager**, el ciclo de vida de los datos sigue las siguientes etapas:

1. **Generación**: Los datos son generados a través del escaneo de productos mediante RFID simulado en Python. Cada producto escaneado genera un ID único que es procesado por el sistema.

2. **Almacenamiento**: Los datos del escaneo son almacenados en **AWS S3**, utilizando cifrado AES256 para garantizar su seguridad.

3. **Procesamiento**: Los datos almacenados pueden ser utilizados por el modelo de **Machine Learning** basado en regresión lineal para predecir la demanda futura de productos.

4. **Uso**: El modelo predictivo ayuda a la toma de decisiones en la gestión de inventarios, optimizando el stock disponible.

5. **Eliminación**: Actualmente, el sistema no implementa una política de retención o eliminación de datos, pero podría integrarse mediante reglas de retención en S3 o configuración de tiempos de vida de objetos en la nube.

---

## ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?

Para garantizar la consistencia e integridad de los datos, se han tomado las siguientes medidas:

- **Validación de datos**: Antes de almacenar cualquier información en AWS S3, el sistema valida que los **IDs de los productos** escaneados sean alfanuméricos.
- **Cifrado**: Los datos almacenados en la nube utilizan cifrado AES256 para protegerlos contra accesos no autorizados.
- **Modelo de predicción evaluado**: La regresión lineal utilizada para predecir la demanda incluye una evaluación con **error cuadrático medio (MSE)** para verificar la precisión del modelo.
- **Autenticación JWT**: Se emplea autenticación segura con **JSON Web Tokens (JWT)** para evitar accesos indebidos a los datos.

---

## Si no trabajas con datos, ¿Cómo podrías incluir una funcionalidad que los gestione de forma eficiente?

Si no se trabajara actualmente con datos, se podría incluir una base de datos **SQL (PostgreSQL)** o **NoSQL (MongoDB)** para almacenar los registros de productos y sus predicciones de demanda. Esto permitiría un acceso estructurado y eficiente a los datos, además de facilitar consultas avanzadas para la toma de decisiones.

---

# Almacenamiento en la nube (5f)

## Si tu software utiliza almacenamiento en la nube, ¿Cómo garantizas la seguridad y disponibilidad de los datos?

El sistema usa **AWS S3** para almacenar los datos de los productos escaneados y las predicciones de demanda. Para garantizar seguridad y disponibilidad se han implementado:

- **Cifrado AES256** en los objetos almacenados en S3.
- **Control de acceso** mediante AWS IAM para definir permisos y restringir accesos no autorizados.
- **Autenticación JWT** para el acceso seguro a los datos.
- **Alta disponibilidad** de S3, con replicación en múltiples zonas de disponibilidad de AWS.
- **Reglas de versión y backup** para evitar pérdida de datos por errores humanos.

---

## ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?

Se consideraron varias opciones para almacenar datos:

1. **Bases de datos locales**: Dificultades para escalar y falta de disponibilidad remota.
2. **Google Cloud Storage o Azure Blob Storage**: Son opciones viables, pero AWS S3 se eligió por **integración sencilla con otros servicios AWS** y su facilidad de uso.

La elección de AWS S3 permitió una gestión segura, escalable y accesible desde cualquier ubicación.

---

## Si no usas la nube, ¿Cómo podrías integrarla en futuras versiones?

Si no se usara la nube, se podría integrar mediante:

- **AWS DynamoDB** para gestionar los productos de manera estructurada.
- **AWS Lambda** para procesar eventos de escaneo en tiempo real.
- **Azure o Google Cloud** como alternativas de almacenamiento y procesamiento en la nube.

---

# Seguridad y regulación (5i)

## ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?

- **Autenticación JWT** para garantizar accesos seguros.
- **Cifrado de datos (AES256) en AWS S3**.
- **Validación de entradas** para evitar inyecciones de datos no válidos.
- **Manejo de excepciones** para evitar caídas del sistema.

---

## ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?

- **GDPR (Reglamento General de Protección de Datos)**: Si el sistema maneja datos personales, debe incluir opciones de eliminación y portabilidad de datos.
- **ISO 27001**: Se podría implementar para mejorar la gestión de seguridad de la información.

---

## Si no implementaste medidas de seguridad, ¿Qué riesgos potenciales identificas y cómo los abordarías en el futuro?

- **Fuga de datos**: Implementar autenticación multifactor.
- **Pérdida de información**: Configurar backups automáticos.
- **Ataques de inyección de datos**: Mejorar validaciones y sanitización de entradas.

---

# Tecnologías Habilitadoras Digitales (2g)

## ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

- **IoT** (sensores RFID).
- **Machine Learning** (predicción de demanda).
- **Cloud Computing** (AWS S3 para almacenamiento seguro).

Estas tecnologías permiten una mejor **automatización, predicción y seguridad** en la gestión del inventario.
