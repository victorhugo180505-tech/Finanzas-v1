import itertools as iter



class Movimiento :
    def __init__(self,id,nombre,tipo,monto,fecha,estado="Activo",aceptaParcial = None,frecuencia = 0,penalizacionFija=False,porc_penalizacion = 0):
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
    


def busquedaBinaria(indice:int,lista:list[Movimiento]):
    ini = 0
    final = len(lista)
    res = -1
    while(ini <= final):
        mid = int((ini+final)/2)
        #print(mid)
        if(indice>lista[mid].id):
            ini = mid+1
        elif(indice<lista[mid].id):
            final = mid-1
        else:
            res = mid
            break
            
    
    return res
class Usuario:
    def __init__(self,balance = 0, nombre = "",supervivencia=0):
        self.balance = balance
        self.nombre = nombre
        self.supervivencia= supervivencia




class SimulacionSemanal :
    def __init__(self,movimientosIniciales = None):
        
        self.movimientos = []    
        
        for movimiento in movimientosIniciales:
            self.movimientos.append(movimiento)

    def agregarMovimiento(self,movement:Movimiento):
        self.movimientos.append(movement)
    

    def eliminarMovimiento(self,id = -1, nombre = ""):
        if id == -1:
            for movimiento in self.movimientos:
                if(movimiento.nombre==nombre):
                    self.movimientos.remove(movimiento)
                    break
            
            
        else:
            indice = busquedaBinaria(id,self.movimientos)
            if indice != -1:
                self.movimientos.pop(indice)


    def correrSimulacion(self,user:Usuario):
        """
        Realiza cambios en el balance del usuario en base a los movimientos almacenados,
        retorna una lista con los movimientos que no se alcanzaron a cubrir.
        """
        #egresos = []
        eventos = []
        deudas = []
        for movimiento in self.movimientos:


            """if movimiento.estado == "Activo":
                eventos.append(movimiento)
                if movimiento.tipo == "Ingreso":
                    user.balance+=movimiento.monto
                elif movimiento.tipo == "Deuda":
                    egresos.append(movimiento)
                else:
                    user.balance-=movimiento.monto"""
            if movimiento.estado == "Activo" and (movimiento.tipo == "Ingreso" or movimiento.tipo == "Gasto"):
                eventos.append(movimiento)
            else:
                deudas.append(movimiento)
        #aqui ya filtramos para quedarnos con los activos y descartar los que ya no me importan, tambien filtramos solo los obligatorios
        #Modificando
    





        




       
        #return balance
            

            



    
        
    