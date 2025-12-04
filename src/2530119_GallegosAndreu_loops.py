
#PORTADA

#NOMBRE: Andreu Alexandre Gallegos Martinez
#MATRICULA: 2530119
#GRUPO: IM 1-1

#Resumen Ejecutivo
"""
Un **bucle for** se usa para iterar sobre una secuencia (lista, tupla, cadena o rango).
Típicamente se usa para recorrer elementos y realizar una acción por cada uno.

Un **bucle while** se usa cuando el número de repeticiones es indeterminado y depende
de una condición lógica. Es natural usarlo para menús o lectura de datos con centinela.

Un **contador** es una variable que incrementa en un valor fijo (ej., +1) en cada ciclo.
Un **acumulador** es una variable que suma o acumula valores variables en cada ciclo.

Es crucial definir bien la condición de salida para evitar **ciclos infinitos**, lo cual
congelaría el programa. La condición debe volverse falsa en algún punto.

Este documento cubrirá: la descripción de cada problema, el diseño de entradas y salidas,
las validaciones, y el uso de 'for' para recorridos (ej., sumas) y 'while' para
situaciones de lectura repetida o menús de opciones.
"""

print(
    """
---------------------------
Sum of range with for
---------------------------
"""
)

"""
En este código se calcula la suma total de un rango de números (desde 1 hasta N) y la suma
de los números pares dentro de ese mismo rango, utilizando un bucle 'for'.
"""
"""
Inputs:
- n (int): El límite superior del rango (ej. para sumar de 1 a N).

Outputs:
- total_sum (int): La suma de todos los números desde 1 hasta N.
- even_sum (int): La suma de todos los números pares en el rango de 1 a N.
- Mensaje de Error: "Error: Number not valid, try again." si la entrada no es un entero.
- Mensaje de Error: "Error: invalid input" si N es menor que 1.

Validations:
- Verifica que la entrada 'n' sea un número entero.
- Verifica que 'n' sea mayor o igual a 1.
"""
"""
Test cases table:
| Test cases |   n     | Sum 1..n  | Sum of even numbers |
|   Normal   |    5    |     15    |         6          |
|   Border   |    1    |     1     |         0          |
|   error    |   "a"   |      Error: Number not valid        |

"""
try:
   n=int(input("Set your superior limit range: "))
except Exception as err:
    n="NO"

if n=="NO":
    print("Error: Number not valid, try again.")
else:
    if n>=1: 
        total_sum=0
        even_sum=0

        for i in range(1,n+1):
           total_sum += i
           if i % 2 == 0:
               even_sum += i

        print(f"Sum 1..n: {total_sum}")
        print(f"Sum of even numbers: {even_sum}")

    else:
        print("Error: invalid input")

print(
"""
-------------------
Multiplicator table with for
-------------------
"""
)

"""
En este código se imprime la tabla de multiplicar (base * i) desde 1 hasta un límite 'm'
utilizando un bucle 'for'.
"""
"""
Inputs:
- base (int): El número base de la tabla de multiplicar.
- m (int): El límite superior de las multiplicaciones.

Outputs:
- mult_num (int): El resultado de la multiplicación (base * i) para cada iteración.
- Impresión de la tabla en formato: "i x base = resultado".
- Mensaje de Error: "Error: Invalid input." si las entradas no son válidas.

Validations:
- Verifica que las entradas 'base' y 'm' sean números enteros.
- Verifica que 'm' sea al menos 1.
"""
"""
Test cases table:
| Test cases |   base  |   m   | Output Sample             |
|   Normal   |    5    |    3  | 1x5=5, 2x5=10, 3x5=15   |
|   Border   |    1    |    1  | 1x1=1                   |
|   error    |   "a"   |    5  |      Error: Invalid input    |

"""
try:
    base=int(input("Set your base multipication: "))
    m=int(input("Set your limit digit to the multiplications: "))

except Exception as err:
    m=-1
    base="NO"

if base=="NO" or m<1:
    print("Error: Invalid input.")

else:
    for i in range(1,m+1):
        mult_num=base*i
        print(f"{i} x {base} = {mult_num}")

print(
"""
------------------
Average of numbers with while and sentinel
------------------
"""
)

