from tinydb import TinyDB, Query
import logica as lg
db = TinyDB('datos.json')
tabla_usuario = db.table("usuario")
def insertarMovimiento(movimiento:lg.Movimiento):
    db.insert(movimiento.__dict__)

def obtenerMovimientos():
    return db.all()

def eliminarMovimiento(id_movimiento:int):

    Movement = Query()
    db.remove(Movement.id == id_movimiento)
    

def encontrarProximoId():
    temporal = db.all()
    if len(temporal)==0:
        return 1
    else:
        return max(temporal,key=lambda x: x["id"])["id"]+1
    
def actualizarMovimiento(id_movimiento:int,movimiento_actualizado:lg.Movimiento):
    movement = Query()
    db.update(movimiento_actualizado.__dict__,movement.id==id_movimiento)

def reiniciarDB():
    db.truncate()

def guardarUsuario(usuario:lg.Usuario):
    tabla_usuario.truncate()
    tabla_usuario.insert(usuario.__dict__)

def obtenerUsuario() -> lg.Usuario:
    datos = tabla_usuario.all()
    if len(datos)>0:
        datos_usuario = datos[0]
        return lg.Usuario(balance=datos_usuario["balance"],supervivencia=datos_usuario["supervivencia"])
    else:
        return lg.Usuario()