from pydantic import BaseModel


class Orden(BaseModel):
    id: InterruptedError
    fecha:str
    usuario: str
    tienda: str
    valor:float


ordenes = {
    1: Orden (id=1 , fecha = "20-11-2020", usuario="pepe", tienda="dominos", valor=200),
    1: Orden (id=1 , fecha = "20-11-2020", usuario="ramon", tienda="pizzahat", valor=300),



}

def obtener_ordenes():
    #haga lo que tenga que hacer para conectarse a la base de datos y obtner todas las ordenes
    lista_ordenes=[]

    for e in ordenes:
        lista_ordenes.append(ordenes[e])
    return ordenes