"""
En este código se calcula el promedio de una serie de números ingresados por el usuario
utilizando un bucle 'while', hasta que se ingresa un valor centinela (35.0) para detener el proceso.
"""
"""
Inputs:
- number (float): Números ingresados secuencialmente para el cálculo del promedio.
- sentinel_value (float): El valor que detiene el bucle (35.0).

Outputs:
- count (int): El número total de entradas válidas antes de la centinela.
- average_value (float): El promedio de los números ingresados.
- Mensaje de Error: "Error: None number entered" si la centinela es el primer valor.

Validations:
- Verifica que la entrada 'number' se pueda convertir a float.
- Maneja la división por cero si no se ingresaron números antes de la centinela.
"""
"""
Test cases table:
| Test cases |   Inputs        | count  | Average Output           |
|   Normal   | 10, 20, 30, 35 |    3    | Average 20.0             |
|   Border   |    35          |    0    | Error: None number entered|
|   error    |  "a", 10, 35   |    2    | Average 5.0 (si 'a' es 0.0)|

"""
number=None
sentinel_value=35.0
count=0
total_sum=0

while True:
    try:
        number=float(input("Set the number correct: "))
    except Exception as err:
        number=0.0


    if number == sentinel_value:
        if count == 0:
            average_value = 0.0
            print("Error: None number entered")
        else:
            average_value = total_sum/count

        print(f"Great job.")
        print(f"Count: {count}")
        print(f"Average {average_value}")
        break
    else:
        print("Sorry: Try again.")
        total_sum += number
        count+=1

    continue

print(
"""
-------------------------
Password attempts with while
-------------------------
"""
)

"""
En este código se simula un proceso de inicio de sesión que requiere una contraseña.
Utiliza un bucle 'while' para dar al usuario un número limitado de intentos.
"""
"""
Inputs:
- user_password (string): Contraseña ingresada por el usuario.
- password (string): La contraseña correcta ("2530119AG").

Outputs:
- Mensaje de Éxito: "Login Success. Welcome..." si la contraseña es correcta.
- Mensaje de Fracaso: "Account Locked" si se agotan los 5 intentos.
- Muestra los intentos restantes.

Validations:
- Compara la entrada del usuario con la contraseña definida.
- Limita los intentos a MAX_ATTEMPTS (5).
"""
"""
Test cases table:
| Test cases |   Inputs           | Outcome               |
| :--- | :--- | :--- |
|   Éxito    | Intentos fallidos, luego la correcta | Login Success. Welcome AndruxSM35.|
|   Fallo    | 5 contraseñas incorrectas | Account Locked |
|   Border   |      Correcta en el 5to intento   | Login Success. Welcome AndruxSM35.|

"""
user="AndruxSM35"
password="2530119AG"
MAX_ATTEMPTS=5
while True:
    user_password=input(f"Set the password for {user}: ")

    if user_password==password:
        print(f"Login Success. Welcome {user}.")
        break
    else:
        print("Try again.")
        MAX_ATTEMPTS-=1

    print(f"Attempts: {MAX_ATTEMPTS}")
    if MAX_ATTEMPTS==0:
        print("Account Locked")
        break
    continue
        
print(
"""
---------------
Simple menu with while
---------------
"""
)


"""
En este código se presenta un menú interactivo simple. Utiliza un bucle 'while' para
repetir las opciones hasta que el usuario selecciona la opción de Salir (0).
"""
"""
Inputs:
- option (int): Número de la opción seleccionada.
- yes_no (string): Confirmación de sí o no para salir.

Outputs:
- Ejecuta la opción seleccionada (muestra saludo, contador o incrementa contador).
- Mensaje de Salida: "BYE" al finalizar el programa.
- Mensaje de Error: "Error: Invalid option." o errores de opción inválida en el sub-menú.

Validations:
- Verifica que la 'option' sea un entero válido y exista en el diccionario 'menu'.
- Maneja opciones de sub-menú (YES/NO) de manera robusta.
"""
"""
Test cases table:
| Test cases |   Inputs                   | Outcome                                    |
| :--- | :--- | :--- |
|   Normal   |   3, 3, 2, NO, 0, YES      | Contador incrementa a 2, luego se sale.|
|   Error    |    "a"                   | Error: Invalid option.                  |
|   Cancelar |    0, NO                  | Vuelve al menú principal.                  |

"""

