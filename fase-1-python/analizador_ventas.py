# ============================================
#  ANALIZADOR DE VENTAS - Python Nativo
#  Sin Pandas, sin librerías externas
# ============================================

import csv
import json
from collections import defaultdict

# 1. LEER EL CSV
archivo_csv = "supermarket_sales.csv"
ventas = []

with open(archivo_csv, mode='r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        ventas.append(fila)

print(f"✅ Total de transacciones leídas: {len(ventas)}")

# 2. CALCULAR TOTALES POR CATEGORÍA (Product line)
totales_por_categoria = defaultdict(float)

for venta in ventas:
    categoria = venta['Product line']
    total = float(venta['Total'])
    totales_por_categoria[categoria] += total

print("\n📊 Ventas por categoría:")
for categoria, total in sorted(totales_por_categoria.items(), key=lambda x: x[1], reverse=True):
    print(f"  {categoria}: ${total:,.2f}")

# 3. PRODUCTO MÁS VENDIDO (por cantidad)
cantidad_por_producto = defaultdict(int)

for venta in ventas:
    producto = venta['Product line']
    cantidad = int(venta['Quantity'])
    cantidad_por_producto[producto] += cantidad

producto_top = max(cantidad_por_producto, key=cantidad_por_producto.get)
print(f"\n🏆 Producto más vendido: {producto_top} ({cantidad_por_producto[producto_top]} unidades)")

# 4. VENTAS POR CIUDAD
ventas_por_ciudad = defaultdict(float)

for venta in ventas:
    ciudad = venta['City']
    total = float(venta['Total'])
    ventas_por_ciudad[ciudad] += total

print("\n🌆 Ventas por ciudad:")
for ciudad, total in sorted(ventas_por_ciudad.items(), key=lambda x: x[1], reverse=True):
    print(f"  {ciudad}: ${total:,.2f}")

# 5, VENTAS POR METODOS DE PAGO
ventas_por_metodo_de_pago = defaultdict(float)

for venta in ventas:
	metodo = venta['Payment']
	total = float(venta['Total'])
	ventas_por_metodo_de_pago[metodo] += total

print("\n💳 ventas por metodo de pago:")
for metodo, total in sorted(ventas_por_metodo_de_pago.items(), key=lambda x: x[1], reverse=True):
	print(f" {metodo}: ${total:,.2f}")


# 6. PROMEDIO DE RATING POR CATEGORÍA
rating_por_categoria = defaultdict(list)

for venta in ventas:
    categoria = venta['Product line']
    rating = float(venta['Rating'])
    rating_por_categoria[categoria].append(rating)

print("\n⭐ Rating promedio por categoría:")
for categoria, ratings in rating_por_categoria.items():
    promedio = sum(ratings) / len(ratings)
    print(f"  {categoria}: {promedio:.2f}/10")

# 7. EXPORTAR RESULTADOS A JSON
resultados = {
    "total_transacciones": len(ventas),
    "ventas_por_categoria": dict(totales_por_categoria),
    "producto_mas_vendido": {
        "nombre": producto_top,
        "cantidad": cantidad_por_producto[producto_top]
    },
    "ventas_por_ciudad": dict(ventas_por_ciudad),
    "ventas_por_metodo_de_pago": dict(ventas_por_metodo_de_pago),
    "rating_promedio_por_categoria": {
        cat: round(sum(vals)/len(vals), 2) for cat, vals in rating_por_categoria.items()
    }
}

with open("resultados_ventas.json", "w", encoding='utf-8') as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)

print("\n💾 Resultados exportados a: resultados_ventas.json")