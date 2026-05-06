import itertools as iter
import archivos as f
import datetime as dt

class Movimiento :
    def __init__(self,id,nombre,tipo,monto,fecha:str,estado="activo",aceptaParcial = False,frecuencia = 0,penalizacionFija=False,porc_penalizacion = 0):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
        self.monto = monto
        self.aceptaParcial = aceptaParcial
        self.fecha = fecha
        
        self.frecuencia = frecuencia
        self.porc_penalizacion = porc_penalizacion
        self.penalizacionFija = penalizacionFija
    
    def __str__(self):
        cadena = f"id: {self.id} Nombre: {self.nombre} {self.tipo}-${self.monto} (Fecha: {self.fecha})"
        return cadena
    

def penalizacion(movimiento):
    if movimiento["penalizacionFija"] == False:
        return movimiento["porc_penalizacion"] * movimiento["monto"] / 100
    else:
        return movimiento["porc_penalizacion"]

class Usuario:
    def __init__(self,balance = 0,supervivencia=0):
        self.balance = balance
        self.supervivencia= supervivencia




"""class SimulacionSemanal :
    def __init__(self,movimientosIniciales = None):
        
        self.movimientos = []    
        
        for movimiento in movimientosIniciales:
            self.movimientos.append(movimiento)"""



def correrSimulacion(user:Usuario,lista_movimientos:list[dict],fecha_inicial:str):
    """
    Realiza cambios en el balance del usuario en base a los movimientos almacenados,
    retorna una lista con pares listos para ser graficados y los movimientos que no se alcanzaron a cubrir.
    """
    movimientos_activos = []
    for movimiento in lista_movimientos:
        if movimiento["estado"]=="activo":
            movimientos_activos.append(movimiento)
    fecha_inicio = dt.datetime.strptime(fecha_inicial,"%Y-%m-%d")
    fecha_actual = fecha_inicio
    #fecha_inicial = fecha_inicial - dt.timedelta(days=1)
    graficacion = []
    deudas = []
    while(len(movimientos_activos) > 0):
        fecha_limite = fecha_inicio + dt.timedelta(days=14)

        while(fecha_actual != fecha_limite):
            
            for movimiento in movimientos_activos.copy():

                if fecha_actual== dt.datetime.strptime(movimiento["fecha"],"%Y-%m-%d"):

                    if movimiento["tipo"]=="ingreso":
                        user.balance+=movimiento["monto"]
                    
                    elif movimiento["tipo"]=="gasto":
                        user.balance-=movimiento["monto"]
                    
                    else:
                        deudas.append(movimiento)
                    movimientos_activos.remove(movimiento)
                                    
                
            graficacion.append([ fecha_actual,user.balance])
            fecha_actual = fecha_actual + dt.timedelta(days=1)
        fecha_inicio = fecha_limite
        #Aqui ya tengo los saldos considerando solamente los gastos e ingresos. Los cuales son obligatorios aunque se llegue a negativo.
    deudas_ordenadas = sorted(deudas,key=lambda x: (-penalizacion(x),x["fecha"]))
    
    fecha_inicio = dt.datetime.strptime(fecha_inicial,"%Y-%m-%d")
    fecha_actual = fecha_inicio
    indice = -1
    for elemento in graficacion:
        indice+=1
        for deuda in deudas_ordenadas.copy():
            
            punto_mas_bajo = min(graficacion[indice:indice+14],key=lambda x: x[1])[1]
            limite = 0
            if indice+14 >= len(graficacion):
                limite = len(graficacion)-1
            else:
                limite = indice+14
            if punto_mas_bajo - deuda["monto"] >= user.supervivencia and graficacion[limite][0] >= dt.datetime.strptime(deuda["fecha"],"%Y-%m-%d"):
                for dia_futuro in graficacion[indice:]:
                    dia_futuro[1] -= deuda["monto"]
                deudas_ordenadas.remove(deuda)
            else:
                if dt.datetime.strptime(deuda["fecha"],"%Y-%m-%d") == elemento[0]:
                    modificador_indice = deudas_ordenadas.index(deuda)
                    deudas_ordenadas[modificador_indice]["fecha"] = dt.datetime.strftime(dt.datetime.strptime(deuda["fecha"],"%Y-%m-%d") + dt.timedelta(days=30),"%Y-%m-%d")
                    deudas_ordenadas[modificador_indice]["monto"] += penalizacion(deudas_ordenadas[modificador_indice])
                    deudas_ordenadas = sorted(deudas_ordenadas,key=lambda x: (-penalizacion(x),x["fecha"]))
                
      
    return graficacion,deudas_ordenadas
        

    #punto_mas_bajo = min(graficacion[i:],key=lambda x: x[1])[1]
    # if punto_mas_bajo - deuda["monto"] >= user.supervivencia:


 