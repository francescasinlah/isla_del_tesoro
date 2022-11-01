print("+++++++++++++++++++++++++++++++++")
print("Algoritmo de la Isla del tesoro")
print("+++++++++++++++++++++++++++++++++")

print("Bienvenido/a a la Isla. Tu misión será encontrar el Tesoro")

opciones=input("Existen dos opciones, ¿cuál opción eliges carro o moto? :")

if opciones=="carro":
    print("Te pasaste un semáforo en rojo y tuviste un accidente 'GAME OVER'")

elif opciones=="moto":
    tipo_vias=input("¿Ir por: via o calles?")
    if tipo_vias=="via":
        print("Te encuentras con una manifestación y un grupo de vándalos te pincha los neumáticos 'GAME OVER' ")
    elif tipo_vias=="calles":
        print("Tienes tres opciones, ¿cruzar el: puente, vórtice temporal ó portal?")   
        opciones=input("¿Cuál opción? (¿cruzar el: puente, vórtice temporal ó portal) :")
        if opciones=="puente":
            print("El puente está quebrado 'GAME OVER'")
        elif opciones=="portal":
            print("Te encuentras con monstruos de otro planeta 'GAME OVER'")
        elif opciones=="vortice temporal" or "vórtice temporal" or "vortice": 
            print("Fuiste teletransportado a una habitación y se está comenzando a llenar de agua")
            opciones=input("¿Buscar con qué salir de la habitación?: (puerta, llave o botón")
            if opciones=="puerta":
                print("Te quemas las manos")
            if opciones=="llave":
                print("Abrir la puerta")
                print("HAS GANADO")
            if opciones=="boton" or "botón":
                print("Te devuelve a otro planeta. Te encuentras con monstruos de otro planeta 'GAME OVER'") 
                     
            
         
            


        





    
