# PROGRAMA PARA VERIFICAR CUÁL DE DOS NÚMEROS ENTEROS ES EL MAYOR 

print("--------------------------------")
print("------ INGRESE UN NUMERO -------")
print("--------------------------------")

#input
x = int(input("INGRESE EL VALOR DE X: "))
y = int(input("INGRESE EL VALOR DE Y: "))

#processing

if x == y: 
    # output
    print("LOS NÚMEROS SON IGUALES...")
else:
    if x > y:
        mayor = x
    else:
        mayor = y 
        # output
    print("EL MAYOR ENTRE: " + str(x) + " y " + str(y) + " ES= " + str(mayor))