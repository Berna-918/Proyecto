import random

#Panel de inicio para poder elegir el auto 
def mostrar_menu():
    print("\n 🏁 Simulador de Carrera de Autos🏁")
    print("1. Escoge tu auto para competir")
    print("2. Ve tu historial de carreras")
    print("3. Salir")

#Muestra todos los autos disponibles que tiene en el Garage.
def elegir_auto():
    autos = ["Ferrari LaFerrari", "Lamborghini Veneno", "McLaren Senna", "Bugatti Veyron", "Porsche 918 Spyder", "Pagani Zonda R", "Koenigsegg One:1", "Audi R8", "Aston Martin Valkyrie"]
    print("\nBienvenido a tu Garage:")
    for i, auto in enumerate(autos, 1):
        print(f"{i}. {auto}")
        
    #Muestra los valores y hasta que cantidad de autos puede seleccionar y tambien muestra si ha elegido un numero fuera de rango o si no es valido
    while True:
        try:
            eleccion = int(input("Elige un auto (1-9): "))
            if 1 <= eleccion <= 9:
                return autos[eleccion - 1]
            else:
                print("Número fuera de rango, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida, ingresa un número.")
            
#Muestra el apartado de velocidad y el limite que Km/h
def simular_carrera(auto_elegido, historial):
    competidores = ["Ferrari LaFerrari", "Lamborghini Veneno", "McLaren Senna", "Bugatti Veyron", "Porsche 918 Spyder", "Pagani Zonda R", "Koenigsegg One:1", "Audi R8", "Aston Martin Valkyrie"]
    velocidades = {auto: random.randint(200, 450) for auto in competidores}
    velocidades[auto_elegido] = random.randint(200, 450)
    
    #Inicia la carrera  y muestra quien gana y quien pierde y muestra mensaje con el otro carro con el que perdio y el mensaje que perdio el coche.
    ganador = max(velocidades, key=velocidades.get)
    print("\n🚦Inicia la carrera🚦")
    for auto, velocidad in velocidades.items():
        print(f"{auto}: {velocidad} km/h")
    
    if ganador == auto_elegido:
        print(f"\n🏆 🏁 ¡El ganador es {ganador}! 🏁")
        print("Vaya vaya, ¡has ganado! 🎉🏁")
    else:
        print(f"\n🏆 🏁 ¡El ganador es {ganador}! 🏁")
        print("Vaya has perdido 😔 y has perdido tu coche")
    
    #Muestra el historial de cada carrera que ha realizado si ha ganado o ha perdido.
    historial.append((auto_elegido, velocidades[auto_elegido], ganador))

def ver_historial(historial):
    if not historial:
        print("\n No hay carreras registradas aún.")
    else:
        print("\n Historial de Carreras:")
        for i, (auto, velocidad, ganador) in enumerate(historial, 1):
            print(f"{i}. Elegiste: {auto} ({velocidad} km/h) | Ganador: {ganador}")

#Muestra si se quiere salir de la carrera o si quiere ver su historial o volver a intentarlo
def main():
    historial = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            auto_elegido = elegir_auto()
            simular_carrera(auto_elegido, historial)
        elif opcion == "2":
            ver_historial(historial)
        elif opcion == "3":
            print("Saliendo del simulador. Te veo en la próxima carrera.")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()

#Bernabé Emanuel Guevara Moreno.