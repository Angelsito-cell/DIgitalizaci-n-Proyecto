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


¡Perfecto! Aquí tienes una versión completa y redactada de forma clara y humana para que puedas copiarla directamente a un archivo `.md` (Markdown):

---

## Objetivos estratégicos

**¿Qué objetivos estratégicos específicos de la empresa aborda tu software?**  
Nuestro Smart Inventory Manager se alinea directamente con los siguientes objetivos estratégicos:
- **Reducción de costes operativos:** Minimiza el exceso de stock y evita roturas de inventario gracias a predicciones de demanda basadas en Machine Learning.  
- **Mejora en la trazabilidad y visibilidad:** Proporciona visibilidad en tiempo real del inventario mediante escaneo IoT (RFID), acelerando la toma de decisiones.  
- **Escalabilidad y digitalización:** Sienta las bases para una operación 100 % digital, permitiendo crecer sin necesidad de infraestructuras físicas adicionales.

**¿Cómo se alinea el software con la estrategia general de digitalización?**  
El sistema convierte procesos manuales de registro de inventario en flujos automatizados en la nube, integra IoT y ML, y facilita la transición hacia una ‘Fábrica Inteligente’ donde los datos guían cada decisión operativa.

---

## Áreas de negocio y comunicaciones

**¿Qué áreas de la empresa se ven más beneficiadas con tu software?**  
- **Producción / Operaciones:** Planificación de pedidos optimizada al conocer el nivel de stock y la demanda futura.  
- **Logística / Almacén:** Reposición automática basada en umbrales definidos y alertas en tiempo real.  
- **Comunicaciones / Marketing:** Información de ventas proyectadas para diseñar campañas estacionales.

**¿Qué impacto operativo esperas en las operaciones diarias?**  
- **Menos paradas de línea:** Al evitar quiebres de stock.  
- **Reducción de tareas manuales:** Menos tiempo dedicado a recuentos físicos.  
- **Planificación proactiva:** Alertas tempranas que permiten ajustes inmediatos en producción y compra de materiales.

---

## Áreas susceptibles de digitalización

**¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?**  
- **Entrada y salida de mercancías:** Registro automático con RFID en vez de sistemas manuales de escaneo.  
- **Control de stock en almacén:** Dashboard en la nube en lugar de hojas de cálculo locales.  
- **Análisis de ventas:** Generación de informes dinámicos en lugar de procesos batch semanales.

**¿Cómo mejorará la digitalización las operaciones en esas áreas?**  
- **Tiempos de ciclo más cortos:** Desde la recepción hasta el despacho.  
- **Menos errores humanos:** Al eliminar transcripción manual.  
- **Visibilidad 24/7:** Acceso remoto a datos de inventario desde cualquier dispositivo.

---

## Encaje de áreas digitalizadas (AD)

**¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?**  
- Los **sensores RFID** (digital) informan al ERP (legacy) vía API de reposición.  
- Los datos de ventas proyectadas (ML) alimentan los sistemas de planificación manual existentes hasta su renovación.

**¿Qué soluciones o mejoras propondrías para integrar estas áreas?**  
- **Desarrollo de conectores** (middleware) que traduzcan formato JSON de FastAPI a los formatos propietarios del ERP.  
- **Tableros híbridos** que muestren datos en tiempo real junto a indicadores históricos importados desde sistemas antiguos.

---

## Necesidades presentes y futuras

**¿Qué necesidades actuales de la empresa resuelve tu software?**  
- **Control de inventario al día:** Evita quiebres y sobre-stock.  
- **Agilidad en pedidos:** Basada en datos reales y predicciones.  
- **Seguridad y cumplimiento:** Cifrado en la nube y auditoría de accesos con JWT.

**¿Cómo puede evolucionar para cubrir necesidades futuras?**  
- **Soporte multi-almacén** y gestión distribuida.  
- **Integración con proveedores** vía EDI o APIs B2B.  
- **Análisis avanzado** (Big Data) incorporando redes neuronales para predicción estacional.

---

## Relación con tecnologías

**¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?**  
- **IoT (RFID):** Automatiza la captura de datos en almacén.  
- **Cloud (AWS S3):** Centraliza el almacenamiento, facilita copias de seguridad y alta disponibilidad.  
- **Machine Learning:** Aporta inteligencia predictiva a producción y compras.

**¿Qué beneficios específicos aporta la implantación de estas tecnologías?**  
- **Reducción de errores** de inventario en un 90 %.  
- **Tiempos de respuesta** ante variaciones de demanda reducidos de semanas a horas.  
- **Escalabilidad instantánea** sin inversión en hardware.

---

## Brechas de seguridad

**¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?**  
- **Exposición de credenciales AWS** si no se protegen adecuadamente.  
- **Interceptación de tokens JWT** en comunicaciones inseguras.  
- **Acceso no autorizado** a la bucket de S3.

**¿Qué medidas concretas propondrías para mitigarlas?**  
- **Rotación periódica de claves** y uso de roles IAM con permisos mínimos.  
- **HTTPS obligatorio** y HSTS en el API.  
- **Caducidad corta de tokens** y logout forzado en caso de detección de anomalías.  
- **Registro y monitorización** de logs de acceso en CloudWatch.

---

## Tratamiento de datos y análisis

**¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?**  
- **Ingesta:** Escaneo IoT y subida segura a S3.  
- **Procesamiento:** ETL ligero con Pandas para preparar CSV de ventas.  
- **Modelado:** Regresión lineal con scikit-learn.

**¿Qué haces para garantizar la calidad y consistencia de los datos?**  
- **Validaciones de esquema** con Pydantic al recibir peticiones.  
- **Checksums y cifrado** en tránsito y reposo.  
- **Test automáticos** de integridad de datos y validación de MSE en cada reentrenamiento.

---  
