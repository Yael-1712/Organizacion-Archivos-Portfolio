import pandas as pd
import matplotlib.pyplot as plt
import os

# =====================================
# 1. CARGA DE DATOS (PARTE I)
# =====================================
directorio = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(directorio, "ventas_tecnologia.csv")

try:
    df = pd.read_csv(ruta_csv)
    # Limpieza de nombres por si hay espacios
    df.columns = df.columns.str.strip()
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

# =====================================
# 2. PROCESAMIENTO (REPORTE TABULAR)
# =====================================
# Cálculo de ingresos
df["ingresos"] = df["cantidad"] * df["precio_unitario"]

# Agrupaciones solicitadas
ventas_producto = df.groupby("producto")["cantidad"].sum()
ventas_mes = df.groupby("mes", sort=False)["cantidad"].sum()
ingresos_producto = df.groupby("producto")["ingresos"].sum()
ingresos_mes = df.groupby("mes", sort=False)["ingresos"].sum()

# Identificación de productos clave
producto_estrella = ventas_producto.idxmax()
producto_menos_v = ventas_producto.idxmin()
mes_top_ingresos = ingresos_mes.idxmax()
producto_mas_ganancia = ingresos_producto.idxmax()

# Imprimir Reportes Tabulares
print("--- REPORTE 1: VENTAS TOTALES POR PRODUCTO ---")
print(ventas_producto, "\n")
print("--- REPORTE 2: VENTAS TOTALES POR MES ---")
print(ventas_mes, "\n")
print("--- REPORTE 3: INGRESOS POR PRODUCTO ---")
print(ingresos_producto.map("${:,.2f}".format), "\n")
print(f"--- REPORTE 4: PRODUCTO MÁS VENDIDO: {producto_estrella} ---\n")

# =====================================
# 3. VISUALIZACIONES (PARTE II)
# =====================================
plt.style.use('ggplot')

# Gráfica de Barras (Ventas por Producto)
plt.figure(figsize=(9, 5))
ventas_producto.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")
plt.tight_layout()

# Gráfica de Líneas (Evolución Mensual)
plt.figure(figsize=(9, 5))
ventas_mes.plot(kind='line', marker='o', linewidth=2, color='green')
plt.title("Evolución Mensual de Ventas")
plt.xlabel("Mes")
plt.ylabel("Cantidad")
plt.tight_layout()

# Gráfica Circular (Porcentaje de Ventas)
plt.figure(figsize=(7, 7))
ventas_producto.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Porcentaje de Ventas por Producto")
plt.ylabel("")

# Mostrar todas las gráficas (se abrirán una tras otra o juntas según tu editor)
plt.show()

# =====================================
# 4. INTERPRETACIÓN (PARTE III Y IV)
# =====================================
print("="*50)
print("JERARQUÍA E INTERPRETACIÓN DE INFORMACIÓN")
print("="*50)
print(f"1. Producto con mayores ingresos: {producto_mas_ganancia}")
print(f"2. Producto menos vendido:       {producto_menos_v}")
print(f"3. Mes más rentable:             {mes_top_ingresos}")
print(f"4. Producto prioritario (Inv.):  {producto_estrella}")

print("\n--- ANÁLISIS PARA TOMA DE DECISIONES ---")
print(f"• El producto más importante es la {producto_mas_ganancia} por su alto valor de ingreso.")
print(f"• Información crítica: El volumen de ventas en {mes_top_ingresos} sugiere picos estacionales.")
print(f"• Promoción: Se deben promocionar más los {producto_menos_v} para rotar inventario.")
print(f"• Oportunidad: El mes de {mes_top_ingresos} representa la mejor oportunidad de cierre de ventas.")