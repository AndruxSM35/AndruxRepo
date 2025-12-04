#PORTADA

#NOMBRE: Andreu Alexandre Gallegos Martinez
#MATRICULA: 2530119
#GRUPO: IM 1-1

#Resumen Ejecutivo

"""
Una función en Python es un bloque de código reusable que realiza una tarea específica. Sirve para
organizar el código, hacerlo más legible y evitar repeticiones (principio DRY).

La diferencia clave: los 'parámetros' son los nombres de las variables que se definen en la
cabecera de la función (definition). Los 'argumentos' son los valores concretos que se
le pasan a la función cuando esta es invocada (call).

Es útil separar la lógica en funciones reutilizables porque facilita el mantenimiento, la
depuración y permite construir programas complejos a partir de piezas modulares simples.

Un valor de retorno es el resultado que la función entrega al código que la llamó, usando 'return'.
Es mejor devolver resultados en lugar de solo imprimirlos para que el valor pueda ser usado
o procesado por otras partes del programa (flexibilidad y modularidad).

Este documento cubrirá: la descripción de cada problema a resolver, el diseño detallado de
funciones, las entradas esperadas, las salidas generadas, las validaciones necesarias y
las pruebas básicas para verificar su correcto funcionamiento.
"""

print(
"""
-------------------
Rectangle area and perimeter (basic functions)
-------------------
"""
)

"""
En este código se calculan el área y el perímetro de un rectángulo.
Las dimensiones (ancho y alto) son solicitadas al usuario.
"""
"""
Inputs:
- width (float): El ancho del rectángulo ingresado por el usuario.
- height (float): La altura del rectángulo ingresada por el usuario.

Outputs:
- area_value (float): El resultado del cálculo del área (width * height).
- perimeter_value (float): El resultado del cálculo del perímetro (2 * (width + height)).
- Mensaje de Error: "Error: Invalid input" si las dimensiones no son números positivos.

Validations:
- Verifica que las entradas 'width' y 'height' se puedan convertir a float (si no, asigna -1.0 a ambos).
- Verifica que 'width' y 'height' sean mayores que 0.
"""
"""
Test cases table:
| Test cases |  width | height | area_value | perimeter_value |
|  Normal  |  10.0  | 5.0  |  50.0   |   30.0    |
|  Border  |  0.1  | 1.0  |  0.1   |   2.2     |
|  error  |  "a"   |    Error: Invalid input     |

"""
def calculate_area(width,height):
    area_value=width*height
    return area_value

def calculate_perimeter(width,height):
    perimeter=2 * (width + height)
    return perimeter
try:
    width=float(input("Set your width of the triangle: "))
    height=float(input("Set the height of the triangle: "))

except Exception as err:
    width=-1.0
    height=-1.0 

if not(width>0 and height>0):
    print("Error: Invalid input")
else:
    area_value=calculate_area(
        width=width,
        height=height
    )

    perimeter_value=calculate_perimeter(
        width=width,
        height=height
    )

    print(f"Area: {area_value}")
    print(f"Perimeter: {perimeter_value}")

print(
"""
------------------
Grade Classifier (function with return string)
------------------
"""
)

"""
En este código se clasifica una puntuación (score) numérica dentro de un nivel de calificación (grado)
según rangos predefinidos (A, B, C, D, F).
"""
"""
Inputs:
- score (float): La puntuación numérica (0-100) ingresada por el usuario.

Outputs:
- grade_level (string): Un string que indica el puntaje y el nivel de calificación asociado.
    Ejemplo: "The score of 95.0: A"
- Mensaje de Error: "Error: Invalid input." si la puntuación no es válida.

Validations:
- Verifica que la entrada 'score' se pueda convertir a float (si no, asigna -1).
- Verifica que 'score' esté en un rango válido (mayor a 0 y menor o igual a 100).
"""
"""
Test cases table:
| Test cases |  score  | grade_level          |
|  A    |  95.0  | The score of 95.0: A     |
|  C    |  75.0  | The score of 75.0: C     |
|  F    |  20.0  | The score of 20.0: F     |
|  error  |  "x"   |    Error: Invalid input.  |

"""
def classify_grade(score):
    if score>=90:
        grade_level=f"The score of {score}: A"
    elif score >=80 and score <90:
        grade_level=f"The score of {score}: B"
    elif score >=70 and score <80:
        grade_level=f"The score of {score}: C"
    elif score>=60 and score <70:
        grade_level=f"The score of {score}: D"
    else:
        grade_level=f"The score of {score}: F"
    return grade_level

