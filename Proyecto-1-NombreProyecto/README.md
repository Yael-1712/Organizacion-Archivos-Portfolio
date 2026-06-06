# Proyecto Corte 2: Sistema de Control y Gestión de Usuarios

---

## 1. Descripción del Sistema

Este módulo es una solución de software diseñada para regular, gestionar y auditar el control de usuarios. El sistema se compone de un componente analítico local desarrollado en Python que procesa la lógica de control interna, interactuando de manera directa con una interfaz web de supervisión y gestión desarrollada en PHP, HTML5 y CSS3. El sistema intercepta las peticiones de los usuarios, evalúa sus parámetros y permite visualizar el estado del entorno de manera dinámica.

---

## 2. Arquitectura de Archivos y Flujo de Datos

La estructura interna del proyecto centraliza sus componentes en la raíz del directorio principal, distribuyendo las responsabilidades de la siguiente manera:

1. **`diagrama de flujo.jpeg`** : Documentación gráfica y mapeo del algoritmo que describe visualmente la lógica, decisiones y el flujo de trabajo del sistema.
2. **`usuarios.json`** : Base de datos local estructurada en formato plano que almacena las credenciales, registros e información persistente de los usuarios del sistema.
3. **`style.css`** : Hoja de estilos encargada del diseño responsivo, la distribución tipográfica y la presentación visual de la interfaz de usuario.
4. **`index.php`** : Monitor e interfaz web principal que renderiza el entorno gráfico del sistema, permitiendo la interacción con los datos en tiempo real.
5. **`control.py`** : Script y lógica central de procesamiento (Python) encargado de ejecutar las rutinas de control, validación y manipulación de los flujos del sistema.

---

## 3. Justificación Científica de Formatos y Modos de Acceso

### Estructura de Datos en Formato Organizado (`usuarios.json`)

* **Justificación:** Se seleccionó el formato JSON (JavaScript Object Notation) para la persistencia de los usuarios autorizados debido a que proporciona una organización jerárquica basada en pares clave-valor. Esto permite almacenar colecciones de datos complejas sin el sobrecosto operativo de un motor de base de datos relacional tradicional, asegurando portabilidad absoluta y una sintaxis estandarizada nativamente legible tanto por el backend en Python como por el frontend en PHP.
* **Modo de acceso:** En la lógica de control, los scripts acceden a este flujo de datos optimizando el uso de memoria RAM a través de mapeos directos (como la librería nativa `json`), lo que agiliza los tiempos de búsqueda, lectura y actualización mediante comparaciones lógicas directas.

---

## 4. Evitada de Código Fijo

Para asegurar el cumplimiento de las buenas prácticas de desarrollo de software y garantizar la escalabilidad, el sistema implementa un desacoplamiento estricto. No existen identificadores, nombres ni parámetros de usuarios quemados (*hardcoded*) dentro del código fuente de `control.py` o `index.php`. Toda validación de identidad e información de entrada se resuelve dinámicamente consultando el archivo de configuración externo `usuarios.json`, permitiendo altas, bajas o modificaciones de personal de forma externa sin alterar la lógica de programación base.
