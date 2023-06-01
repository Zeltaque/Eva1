#Evaluacion_Algoritmo

sw = 1


Cont_Entra = 0  


Acum_Total = 0  


Cont_Niño = 0  


Cont_Jov = 0  


Cont_Adul = 0  


Tot_Ganan= 0


while sw == 1:
    print("-------------------------------------------------------------------------")
    print("Bienvenido al Cine Moro")
    print("1. Comprar una Entrada")
    print("2. Ver Cantidad del Total de Entradas Vendidas y el Monto Recaudado")
    print("3. Ver Porcentaje de Entradas Vendidas")
    print("4. Salir")
    print("-------------------------------------------------------------------------")
    try:
        vOp = int(input("Seleccione una opción: "))
        if vOp == 1:
            print("CATEGORÍAS:")
            print("Niño [$5500] (1-13)")
            print("Joven [$7000] (14-21)")
            print("Adulto [$9000] (mayor a 22)")
            vCanti = int(input("Ingrese la cantidad de entradas: "))
            print("---------------------------------")
            print("CATEGORÍAS:")
            print("Niño [$5500] (1-13)")
            print("Joven [$7000] (14-21)")
            print("Adulto [$9000] (mayor a 22)")
            vEdad = int(input("ingresa tu edad: "))
            print("---------------------------------")
            print("CATEGORÍAS:")
            print("Niño [$5500] (1-13)")
            print("Joven [$7000] (14-21)")
            print("Adulto [$9000] (mayor a 22)")


            if vedad <= 13:
                Subtotal = vCanti * 5500
                Cont_Niño += vCanti
                print("categoria de entrada niño")
                print(f"cantidad de entradas {vCanti}")
                print(f"total a pagar = {subtotal}")


          
            elif vEdad >= 14 and vEdad <= 21:
                subtotal = vCanti * 7000
                Cont_Jov += vCanti
                print("categoria de entrada joven")
                print(f"cantidad de entradas {vCanti}")
                print(f"total a pagar = {subtotal}")


            elif vEdad <= 22:
                subtotal = vCanti * 9000
                Cont_Adul += vCanti
                print("categoria de entrada adulto")
                print(f"cantidad de entradas: {vCanti}")
                print(f"total a pagar = {subtotal}")


            Cont_Entra += vCanti
            Acum_Total += subtotal


        elif vOp == 2:
            print("---------------------------------")
            print("Total del día")
            print("---------------------------------")
            print("Cantidad de entradas vendidas:", Cont_Entra)
            print("Monto total recaudado: $", Acum_Total)


        elif vOp == 3:
            print("---------------------------------")
            print("Porcentaje del día")
            print("---------------------------------")
            print("Porcentaje de entradas por categoría:")
            total_entradas = Cont_Niño + Cont_Jov + Cont_Adul
            if total_entradas > 0:
                porcentaje_ni = (Cont_Niño / total_entradas) * 100
                porcentaje_joven = (Cont_Jov / total_entradas) * 100
                porcentaje_adulto = (Cont_Adul / total_entradas) * 100
                print("Niño:", porcentaje_ni, "%")
                print("Joven:", porcentaje_joven, "%")
                print("Adulto:", porcentaje_adulto, "%")
            else:
                print("No se han vendido entradas aún.")


        elif vOp == 4:
            sw = 0 


            
        else:
            print("Opción inválida")


    except ValueError:
        print("Opción inválida")


print("Gracias por su compra, disfrute la función.")