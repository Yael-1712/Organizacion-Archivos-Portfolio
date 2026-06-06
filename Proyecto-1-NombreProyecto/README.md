# Proyecto Corte 1: Sistema de Captura, Procesamiento y Filtrado de Información

---

##  Contextualización y Propósito del Sistema

Este módulo representa una solución de software orientada a la recolección estandarizada, procesamiento lógico y segmentación de datos de entrada. El sistema integra una interfaz web frontend desarrollada en HTML5 y CSS3 para la captura de parámetros, la cual interactúa con un backend dinámico en PHP encargado del procesamiento inmediato de las solicitudes. Adicionalmente, se acopla un componente analítico programado en Python para la manipulación avanzada y generación de reportes basados en la información recolectada, consolidando un flujo de trabajo íntegro y automatizado.

---

##  Distribución del Código Fuente y Componentes

La arquitectura interna del proyecto se distribuye de manera modular dentro del directorio principal, asignando responsabilidades específicas a cada uno de sus elementos:

1. **`proyecto-corte1/formulario.html`** : Interfaz gráfica inicial que actúa como el punto de captura de datos y envío de parámetros por parte del usuario.
2. **`proyecto-corte1/estilos.css`** : Capa estática encargada de la maquetación visual, diseño responsivo y la estandarización estética de los formularios y vistas.
3. **`proyecto-corte1/procesar.php`** : Controlador backend de primera capa encargado de recibir, validar y canalizar la información enviada desde la interfaz web hacia los archivos de persistencia.
4. **`proyecto-corte1/visualizar.php`** : Módulo web dinámico diseñado para la lectura y renderizado en tiempo real de los datos almacenados de forma estructurada.
5. **`proyecto-corte1/generacion.py`** : Script analítico en Python diseñado para procesar el conjunto de datos global, ejecutar algoritmos de automatización y generar salidas específicas.
6. **`proyecto-corte1/maestro.txt`** : Archivo de persistencia plano que actúa como el repositorio centralizado e histórico de todas las entradas del sistema.
7. **`proyecto-corte1/filtrado.txt`** : Registro de salida secuencial que almacena exclusivamente los datos depurados bajo reglas lógicas específicas de exclusión o segmentación.

---

##  Fundamentación Técnica de Almacenamiento y Canales de Datos

### Gestión de Información en Estructuras Secuenciales (`maestro.txt` y `filtrado.txt`)

* **Análisis de Selección:** Se optó por el uso de archivos de texto plano para el almacenamiento debido a la necesidad de implementar una persistencia ligera, veloz y de baja sobrecarga en los procesos de escritura concurrente. Esta estructura permite un registro lineal idóneo para operaciones de auditoría y almacenamiento masivo rápido sin depender de servicios de bases de datos de terceros.
* **Mecanismo de Manipulación Híbrida:** 
  * El entorno PHP interactúa mediante canales de streaming en modos de anexado y lectura lineal continua para registrar y visualizar las entradas sin saturar el servidor.
  * El motor de Python (`generacion.py`) accede al flujo de datos del archivo maestro para parsear la información, aplicar filtros algorítmicos complejos y volcar las métricas resultantes de forma automatizada dentro del archivo de salida filtrado.

---

##  Buenas Prácticas y Flexibilidad del Desarrollo

Con el fin de asegurar el aislamiento de responsabilidades y la modularidad del software, el sistema divide rígidamente la adquisición de datos de su almacenamiento y procesamiento analítico. La lógica de filtrado y generación de reportes se encuentra completamente desacoplada de la interfaz de usuario, garantizando que las reglas de negocio puedan ser modificadas directamente en el script de Python o PHP sin comprometer la integridad del frontend ni la estructura del repositorio de datos maestro.
