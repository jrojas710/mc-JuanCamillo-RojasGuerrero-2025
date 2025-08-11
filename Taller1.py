import random

# Juan Rojas: Se crea la funcion para generar un conjunto aleatorio con cardinalidad indicada

def generar_conjunto(cardinalidad):
    
    # Juan Rojas: Se crea un conjunto vacio

    conjunto = set()
    
    # Juan Rojas: Se crea un "mientras" el conjunto no tenga la cardinalidad indicada

    while len(conjunto) < cardinalidad:
        
        # Juan Rojas: Se agrega un numero aleatorio entre 0 y 30

        conjunto.add(random.randint(0, 30))
    
    # Juan Rojas: Se retoma el conjunto que recientemente se creo

    return conjunto


# Juan Rojas: Se crea una funcion para calcular la union de los conjuntos

def union(a, b):
    
    # Juan Rojas: Se crea un conjunto vacio para guardar el resultado

    c = set()
    
    # Juan Rojas: Se agregan todos los elementos del conjunto a

    for elemento in a:

        c.add(elemento)
    
    # Juan Rojas: Se agregan todos los elementos del conjunto b

    for elemento in b:

        c.add(elemento)
    
    # Juan Rojas: Se retoma el conjunto c o el conjunto resultante

    return c


# Juan Rojas: Se crea una funcion para calcular la interseccion de los conjuntos

def interseccion(a, b):
    
    # Juan Rojas: Se crea un conjunto vacio para almacenar el resultado

    c = set()
    
    # Juan Rojas: Se recorre cada elemento de a para poder usar sus datos del interior

    for elemento in a:
        
        # Juan Rojas: Si el elemento esta en b, se agrega al conjunto resultante o c

        if elemento in b:

            c.add(elemento)
    
    # Juan Rojas: Se retorna al conjunto resultante o c

    return c


# Juan Rojas: Se crea la funcion para calcular la diferencia A - B

def diferencia(a, b):
    
    # Juan Rojas: Se crea un conjunto vacio para c

    c = set()
    
    # Juan Rojas: Se recorre cada elemento de a para poder usar sus datos del interior

    for elemento in a:
        
        # Juan Rojas: Si el elemento no esta en b, se agrega

        if elemento not in b:

            c.add(elemento)
    
    # Juan Rojas: Se retorna el conjunto resultante o c

    return c


# Juan Rojas: Se crea la funcion para calcular la diferencia simetrica entre A y B

def diferencia_simetrica(a, b):
    
    # Juan Rojas: Se crea un conjutno vacio para el resultado

    c = set()
    
    # Juan Rojas: Se recorren todos los elementos de a para poder usar sus datos del interior

    for elemento in a:
        
        # Juan Rojas: Si el elemento no esta en b, se agrega

        if elemento not in b:

            c.add(elemento)
    
    # Juan Rojas: Se recorren todos los elementos de b para poder usar sus datos del interior

    for elemento in b:
        
        # Juan Rojas: Si el elemento no esta en a, se agrega

        if elemento not in a:

            c.add(elemento)
    
    # Juan Rojas: Se retorna el conjunto resultante

    return c


# Juan Rojas: Se pide al usuario la cardinalidad de A con control de error

while True:

    try:

        n_a = int(input("Ingrese la cardinalidad del conjunto A: "))

        break

    except ValueError:

        print("Por favor ingrese un número valido (no letras ni simbolos)")

# Juan Rojas: Se pide al usuario la cardinalidad de B con control de error

while True:

    try:

        n_b = int(input("Ingrese la cardinalidad del conjunto B: "))

        break

    except ValueError:

        print("Por favor, ingrese un número valido (no letras ni simbolos)")

# Juan Rojas: Se generan los conjuntos

A = generar_conjunto(n_a)

B = generar_conjunto(n_b)

# Juan Rojas: Se imprimen los conjuntos

print("Conjunto A:", A)

print("Conjunto B:", B)

# Juan Rojas: Se calcula y se imprime cada operacion

print("A ∪ B:", union(A, B))

print("A ∩ B:", interseccion(A, B))

print("A - B:", diferencia(A, B))

print("B - A:", diferencia(B, A))

print("A Δ B:", diferencia_simetrica(A, B))
