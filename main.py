from typing import List

class Asiento :
    def __init__(self, color, precio, registro) :
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color:str) :
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"] :
            self.color = color

class Motor :
    def __init__(self, numeroCilindros, tipo, registro) :
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro:int) :
        self.registro = registro

    def asignarTipo(self, tipo:str) :
        if tipo in ["electrico", "gasolina"] :
            self.tipo = tipo

class Auto :
    cantidadCreados = 0
    def __init__(self, modelo:str, precio:int, asientos:List[Asiento], marca:str, motor:Motor, registro:int) :
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self) :
        cantidadAsientos = 0
        for asiento in self.asientos :
            if asiento != None :
                cantidadAsientos += 1
        
        return cantidadAsientos
    
    def verificarIntegridad(self) :
        if self.motor != None and self.registro != self.motor.registro :
            return "Las piezas no son originales"
        
        for asiento in self.asientos :
            if asiento != None and self.registro != asiento.registro :
                return "Las piezas no son originales"
            
        return "Auto original"