menu={ 1 : "Show Greeting",
       2 : "Show current counter value",
       3 : "Increment Counter",
       0 : "Exit"}

counter_value=0

while True:
    print(menu)
    print()
    try:
        option=int(input("Set the number where do you want to go: "))
        menu_op=menu[option]
    except Exception as err:
        option=-1
        menu_op="yo"


    if option==1 and menu_op!="yo":
        print(f"You selected {menu_op}")
        print("\nHello!")
        continue
    elif option==2 and menu_op!="yo":
        print(f"You selected {menu_op}")
        print(f"Counter: {counter_value}")

        while True:
            print("¿Exit?")
            yes_no=(input("[yes/no]: ")).upper()

            if yes_no=="YES":
                print("BYE")
                break
            elif yes_no=="NO":
                print("Cancelled")
                break
            else:
                print("Error: option not valid")
                continue
        continue
        
    elif option==3 and menu_op!="yo":
        print(f"You selected {menu_op}")
        counter_value +=1
        print(f"Counter incremented by {counter_value}")
        continue

    elif option==0 and menu_op!="yo":

        while True:
            print("¿Are you sure do you want to exit?")
            yes_no=(input("[yes/no]: ")).upper()

            if yes_no=="YES":
                print("BYE")
                break
            elif yes_no=="NO":
                print("Cancelled")
                break
            else:
                print("Error: option not valid")
                continue
            
        if yes_no=="YES":
            break
        else:
            continue

    else:
        print("Error: Invalid option.")
    continue

print(
"""
------------------
Patter printing with nested loops
------------------
"""
)

"""
En este código se imprime un patrón de asteriscos triangular, cuya altura está determinada por el número N
ingresado por el usuario. Utiliza un bucle 'for' para generar el patrón.
"""
"""
Inputs:
- n (int): El número de filas/altura del patrón.

Outputs:
- Impresión del patrón triangular.

Validations:
- Verifica que la entrada 'n' sea un número entero.
- Verifica que 'n' sea mayor que 1.
"""
"""
Test cases table:
| Test cases |   n   | Pattern Output (N=4)        |
| :--- | :--- | :--- |
|   Normal   |    4   | * / ** / *** / ****        |
|   Border   |    2   | * / **                   |
|   error    |    1   |   Error: Invalid Input.    |

"""
try:
    n=int(input("Set the number of asterisk: "))
except Exception as err:
    n=-1

if n<=1:
    print("Error: Invalid Input.")
else:
    asterisc="*"
    for i in range(1,n+1):
        print(asterisc*i) #Prints te text by multiplie with the actual range.
    print()

"""
La principal diferencia práctica es que **for** se usa cuando se conoce la cantidad de iteraciones
(ej., recorrer una lista o un rango), mientras que **while** se usa cuando la repetición es
incierta y depende de que una condición sea verdadera (ej., entrada de usuario válida).

Los **contadores** nos permitieron llevar un registro de eventos (ej., intentos de contraseña),
y los **acumuladores** fueron cruciales para sumar valores o calcular totales de manera eficiente.

El mayor riesgo al usar **while** es el **ciclo infinito**, que ocurre si la condición de salida
nunca se cumple, congelando el programa. Esto requiere un control estricto de la condición.

Los menús interactivos y los sistemas de intentos de contraseña son ejemplos perfectos de bucles
**while** porque la repetición se mantiene hasta que se alcanza un objetivo específico.

Aprendí que los **bucles anidados** son útiles para generar estructuras bidimensionales, como
tablas o patrones de texto, donde el bucle interno se ejecuta completamente por cada iteración del externo.
"""

"""
References:
1) Python documentation - Learning_about_strings.py
2) Python web - https://docs.python.org/es/3/using/cmdline.html
3) Curso completo de python desde cero - https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1s
4) Curso de python para principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo&t=775s
5) El tutorial de Python - https://docs.python.org/es/3/tutorial/
"""