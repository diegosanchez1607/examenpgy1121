
entradas=[False,False,False,False,False,False,False,False,False,False,
          False,False,False,True,True,True,False,False,False,False,
          False,False,True,False,False,False,False,False,False,False,
          False,False,False,False,True,False,False,False,False,False,
          False,False,False,False,False,False,False,False,False,False,
          False,False,False,False,False,False,False,False,False,False,
          False,False,False,False,False,False,False,False,False,False,
          False,False,False,False,False,False,False,False,False,False,
          False,False,False,False,False,False,False,False,False,False,
          False,False,False,False,False,False,False,False,False,False,]
asistentes=[1,2,3,4,5,6,7,8,9,]
rut=[]
ingresos=[0]
reservas=[]





def comprar_entradas(entradas,reservas):
    
    print("""
    los precios de las entradas pueden variar dependiendo del lugar
      * platinum, $120000 (1 al 20)
      * Gold, $80000 (21 al 50)
      * silver $50000(51 al 100).
    """)

    for i in range(len(entradas)):
            if entradas[i]:
                print(f"asiento ocupados {i+1}")
    asiento= int(input("ingrese el numero de asiento que quiere comprar"))
    if entradas[asiento]:
          entradas[asiento] = True
          print("reserva de entrada exitosa")
    else:
          print("este asiento esta reservado eliga otro o no existe")










def asistentes_disponibles(asistentes):
     for i in range(len(asistentes)):
      print("ver asistences  diponibles")
      print(f"asistente {0+1} fila 1(1,10)")
      print(f"asistente {1+1} fila 2(11,20)")
      print(f"asistente {2+1} fila 3(21,30)")
      print(f"asistente {3+1} fila 4(41,50)")
      print(f"asistente {4+1} fila 5(51,60)")
      print(f"asistente {5+1} fila 6(61,70)")
      print(f"asistente {6+1} fila (71,80)")
      print(f"asistente {7+1} fila 8(81,90)")
      print(f"asistente {8+1} fila 9(91,100)")


def mostrar_ubicaciones_disponibes(entradas):

      
      for i in range(len(entradas)):
            if entradas[i] == True:
             estado="reservada"
            

            else:
                  estado ="disponible"
                  print(f"asiento{i+1}:{estado}")
                
      
              




     





         
         

while True:
        
        print("""

        1. comprar entradas
        2. mostrar ubicaciones disponible
        3. ver listados de asistentes
        4. mostrar ganancias totales
        5. salir

        """)

        opcion=input("eliga una opcion :  ")
        match opcion:
             
            case "1":
                  comprar_entradas(entradas,reservas)
            case "2":
                  mostrar_ubicaciones_disponibes(entradas)
            case "3":
                  asistentes_disponibles(asistentes)
                  
            case "4":
                  pass
                  
            case "5":
                break
            case other:
                  print("opcion no valida")
