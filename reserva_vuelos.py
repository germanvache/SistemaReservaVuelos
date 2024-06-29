'''SISTEMA DE RESERVAS DE VUELOS 
Imagina que estás desarrollando un sistema de reservas de vuelos para una 
aerolínea. Crea un sistema de clases que permita a los usuarios realizar 
reservas de vuelos. Aquí tienes una posible estructura:

- Clase base: `Vuelo`
 - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de 
pasajeros
 - Métodos: agregar pasajero, verificar disponibilidad de asientos

- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
 - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones, 
trabajo)

Resuelve el problema creando instancias de estas clases y realizando 
reservas para diferentes vuelos y tipos de vuelos especiales
'''

class Vuelo:
    def __init__(self, numero, origen, destino, capacidad):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []

    def verificar_disponibilidad(self):
        return(self.capacidad - len(self.pasajeros))

    def agregar_pasajero(self, pasajero):
        if self.verificar_disponibilidad() > 0:  # Llamamos a un metodo dentro de otro metodo dentro de la misma clase
            self.pasajeros.append(pasajero)
            print(f"Pasajero {pasajero} agregar al vuelo {self.numero}")
        else:
            print("No hay asientos disponibles en este vuelo")

class VueloEspecial(Vuelo):  # Clase Derivada
    def __init__(self, numero, origen, destino, capacidad, motivo): 
        super().__init__(numero, origen, destino, capacidad) # herencia de atributos y metodos
        self.motivo = motivo


# Ejemplo de Uso
vuelo_regular = Vuelo("UA30", "NY", "MAD", 150)
vuelo_regular.agregar_pasajero("Juan")

print("Asientos disponibles:", vuelo_regular.verificar_disponibilidad())

vuelo_especial = VueloEspecial("UA31", "MIA", "BAR", 100, "Vacaciones")
vuelo_especial.agregar_pasajero("Laura")
print("Asientos disponibles en el vuelo especial:", vuelo_especial.verificar_disponibilidad())
print("Motivo del vuelo especial:", vuelo_especial.motivo)