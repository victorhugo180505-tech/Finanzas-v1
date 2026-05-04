import logica as l

prueba =  l.Movimiento(id=1,nombre="IngresoPrueba",tipo="Ingreso",estado="Activo",monto=550,fecha="2026/04/16",aceptaParcial=None,frecuencia=0,porc_penalizacion=0)
prueba2 =  l.Movimiento(id=2,nombre="GastoPrueba",tipo="Gasto",estado="Activo",monto=500,fecha="2026/04/17",aceptaParcial=False,frecuencia=0,porc_penalizacion=0)
#print(prueba2)
arreglo = []
arreglo.append(prueba)
arreglo.append(prueba2)
simulacion1 = l.SimulacionSemanal(arreglo)

prueba3 =  l.Movimiento(id=3,nombre="DeudaPrueba",tipo="Deuda",estado="Activo",monto=50,fecha="2026/04/17",aceptaParcial=True,frecuencia=0,porc_penalizacion=20)
simulacion1.agregarMovimiento(prueba3)

for movimiento in simulacion1.movimientos:
    print(movimiento)

simulacion1.eliminarMovimiento(nombre="DeudaPrueba")
print("\n\n")
for movimiento in simulacion1.movimientos:
    print(movimiento)

userTester = l.Usuario(nombre = "krazy",balance=128)
print("krazy")
print(l.busquedaBinaria(2,arreglo))
#print(userTester.balance)
#simulacion1.correrSimulacion(userTester)
#userTester.balance = 
#userTester.balance-=100
#print(userTester.balance)
