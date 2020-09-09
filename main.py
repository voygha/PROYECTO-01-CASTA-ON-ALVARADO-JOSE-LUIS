from lifestore_file import lifestore_products,lifestore_sales, lifestore_searches


usuarios_admin = [["Luis","123"],["Javier", "hola"]]

usuario_digitado= input("Ingresa el usuario: ")
contra_digitado= input("Ingresa la contraseña: ")

admin= 0

for usuario in usuarios_admin:
    if usuario[0] == usuario_digitado and usuario[1] == contra_digitado:
        #print("Hola bienvenido")
        admin = 1
        break
    else:
        continue
if admin == 1:
    ciclo=1
    while ciclo == 1:
        print("Bienvenido a LifeStore")
        print("\n\n")
        print("¿Qué desea hacer?")
        print("(1) Ver los Productos más vendidos")
        print("(2) Ver los productos rezagados")
        print("(3) Ver los Productos con Mayor busqueda")
        print("(4) Ver los Productos con Menor busqueda")
        print("(5) Productos por reseña en el servicio")
        print("(6) Total de ingresos y ventas promedio mensuales")
        print("(7) Total anual y meses con más ventas al año")
        opcion= int(input("Digite una Opción: "))

        #-------------------------------------------------------------------------------------------------------------------
        #SACAR LOS PRODUCTOS MAS Y MENOS VENDIDOS
        """
        La variable apoyo la uso para almacenar todos los id de los productos aunque esten repetidos
        #print (apoyo)
        """
        apoyo=[]
        n=0
        while n < len(lifestore_sales):
            apoyo.append(lifestore_sales[n][1])
            n+=1
        #La variable prueba es una lista que uso para contar cuantas veces se repite el id de un producto 
        prueba=[]
        #la variable a es un indice para ir recorriendo la lista y captura el id del producto
        a=0
        control= 0

        #PRIMERO IMPRIME EL ID DEL PRODUCTO Y LUEGO EL NUMERO DE VECES QUE SE REPITE
        mayor=apoyo.count(a)
        #mayor es una variable que guarda el numero que más se repite
        #CALCULA CUANTAS VECES FUERON VENDIDOS LOS PRODUCTOS 
        while a < len(lifestore_products):
            #Aqui la a presenta el id del producto y el numero de veces que se repite en la lista llamada apoyo 
            prueba.append(["Código del Producto: ",a,"Numero de ventas del producto:",apoyo.count(a)])
            #idpro.append(a)
            if mayor <= apoyo.count(a):
                mayor= a
                control=apoyo.count(a)
            a+=1
            
        #FIN DE LA "FUNCION" QUE SACA LOS PRODUCTOS MAS Y MENOS VENDIDOS
        #-------------------------------------------------------------------------------------------------------------------
        

        #________________________________________________________________________________________________________________________
        if opcion == 1:
            #ESTE FOR IMPRIME LOS 30 PRODUCTOS MÁS VENDIDOS
            #disminuye es una variable que toma el valor de mayor, se declaro porque se va modificando la variable
            disminuye= mayor
            veces=0
            print("\n Los 30 Productos más vendidos son: \n\n")
            print(prueba[mayor],lifestore_products[mayor][1])

            for productos in prueba:
                for x in prueba:
                    if disminuye == prueba[veces][1]  and veces < 30:
                        #rint("Vamos bien")
                        print(prueba[veces],lifestore_products[veces][1])
                    veces+=1
                veces=0
                disminuye-=1
            
        #__________________________________________________________________________________________________________________________

        if opcion ==2:
            #ESTE FOR IMPRIME LOS PRODUCTOS QUE MENOS SE VENDIERON
            print("\n\n Los Productos que menos se vendieron son: \n\n")
            veces=0
            disminuye= mayor
            for productos in prueba:
                for x in prueba:
                    if disminuye == prueba[veces][1]  and veces > 30:
                        #rint("Vamos bien")
                        print(prueba[veces],lifestore_products[veces][1])
                    veces+=1
                veces=0
                disminuye-=1
        
        #__________________________________________________________________________________________________________________________
        """
        LO QUE SE HACE ABAJO ES EL CALCULO DE LOS PRODUCTOS MÁS Y MENOS BUSCADOS Y YA SOLO SE MANDA A LLAMAR A LA 
        LISTA QUE CORRESPONDE LA OPCION QUE SE ELIJA
        """
        #AQUI CONTAMOS CUANTAS VECES SE BUSCO EL ID DE CADA PRODUCTO
        contador=0
        busquedas_totales=[]
        mayor=0
        indice=0
        for producto in lifestore_products:
            contador=0
            for buscar in lifestore_searches:
                if producto[0] == buscar[1]:
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contador+=1
            formato= [producto[0], contador]
            busquedas_totales.append(formato)
            #AQUI DETERMINAMOS CUAL ES EL MAYOR Y LISTO
            if mayor <= contador:
                mayor=contador
                indice= producto[0]
        #SE IMPRIME  LA LISTA DE TODOS LOS PRODUCTOS ORDENADOS POR ID Y CONTANDO LAS VECES QUE SE REPITE




        #SE CREA LA VARIA DE CONTROL QUE SERVIRA PARA DISMINUIR EN CADA ITERACIÓN
        controlador=mayor-1
        mayores_busquedas=[]
        menores_busquedas=[]
        #SE GUARDA EL PRODUCTO MÁS BUSCADO
        mayores_busquedas.append(["El producto más buscado es: ", indice, lifestore_products[indice-1][1], "Se busco un total de: ",mayor,"veces"])
        b=0
        veces=0
        while b < mayor-1: 
            a=0
            while a < len(busquedas_totales): 
                if busquedas_totales[a][1] == controlador:
                    veces+=1
                    if veces <= 30:
                        mayores_busquedas.append(["El producto: ", a+1, lifestore_products[a][1], "Se busco un total de: ",controlador, "veces"])
                    if veces > 30:
                        menores_busquedas.append(["El producto: ", a+1, lifestore_products[a][1], "Se busco un total de: ",controlador, "veces"])
                a+=1
            b+=1
            controlador=controlador-1  
        #__________________________________________________________________________________________________________________________
        if opcion==3:
            
            #IMPRIME LA LISTA DE PRODUCTOS MÁS Y MENOS BUSCADOS
            print("\n\n Los productos más buscados son: \n\n")
            for index in range(0,len(mayores_busquedas)):
                print(mayores_busquedas[index])
        #__________________________________________________________________________________________________________________________
        if opcion==4:
            print("\n\n Los productos menos buscados son: \n\n")
            for index in range(0,len(menores_busquedas)):
                print(menores_busquedas[index])
        #__________________________________________________________________________________________________________________________
        
        if opcion==5:
            #AQUI CONTAMOS CUANTAS VECES SE BUSCO EL ID DE CADA PRODUCTO
            contador=0
            resenas_totales=[]
            mayor=0
            indice=0
            veces=0

            for producto in lifestore_products:
                contador=0
                calificacion=0
                for resena in lifestore_sales:
                    if producto[0] == resena[1]:
                        #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                        calificacion+= resena[2]
                        veces+=1
                #AQUI SACAMOS EL PROMEDIO DE LA RESEÑA DE CADA PRODUCTO
                calificacion= int(calificacion/veces)
                #calificacion= calificacion/veces
                formato= [producto[0], calificacion]
                resenas_totales.append(formato)
                
                #AQUI DETERMINAMOS CUAL ES EL MAYOR Y LISTO
                if mayor <= calificacion:
                    mayor=calificacion
                    indice= producto[0]
                
            #SE IMPRIME  LA LISTA DE TODOS LOS PRODUCTOS ORDENADOS POR ID Y CONTANDO LAS VECES QUE SE REPITE
            
            #print(len(resenas_totales)) SON 96 PRODUCTOS


            #SE CREA LA VARIA DE CONTROL QUE SERVIRA PARA DISMINUIR EN CADA ITERACIÓN
            controlador=mayor
            mayores_re=[]
            menores_re=[]
            #SE GUARDA EL PRODUCTO MÁS BUSCADO
            mayores_re.append(["El producto con mejor reseña es: ", indice, lifestore_products[indice-1][1], "Tiene una calificación de: ",mayor,"Puntos"])
            b=0
            veces=0
            while b < mayor: 
                a=0
                while a < len(resenas_totales): 
                    if resenas_totales[a][1] == controlador:
                        veces+=1
                        if veces <= 10:
                            mayores_re.append(["El producto: ", a+1, lifestore_products[a][1], "Tiene una calificación de: : ",controlador, "Puntos"])
                        if veces > 10:
                            menores_re.append(["El producto: ", a+1, lifestore_products[a][1], "Tiene una calificación de: ",controlador, "Puntos"])
                    if controlador == 0:
                        menores_re.append(["El producto: ", a+1, lifestore_products[a][1], "Tiene una calificación de: ",controlador, "Puntos"])
                    a+=1

                b+=1
                if controlador > 0:
                    controlador=controlador-1 
                
            print("\n\n Los productos con mas puntos en reseñas son: \n\n")
            for index in range(0,len(mayores_re)):
                print(mayores_re[index])
            """
            POR ALGUNA EXTRAÑA NO ME IMPRIME NADA EN RESEÑAS CON MENOS PUNTOS, PORQUE SON 0 PUNTOS Y NO LO GUARDA EN EL ARREGLO
            PORQUE COMPARA Y PREGUNTA ALGO COMO, SI 0 ES IGUAL A 0
            HAS ESTO, PERO NO LO HACE"""
            print("\n\n Los productos con menos puntos son: \n\n")
            for index in range(0,len(menores_re)):
                print(menores_re[index])
        
        #__________________________________________________________________________________________________________________________
        #AQUI CONTAMOS CUANTAS VECES SE BUSCO EL ID DE CADA PRODUCTO
        contadorglobal=0
        contadorene=0
        contadorfeb=0
        contadormar=0
        contadorabril=0
        contadormay=0
        contadorjun=0
        contadorjul=0
        contadoragos=0
        resenas_totales=[]
        mayor=0
        indice=0
        veces=0
        fecha=[]
        enero=[]
        febrero=[]
        marzo=[]
        abril=[]
        mayo=[]
        junio=[]
        julio=[] 
        agosto=[]
        ventasanuales=[]
        for producto in lifestore_products:
            contadorglobal=0
            #calificacion=0
            for fecha1 in lifestore_sales:
                if producto[0] == fecha1[1]:
                    contadorglobal+=1
                #ENERO
                if producto[0] == fecha1[1] and fecha1[3][3:5] == "01" :
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contadorene+=1
                    veces+=1
                #FEBRERO
                if producto[0] == fecha1[1] and fecha1[3][3:5] == "02" :
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contadorfeb+=1
                    veces+=1
                #MARZO
                if producto[0] == fecha1[1] and fecha1[3][3:5] == "03" :
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contadormar+=1
                    veces+=1
                #ABRIL
                if producto[0] == fecha1[1] and fecha1[3][3:5] == "04" :
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contadorabril+=1
                    veces+=1
                #MAYO
                if producto[0] == fecha1[1] and fecha1[3][3:5] == "05" :
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contadormay+=1
                    veces+=1
                #JUNIO
                if producto[0] == fecha1[1] and fecha1[3][3:5] == "06" :
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contadorjun+=1
                    veces+=1
                #JULIO
                if producto[0] == fecha1[1] and fecha1[3][3:5] == "07" :
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contadorjul+=1
                    veces+=1
                #AGOSTO
                if producto[0] == fecha1[1] and fecha1[3][3:5] == "08" :
                    #AQUI CONTAMOS CUAL ES EL NUMERO DE VECES QUE SE BUSCO CADA PRODUCTO
                    contadoragos+=1
                    veces+=1
            promedio=0
            promedio= contadorglobal/365 
            formatoanual=["El Producto ",producto[0],"Se vendio en el Año",contadorglobal,"Veces","Su promedio de ventas por dia es: ", round(promedio,2)]
            ventasanuales.append(formatoanual)

            promedio=0
            promedio= contadorene/30    
            formato_fechaene=["El Producto ",producto[0],"Se vendio en el mes de Enero",contadorene,"Veces en el mes","Su promedio de ventas por dia es: ", round(promedio,2)]
            enero.append(formato_fechaene)

            promedio=0
            promedio= contadorfeb/30
            formato_fechafeb=["El producto ",producto[0],"Se vendio en el mes de Febrero",contadorfeb,"Veces en el mes","Su promedio de ventas por dia es: ", round(promedio,2)]
            febrero.append(formato_fechafeb)

            promedio=0
            promedio= contadormar/30
            formato_fechamar=["El producto ",producto[0],"Se vendio en el mes de Marzo",contadormar,"Veces en el mes","Su promedio de ventas por dia es: ", round(promedio,2)]
            marzo.append(formato_fechamar)

            promedio=0
            promedio= contadorabril/30
            formato_fechaaabril=["El Producto ",producto[0],"Se vendio en el mes de Abril",contadorabril,"Veces en el mes","Su promedio de ventas por dia es: ", round(promedio,2)]
            abril.append(formato_fechaaabril)

            promedio=0
            promedio= contadormay/30
            formato_fechamay=["El Producto",producto[0],"Se vendio en el mes de Mayo",contadormay,"Veces en el mes","Su promedio de ventas por dia es: ", round(promedio,2)]
            mayo.append(formato_fechamay)

            promedio=0
            promedio= contadorjun/30
            formato_fechajun=["El Producto",producto[0],"Se vendio en el mes de Junio",contadorjun,"Veces en el mes","Su promedio de ventas por dia es: ", round(promedio,2)]
            junio.append(formato_fechajun)

            promedio=0
            promedio= contadorjul/30
            formato_fechajul=["El Producto ", producto[0],"Se vendio en el mes de ","Julio",contadorjul,"Veces en el mes","Su promedio de ventas por dia es: ", round(promedio,2)]
            julio.append(formato_fechajul)

            promedio=0
            promedio= contadoragos/30
            formato_fechaagos=["El Producto ",producto[0],"Se vendio en el mes de Agosto",contadoragos,"Veces en el mes","Su promedio de ventas por dia es: ", round(promedio,2)]
            agosto.append(formato_fechaagos)
        if opcion==6:
            print("\n\nVentas Mensuales\n\n")
            print("\n\nVentas Totales en Enero:\n\n")
            for index in range(0,len(enero)):
                print(enero[index])
            print("\n\nVentas Totales en Febrero:\n\n")
            for index in range(0,len(febrero)):
                print(febrero[index])
            print("\n\nVentas Totales en Marzo:\n\n")
            for index in range(0,len(marzo)):
                print(marzo[index])
            print("\n\nVentas Totales en Abril:\n\n")
            for index in range(0,len(abril)):
                print(abril[index])
            print("\n\nVentas Totales en Mayo:\n\n")
            for index in range(0,len(mayo)):
                print(mayo[index])
            print("\n\nVentas Totales en Junio:\n\n")
            for index in range(0,len(junio)):
                print(junio[index])
            print("\n\nVentas Totales en Julio:\n\n")
            for index in range(0,len(julio)):
                print(julio[index])
            #print(mayor)
            print("\n\nVentas Totales en Agosto\n\n")
            for index in range(0,len(agosto)):
                print(agosto[index])
        if opcion==7:
            print("\n\n\n\n")
            print("Las ventas por año son:\n\n ")
            for index in range(0,len(ventasanuales)):
                print(ventasanuales[index])






        ciclo= int(input("\n\nHola ¿Deseas volver a Comenzar?\n\n(1) Sí\n\n(2)no\n\n"))

if admin == 0:
    print("El usuario o contraseñas son incorrectas")


#print(lifestore_searches)