try:
    score=float(input("Set your grade to classify: "))
except Exception as err:
    score=-1

if score <= 0 or score > 100: 
    print("Error: Invalid input.")
else:
    grade_score=classify_grade(
    score=score
    )
    print(grade_score)

print(
"""
-----------------
List Statistics function (min, max,average)
-----------------
"""
)

"""
En este código se calcula el valor mínimo, máximo y el promedio de una lista de números.
La entrada es una cadena de números separados por comas que se convierte en una lista de floats.
"""
"""
Inputs:
- num_text (string): Una cadena de texto de números separados por comas ingresada por el usuario (ej. "10, 20.5, 5").

Outputs:
- dicc_num (dictionary): Un diccionario con las claves "MIN", "MAX" y "Average" de los números válidos.
- Mensaje de Error: "Error: number not valid" si la entrada está vacía.
- Mensaje de Error: "Error: Invalid input" si algún elemento en la entrada no es un número.

Validations:
- Verifica que la cadena de entrada 'num_text' no esté vacía.
- Intenta convertir cada elemento separado por coma a float.
- Si la conversión falla para cualquier elemento, se establece 'true_false=0' y se muestra "Error: Invalid input".
"""
"""
Test cases table:
| Test cases |  num_text    | Outputs                        |
|  Normal  |  "1,5,10"    | {'MIN': 1.0, 'MAX': 10.0, 'Average': 5.333333333333333} |
|  Vacio  |   ""      |  Error: number not valid              |
|  error  |  "1,a,10"    |  Error: Invalid input                |

"""
def summarize_numbers(list_num):

    min_num=min(list_num)
    max_num=max(list_num)
    leng_num=len(list_num)

    average_val=(sum(list_num)/leng_num)

    dicc_num={"MIN":min_num,
              "MAX":max_num,
              "Average":average_val}
    return dicc_num


num_text=input("Set your numbers: ").strip()


if num_text=="":
    print("Error: number not valid")
else:
    num_text_array=num_text.split(",")

    num_list_text=[]
    true_false=1 

    for num in num_text_array:
        try:
            num_conv=float(num.strip())
            num_list_text.append(num_conv)
        except Exception as err:
            true_false=0
            break
    if true_false==0:
        print("Error: Invalid input")
    else:
        dicc_num=summarize_numbers(
        list_num=num_list_text
        )
        print(dicc_num)

    

print(
    """
-----------------------
Apply discount list(pure function)
-----------------------
    """
)
    

"""
En este código se aplica una tasa de descuento a una lista de precios, devolviendo una nueva lista.
Se valida la tasa de descuento y los precios.
"""
"""
Inputs:
- prices_text (string): Una cadena de precios separados por comas (ej. "100.0, 200.0").
- discount_rate (float): La tasa de descuento (float entre 0 y 1).

Outputs:
- original_list (list): La lista de precios originales válidos (flotantes).
- discounted_list (list): La lista de precios con el descuento aplicado.
- Mensaje de Error: "Error: Data not valid" si 'prices_text' está vacío o si la lista final es vacía.
- Mensaje de Error: "Error: Invalid input" si la tasa de descuento no está entre 0 y 1, o si un precio no es un número positivo.

Validations:
- Verifica que la entrada de precios no esté vacía.
- Verifica que 'discount_rate' sea float y esté entre 0 y 1 (inclusive).
- Verifica que cada precio en la lista sea un número positivo (> 0).
"""
"""
Test cases table:
| Test cases |  prices_text  | discount_rate | discounted_list Output        |
|  Normal  |  "100,200"   |   0.1    | Original: [100.0, 200.0], Discounted: [90.0, 180.0] |
|  Border  | "10"     |   0.0    | Original: [10.0], Discounted: [10.0]      |
|  error  |  ""    |   0.1    |   Error: Data not valid           |
|  error |  "10, -5"   |   0.1    |   Error: Invalid input            |

"""

def apply_discount(prices_list,discount_rate):
    discounted_list=[]
    for price in prices_list:

        discounted_price=price*(1 - discount_rate)
        discounted_list.append(discounted_price)

    return discounted_list 
    
prices_text=input("Set your prices: ").strip()

try:
    discount_rate=float(input("Set your discount rate: "))
except Exception as err:
    discount_rate=-1

if prices_text=="":
    print("Error: Data not valid")
