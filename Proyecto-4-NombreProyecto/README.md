# Pipeline de Cómputo Fuera de Núcleo (Out-of-Core) para Analítica de Datos Masivos

---

##  1. Especificaciones de Diseño y Reto de Infraestructura

Este módulo implementa un motor algorítmico optimizado en Python diseñado para resolver problemas de límites de memoria física en entornos de Big Data. Su función principal es la ingesta y análisis estadístico síncrono de conjuntos de datos tabulares a gran escala (datasets indexados de registros médicos, pacientes y variables clínicas) garantizando un consumo de memoria RAM plano y constante mediante el aislamiento de flujos independientes de procesamiento.

| Métrica de Arquitectura | Especificación del Pipeline |
| :--- | :--- |
| **Paradigma de Ingesta** | Stream de Datos por Fragmentación (*Chunking*) |
| **Tamaño de Ventana Lógica** | $100,000$ registros por ciclo iterativo |
| **Persistencia de Entrada** | Serialización plana indexada (CSV masivo) |
| **Persistencia de Salida** | Mapeo estructurado llave-valor (JSON Balanceado) |

---

##  2. Topología del Pipeline de Datos

El flujo de procesamiento mitiga la sobrecarga del sistema operativo al operar de manera puramente asíncrona por consola, distribuyendo sus dependencias en las siguientes capas de persistencia:

* **`datos.py` [Núcleo de Cálculo] :** Script de ingeniería encargado de la segmentación del archivo fuente, la gestión de acumuladores dinámicos vectorizados y la exportación de metadatos.
* **`Resultados de Auditoría` [Capa de Salida] :** Archivo de datos final (`resultados.json`) que consolida de manera compacta el resumen estadístico, histogramas de extremos y muestras aleatorias para su consumo en microservicios o dashboards de Business Intelligence.

---

##  3. Estrategia de Optimización de Memoria (Análisis de Flujo)

### Algoritmo de Consumo Plano (RAM Controlada)

* **Justificación Científica:** Cargar un dataset que excede la memoria caché del procesador en un único DataFrame (`pd.read_csv`) produce fallos críticos de segmentación e interrupciones del hilo de ejecución. Para resolverlo, el script implementa un bucle de lectura fragmentada basado en un puntero lógico que segmenta el archivo de entrada.
* **Mecanismo de Liberación Inmediata:** El pipeline abre un canal de comunicación directo al archivo, carga exclusivamente el bloque de registros configurado, actualiza instantáneamente los acumuladores globales y purga los objetos temporales de la memoria RAM antes de llamar al bloque subsecuente.

---

##  4. Matriz de Computación Estadística y Muestreo

Durante el ciclo iterativo de los bloques de datos, el core analítico ejecuta en paralelo operaciones de vectorización matemática de alta velocidad:

1.  **Monitoreo de Extremos Límites:** Evalúa en tiempo real los valores máximos y mínimos de variables continuas y discretas (temperaturas y edades de pacientes) mediante funciones de comparación de baja latencia, calculando simultáneamente la media aritmética ponderada de la población global.
2.  **Mapeo de Frecuencias Absolutas:** Utiliza estructuras de indexación rápida (`pandas.Series`) para acumular y ordenar la recurrencia de clasificaciones categóricas (como las especialidades médicas de mayor demanda y medicamentos de alta rotación).
3.  **Aislamiento de Muestras de Control:** Extrae subconjuntos aleatorios controlados a lo largo del flujo masivo para auditorías de calidad de datos, garantizando la trazabilidad del proceso antes de consolidar el JSON final.
