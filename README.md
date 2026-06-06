# Portafolio de Arquitectura y Organización de Archivos - Semestre 2026

---

## Perfil del Alumno

* **Nombre:** Yael Alexander Calderon Reyes
* **Carrera:** Ingeniería en Informática
* **Institución:** Instituto Tecnológico Superior de Lerdo
* **Materia:** Administración y Organización de Datos

---

## Índice de Proyectos

A continuación se presenta el resumen interactivo de los componentes desarrollados en el ciclo académico. Los nombres de las carpetas coinciden directamente con la arquitectura interna de cada solución:

| Repositorio / Carpeta | Enfoque Tecnológico Principal | Componentes Core | Mecanismo de Datos |
| :--- | :--- | :--- | :--- |
| **`Proyecto-1-NombreProyecto`** | Adquisición y Segmentación Web | PHP / HTML5 / CSS3 / Python | Archivos Planos (`.txt`) |
| **`Proyecto-2-NombreProyecto`** | Seguridad Perimetral y Monitoreo | Python (Consola) / PHP / CSS | Estructura Plana JSON |
| **`Proyecto-3-NombreProyecto`** | Inteligencia de Negocios (BI) | Python (`pandas` / `matplotlib`) | Set de Datos Estructurado (`.csv`) |
| **`Proyecto-4-NombreProyecto`** | Big Data / Ingeniería de Datos | Python (Algoritmo de *Chunking*) | Stream CSV a JSON |

---

##  Especificaciones de Arquitectura por Módulo

###  1. Proyecto-1-NombreProyecto (Sistema de Captura y Filtrado)
* **Propósito:** Creación de un ecosistema híbrido para la simulación de inventarios estandarizados (Autos a escala / Hot Wheels).
* **Flujo Operativo:** Un script analítico en Python (`generacion.py`) modela e inyecta dinámicamente un dataset masivo en `maestro.txt`. El usuario interactúa mediante una interfaz web (`formulario.html`) donde envía palabras clave indexadas hacia `procesar.php`, aislando los resultados en `filtrado.txt` para su posterior renderizado estético en `visualizar.php`.

###  2. Proyecto-2-NombreProyecto (Control de Acceso Maquiladora)
* **Propósito:** Automatización del control de ingresos de personal de planta y disparo de alertas de seguridad en tiempo real.
* **Flujo Operativo:** Un controlador backend en Python (`control.py`) emula un lector físico de gafetes interactuando síncronamente en modo lectura con `usuarios.json`. Al detectar credenciales inválidas, gatilla una rutina de alerta inmutable que se anexa a la bitácora, permitiendo al monitor supervisor en PHP (`index.php`) pintar dinámicamente indicadores visuales restrictivos basados en estilos CSS.

###  3. Proyecto-3-NombreProyecto (BI y Visualización de Ventas)
* **Propósito:** Extracción, procesamiento matemático y análisis gráfico de transacciones financieras en catálogos tecnológicos.
* **Flujo Operativo:** El motor analítico en Python (`reporte.py`) ejecuta operaciones vectorizadas sobre el archivo estructurado `ventas_tecnologia.csv`. Utiliza funciones de agregación matricial para clasificar comportamientos cronológicos estacionales y renderiza de manera paralela visualizaciones avanzadas de cuotas de mercado (Gráficos lineales y circulares en `matplotlib`).

###  4. Proyecto-4-NombreProyecto (Procesamiento Masivo Big Data)
* **Propósito:** Procesamiento de flujos masivos de datos numéricos y categóricos médicos optimizando los límites de la memoria RAM.
* **Flujo Operativo:** Diseñado exclusivamente para prescindir de interfaces de usuario y maximizar el rendimiento de la CPU. El script de ingeniería `datos.py` abre un canal de streaming hacia un dataset de gran escala, fragmentándolo en ventanas lógicas estrictas de $100,000$ filas (*chunking*). Calcula de manera síncrona acumuladores globales de extremos térmicos, medias de edad y frecuencias de uso de fármacos, liberando la RAM en cada ciclo antes de serializar el resultado en un JSON balanceado.

---

##  Estándares de Ingeniería Aplicados (Evitada de Código Fijo)

Todos los proyectos integrados en este portafolio siguen estrictamente las directrices de desacoplamiento de código. Los datos de prueba, identificadores, catálogos de productos o registros de identidad **no se encuentran quemados (*hardcoded*)** dentro de la lógica de ejecución de los scripts de Python o PHP. Toda validación de parámetros se resuelve dinámicamente consumiendo las capas de persistencia externas configuradas (`.json`, `.csv`, `.txt`), garantizando la flexibilidad, portabilidad y mantenibilidad de las aplicaciones.
