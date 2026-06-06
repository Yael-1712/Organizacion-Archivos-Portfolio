# Módulo Analítico: Pipeline de Inteligencia de Negocios y Visualización de Datos de Ventas

---

##  Alcance Funcional y Objetivos de la Auditoría Comercial

Este desarrollo actúa como un motor de Business Intelligence (BI) programado de extremo a extremo en Python para auditar la salud financiera y comercial de un catálogo tecnológico. Su propósito principal es la ingesta estructurada de registros históricos de transacciones para transformarlos de forma automatizada en reportes tabulares consolidados, métricas de rendimiento (KPIs) y proyecciones gráficas de tendencias que mitiguen el sesgo de datos y optimicen la toma de decisiones ejecutivas en el inventario.

---

## 🗺️ Mapa de Componentes y Flujo de Información (Data Pipeline)

El entorno analítico desacopla la persistencia de datos del núcleo de procesamiento matemático de la siguiente manera:

1. **`evaluacion/ventas_tecnologia.csv` (Origen de Datos):** Set de datos plano estructurado en formato tabular que almacena las variables nativas del negocio: variables temporales (`mes`), categóricas (`producto`), cuantitativas discretas (`cantidad`) y continuas (`precio_unitario`).
2. **`evaluacion/reporte.py` (Motor de Ingesta, Procesamiento y Renderizado):** Script monolítico estructurado en fases secuenciales que se encarga de la extracción, transformación, cálculo matemático de ingresos agregados y la inyección de datos hacia la interfaz de visualización (`matplotlib`).

---

##  Ingeniería de Transformación y Estrategia de Persistencia Dinámica

### Consolidación y Tratamiento del Set de Datos (`ventas_tecnologia.csv`)

* **Criterio de Arquitectura:** Se explota el uso del formato CSV (Comma-Separated Values) por su alta eficiencia en la serialización y transferencia de registros planos indexados. Esto permite la lectura nativa por bloques mediante punteros lógicos, reduciendo la latencia de entrada/salida (I/O) en comparación con sistemas de bases de datos tradicionales.
* **Estrategia de Manipulación en Memoria:** El motor en Python inicializa un proceso de aislamiento dinámico a través de `pandas` para normalizar las cadenas de texto (eliminando espacios muertos en las columnas). Posteriormente, ejecuta un algoritmo de vectorización para calcular de manera síncrona los ingresos brutos individuales ($cantidad \times precio\_unitario$) e implementar agrupamientos matriciales (`groupby`) que clasifican el rendimiento por producto y cronología mensual.

---

##  Capa de Visualización Avanzada e Interpretación de Decisiones

El script rompe con los esquemas de reporte estáticos al procesar de forma automatizada tres capas de abstracción gráfica para el análisis gerencial:
* **Análisis de Tendencia Temporal:** Una gráfica de líneas continuas diseñada para mapear la evolución y el comportamiento estacional de las ventas a lo largo de los meses.
* **Análisis de Distribución de Mercado:** Un gráfico circular parametrizado porcentualmente para identificar la cuota de participación e impacto financiero de cada producto sobre los ingresos totales.
* **Optimización de Inventario:** Un sistema de reporte por consola que aísla de manera inteligente las variables críticas del negocio: el producto estrella, el producto de menor rotación y el mes con mayor rendimiento financiero, facilitando la planificación logística sin intervención manual en el código fuente.