else:
    if not(discount_rate>=0 and discount_rate<=1):
        print("Error: Invalid input")
    else:
        price_text_array=prices_text.split(",")
        original_list=[]
        valid_input = True

        for price in price_text_array:
            try:
                price_num=float(price.strip())
            except Exception as err:
                price=num=-1 

            if price_num>0:
                original_list.append(price_num)
            else:
                valid_input=False
                break
        if not valid_input:
            print("Error: Invalid input")
        elif not original_list:
            print("Error: Data not valid")
        else:
            discounted_list=apply_discount(
            prices_list=original_list,
            discount_rate=discount_rate
            )

            print(f"Original prices: {original_list}")
            print(f"Discounted prices: {discounted_list}")

        
print(
"""
-----------------
Greeting function with default parametrers
-----------------
"""
)

"""
En este código se construye un saludo completo utilizando un nombre y un título opcional.
La función utiliza parámetros predeterminados para el nombre y el título.
"""
"""
Inputs:
- name (string): El nombre de la persona (se convierte a mayúsculas la primera letra de cada palabra y se eliminan espacios).
- title (string): El título opcional de la persona (se convierte a mayúsculas la primera letra de cada palabra y se eliminan espacios).

Outputs:
- full_name (string): El saludo completo en formato "Título Nombre". Ejemplo: "Mr Name".
- Mensaje de Error: "Error: You must send a name:" si el nombre ingresado está vacío.

Validations:
- Verifica que el 'name' (después de limpiar y convertir a minúsculas) no esté vacío.
"""
"""
Test cases table:
| Test cases |  name   | title   | full_name Output     |
|  Ambos  | "john"  | "mr"   | Hello: Mr John      |
|  Solo Name|  "doe"  |  ""    | Hello: Doe        |
|  error  |    ""   | "dr"   | Error: You must send a name: |

"""
def greet(name="",title=""):
    full_name=f"{title.title()} {name.title()}"
    return full_name

name=input("Set your name: ").lower().strip()
title=input("Set your title: ").lower().strip()

if name=="":
    print("Error: You must send a name: ")
else:
    full_name=greet(
        name,
        title
    )
    print(f"Hello: {full_name}")

print(
"""
-------------------
Factorial function (iterative or recursive)
-------------------
"""
)

"""
En este código se calcula el factorial de un número entero no negativo (n!) de forma iterativa.
"""
"""
Inputs:
- n (int): El número entero para el cual se calculará el factorial (n!).

Outputs:
- factorial_value (int): El resultado del cálculo factorial.
- Mensaje de Error: "Error: Invalid input" si la entrada no es un entero, es negativa o es mayor a 20.

Validations:
- Verifica que la entrada 'n' se pueda convertir a entero (si no, asigna -1).
- Verifica que 'n' esté en el rango válido para el cálculo (0 <= n <= 20).
"""
"""
Test cases table:
| Test cases |  n  | Factorial Output |
|  Normal  |  5  | Factorial=120   |
|  Border  |  0  | Factorial=1    |
|  error  |  -1  |  Error: Invalid input |
|  error  |  "b" |  Error: Invalid input |

"""
def factorial(n):
    factorial_value=1
    for i in range(1,n+1):
        factorial_value*=i
    return factorial_value
    
try:
    n=int(input("Set your number to be your n!: "))
except Exception as err:
    n=-1
if not(n>=0 and n<=20):
    print("Error: Invalid input")
else:
    print(f"n={n}")

    factorial_value=factorial(
        n=n
    )
    print(f"Factorial={factorial_value}")

"""
Las funciones son esenciales para la organización, permitiendo la reutilización del código
y siguiendo el principio DRY (Don't Repeat Yourself), lo cual reduce la complejidad general.

Devolver valores con 'return' es superior a solo imprimir, ya que el valor retornado puede
ser usado, modificado o pasado como argumento a otras funciones, haciendo el código modular.

El uso de parámetros y valores por defecto confiere gran flexibilidad al código,
permitiendo que una misma función se adapte a distintos contextos sin ser reescrita.

En lo personal, encapsular lógica en funciones resultó ser más cómodo para tareas repetitivas
como cálculos matemáticos o validaciones de entrada complejas, simplificando el script principal.

Aprendí que la lógica principal (el flujo del programa) debe ser limpia y clara, delegando
las tareas específicas o de apoyo a las funciones para mantener una estructura de alto nivel.
"""

"""
References:
1) Python documentation - Learning_about_strings.py
2) Python web - https://docs.python.org/es/3/using/cmdline.html
3) Curso completo de python desde cero - https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1s
4) Curso de python para principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo&t=775s
5) El tutorial de Python - https://docs.python.org/es/3/tutorial/
"""