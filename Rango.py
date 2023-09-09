# Solicitar al usuario la cantidad de datos a ingresar
num_datos = int(input("Ingrese la cantidad de datos: "))


min_valor = float('inf')  # Inicializado con infinito positivo
max_valor = float('-inf')  # Inicializado con infinito negativo

# Pedir al usuario que ingrese los datos uno por uno
for i in range(num_datos):
    dato = float(input(f"Ingrese el dato {i + 1}: "))

    if dato < min_valor:
        min_valor = dato
    if dato > max_valor:
        max_valor = dato
rango = max_valor - min_valor
print(f"El rango de los datos es: {rango}")
