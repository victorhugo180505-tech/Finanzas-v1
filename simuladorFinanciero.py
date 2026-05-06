import logica as l

# --- ESCENARIO DE PRUEBA ---

# 1. Usuario con 1000 pesos y quiere conservar al menos 200 siempre
profe_user = l.Usuario(balance=1000, supervivencia=200)

# 2. Movimientos (simulando TinyDB)
datos_prueba = [
    {"id": 1, "tipo": "ingreso", "monto": 500, "fecha": "2026-05-08", "estado": "activo"}, 
    {"id": 2, "tipo": "gasto", "monto": 300, "fecha": "2026-05-10", "estado": "activo"},   
    {"id": 3, "tipo": "deuda", "monto": 1200, "fecha": "2026-05-07", "estado": "activo", 
     "penalizacionFija": False, "porc_penalizacion": 10} 
]

# 3. Ejecutar
historial, pendientes = l.correrSimulacion(profe_user, datos_prueba, "2026-05-06")

# 4. Ver resultados
print("--- HISTORIAL DE SALDOS ---")
for dia in historial:
    print(f"Fecha: {dia[0].strftime('%Y-%m-%d')} | Saldo: ${dia[1]}")

print("\n--- DEUDAS QUE NO SE PUDIERON PAGAR ---")
for d in pendientes:
    print(f"Pendiente: {d['monto']} para la fecha {d['fecha']}")