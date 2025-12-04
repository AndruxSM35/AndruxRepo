#PORTADA

#NOMBRE: Andreu Alexandre Gallegos Martinez
#MATRICULA: 2530119
#GRUPO: IM 1-1

#Resumen Ejecutivo
"""
Lista, Tupla y Diccionario son colecciones de datos. La **Lista** [] es una colección ordenada y modificable.
La **Tupla** () es una colección ordenada pero **inmodificable**. El **Diccionario** {} es una colección
no ordenada que almacena datos en pares de **Clave: Valor**.

**Mutable** (Lista) significa que puedes añadir, eliminar o modificar elementos después de su creación.
**Inmutable** (Tupla) significa que su contenido no puede ser alterado una vez definido.

Los Diccionarios se usan para crear **asociaciones lógicas**, donde una Clave única (ej., "nombre")
apunta a un Valor (ej., "Juan"). Esto permite recuperar el valor de forma muy rápida.

Este documento cubrirá: la descripción de cada problema, el diseño de entradas y salidas,
las validaciones aplicadas y el uso estratégico de Listas (ej., ítems y notas), Tuplas
(ej., coordenadas de puntos) y Diccionarios (ej., catálogos de productos y agendas de contacto)
en contextos prácticos de programación.
"""

print("""
--------------------------
Shopping list basic (list operations)
--------------------------
""")

"""
En este código se crea una lista de la compra a partir de una cadena de texto,
se le añade un nuevo elemento y se verifica si un elemento específico se encuentra en la lista.
"""
"""
Inputs:
- initial_items_text (string): Lista inicial de ítems separados por comas.
- new_item (string): Ítem a añadir a la lista.
- search_item (string): Ítem a buscar en la lista.

Outputs:
- item_list (list): La lista de ítems modificada.
- len_list (int): El número total de ítems en la lista.
- found_item (bool): True si el ítem de búsqueda se encuentra, False si no.
- Mensaje de Error: "Error: You must have at least 1 item" si la lista inicial está vacía.

Validations:
- Verifica que la lista inicial no esté vacía.
- Verifica que las entradas de 'new_item' y 'search_item' no estén ambas vacías (aunque esto podría simplificarse).
"""
"""
Test cases table:
| Test cases | Initial Items | New Item | Search Item | Total Items | Found Item |
|   Normal   | "Manzana,Pera" | "Leche"  | "Pera"      |       3     |     True    |
|   Border   |    "Uno"     | "Dos"    | "Tres"      |       2     |     False   |
|   error    |     ""       |            Error: You must have at least 1 item     |

"""

initial_items_text=(input("Set your first list: "))
item_list=initial_items_text.strip()

if not(item_list==""): 

    item_list=initial_items_text.split(",")
    print(item_list)

    new_item=input("Set your item to add in the list: ").strip()
    search_item=input("Set your item that you want to search: ").strip()

    if not(new_item=="" and search_item==""):
        item_list.append(new_item) 
        print(item_list)

        len_list=len(item_list)
        print(f"Total Items: {len_list}")

        found_item=(search_item in item_list)
        print(f"Found Item: {found_item}")
    else:
        print("Item not valid")
else:
    print("Error: You must have at least 1 item")

print(
"""
--------------
Points and distances with tuples
--------------
"""
)

"""
En este código se calculan la distancia y el punto medio entre dos puntos (A y B)
en un plano cartesiano, utilizando tuplas para representar las coordenadas (x, y).
"""
"""
Inputs:
- x1, y1, x2, y2 (float): Coordenadas de los dos puntos (A y B) ingresadas por el usuario.

Outputs:
- point_a, point_b (tuple): Las coordenadas de los puntos.
- distance (float): La distancia euclidiana entre A y B.
- midpoint (tuple): Las coordenadas del punto medio entre A y B.
- Mensaje de Error: "Error: Number not valid" si alguna coordenada no es un número.

Validations:
- Verifica que todas las entradas se puedan convertir a float.
"""
"""
Test cases table:
| Test cases |   x1, y1  | x2, y2   | Distance  | Midpoint  |
|   Normal   |  (1, 1)   | (4, 5)   |    5.0    |  (2.5, 3.0)  |
|   Border   |  (0, 0)   | (0, 0)   |    0.0    |  (0.0, 0.0)  |
|   error    |  "a"      |      Error: Number not valid        |

"""
try:
    x1=float(input("Set your first cord x: "))
    y1=float(input("Set your first cord y: "))
    x2=float(input("Set your second cord x: "))
    y2=float(input("Set your second cord y: "))

    point_a=(x1,y1)
    print(f"Point A: {point_a}")

    point_b=(x2,y2)
    print(f"Point B: {point_b}")

    distance=((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print(f"Distance: {distance}")

    midpoint=((x1 + x2)/2, (y1 + y2)/2)
    print(f"Midpoint: {midpoint}")


except Exception as err:
    print("Error: Number not valid")

print(
"""
--------------
Product catalog with dictionary
--------------
"""
)

"""
En este código se simula la compra de un producto de un catálogo predefinido (diccionario).
Calcula el precio total de la compra basado en el nombre del producto y la cantidad.
"""
"""
Inputs:
- product_name (string): Nombre del producto a comprar.
- quantity (int): Cantidad de unidades a comprar.

Outputs:
- unit_price (int): Precio unitario del producto.
- total_price (int): Precio total (unit_price * quantity).
- Mensaje de Error: "Error: product not found" si el nombre no está en el catálogo.
- Mensaje de Error: "Error: Quantity not valid." si la cantidad es <= 0.
- Mensaje de Error: "Error: Product name not valid." si el nombre del producto está vacío.

Validations:
- Verifica que 'quantity' sea un entero positivo.
- Verifica que el 'product_name' ingresado exista como clave en el diccionario.
"""
"""
Test cases table:
| Test cases | Product Name | Quantity | Total Output                |
|   Normal   | "game boy"   |    2     | Unit price: 125, Total: 250 |
|   Error    |    "tv"      |    1     | Error: product not found    |
|   Error    |    ""        |    5     | Error: Product name not valid.|

"""
product_prices={
    "game boy": 125,
    "shield" : 92,
    "apple juice" : 12,
    
    }
print(product_prices)

product_name=input("Set your product name: ")
product_name_low=product_name.lower()
product_name_leng=(product_name_low.strip())

try:
    quantity=int(input("Set your quantity for shop: "))
except Exception as err:
    quantity=-1


if product_name_leng=="":
    print("Error: Product name not valid.")
else:
    if quantity > 0:

        if product_name_leng in product_prices:
            unit_price=product_prices[product_name_leng]
            print(f"Unit price: {unit_price}")

            print(f"Quantity: {quantity}")

            total_price=unit_price*quantity
            print(f"Total: {total_price}")

        else:
            print("Error: product not found")
    else:
        print("Error: Quantity not valid.")

print (
"""
---------------------
Student grades with dict and list
---------------------
"""
)

"""
En este código se calcula el promedio de las calificaciones de un estudiante.
Utiliza un diccionario donde la clave es el nombre del estudiante y el valor es una lista de notas.
"""
"""
Inputs:
- student_name (string): El nombre del estudiante a buscar.

Outputs:
- grades (list): La lista de calificaciones del estudiante.
- avrg (float): El promedio de las calificaciones.
- Mensaje de Error: "Error: student not found." si la entrada está vacía.
- Mensaje de Error: "Error: Student not found" si el nombre no existe en el diccionario.

Validations:
- Normaliza el nombre del estudiante (a mayúsculas) para la búsqueda.
- Verifica que el nombre ingresado exista como clave en el diccionario.
"""
"""
Test cases table:
| Test cases | Student Name | Grades List   | Average Output |
|   Normal   |   "luis"    |   [70,50,100] |       73.33     |
|   Error    |   "pablo"   |            Error: Student not found   |
|   Error    |     ""      |            Error: student not found.  |

"""
students={
    "LUIS" : [70,50,100],
    "ANDREA" :[20,50,60],
    "ANDREU" : [50,40,100],
}
print(students)

student_name=input("Set the name of the student: ")
student_name=student_name.upper()
student_name=student_name.strip()

if student_name=="":
    print("Error: student not found.")
else:
    if student_name in students:
        grades = students[student_name]
        print(grades)

        avrg=sum(grades)/len(grades)
        print(avrg)

    else:
        print("Error: Student not found")
    
print(
"""
-------------
Word frecuency counter (list+ dict)
-------------
"""
)

"""
En este código se calcula la frecuencia de las palabras en una oración ingresada por el usuario.
Utiliza listas y diccionarios para contar las ocurrencias e identifica la palabra más común.
"""
"""
Inputs:
- sentence (string): La oración completa a analizar.

Outputs:
- words_list (list): La lista de palabras en la oración.
- freq_dict (dict): Diccionario de frecuencias (palabra: conteo).
- common_word (string): La palabra con la frecuencia más alta.
- Mensaje de Error: "Error: sentence not valid." si la oración está vacía.

Validations:
- Normaliza la oración a minúsculas y elimina espacios iniciales/finales.
- Maneja oraciones vacías.
"""
"""
Test cases table:
| Test cases | Sentence              | Most Common Word Output              |
|   Normal   | "hola hola mundo"     | Most common word hola with 2          |
|   Border   |   "solo una"         | Most common word solo with 1          |
|   error    |     ""              |    Error: sentence not valid.          |

"""
sentence=input("Set your sentence: ")
sentence=sentence.lower()

sentence=sentence.strip()

if not(sentence==""):
    words_list=sentence.split()

    
    print(f"Words List: {words_list}")

    freq_dict={}

    for freq_word in words_list:
        if freq_word:
            freq_dict[freq_word] = freq_dict.get(freq_word,0)+1

    print(f"Frecuencies: {freq_dict}")

    if freq_dict:
        max_freq = max(
            freq_dict.items(),
            key=lambda item: item[1]
            )   
        """
        lambda in python is for define in 1 line just
        one expression.

        for example:
        number = lambda x: x + 10

        print(number(5)) #Output 15
        """
    
        common_word=max_freq[0]
        frecuency=max_freq[1]

        print(f"Most common word {common_word} with {frecuency}")
    else:
        print("Error: Nothing to analize")
else:
    print("Error: sentence not valid.")


print(
"""
----------------
Simple contact book dictionary CRUD
----------------
""" 
)

"""
En este código se simulan operaciones básicas de una agenda de contactos (CRUD).
Utiliza un diccionario donde la clave es el nombre y el valor es el número de teléfono.
"""
"""
Inputs:
- accion_text (string): La operación a realizar ('ADD', 'SEARCH' o 'DELETE').
- name (string): Nombre del contacto para la operación.
- phone (string): Número de teléfono (solo para 'ADD').

Outputs:
- Muestra el diccionario 'contacts' actualizado o el resultado de la búsqueda.
- Mensaje de Éxito o Error según la operación.

Validations:
- Verifica que 'accion_text' sea una de las opciones válidas.
- Normaliza el nombre del contacto (a mayúsculas) para las operaciones.
- Verifica la existencia del contacto para 'SEARCH' y 'DELETE'.
"""
"""
Test cases table:
| Test cases | Action | Name   | Outcome                              |
| :--- | :--- | :--- | :--- |
|   ADD      | "ADD"  | "PABLO"| Contact saved PABLO, [phone]          |
|   SEARCH   | "SEARCH" | "LUIS" | Phone: 8343539461                    |
|   DELETE   | "DELETE" | "ANDRUX" | Contact deleted: ANDRUX, [new dict] |
|   Error    | "a"    |        | Error: menu not valid.                |

"""
contacts= { "ANDRUX":"8342736866", "LUIS": "8343539461" }
print(contacts)

accion_text= (input("'ADD','SEARCH' or DELETE: ")).upper()

if not(accion_text== "ADD" or accion_text=="SEARCH" or accion_text=="DELETE"):
    print("Error: menu not valid.")

elif accion_text=="ADD":
    name=(input("Set the name of the contact: ").upper())
    phone=input(f"Set the phone number of {name}:")

    contacts[name] = phone
    print(f"Contact saved {name}, {phone}")
    print (contacts)

elif accion_text== "SEARCH":
    name=(input("Set the name of the contact: ").upper())
    if name in contacts:
        print(name)
        phone=contacts[name]
        print(f"Phone: {phone}")
    else:
        print("Error: contact not found")

else:
    name=(input("Set the name of the contact to delete: ").upper())
    if name in contacts:
        del_contact=contacts.pop(name)
        print(f"Contact deleted: {name}")
        print(contacts)
    else:
        print("Error: contact not found.")

"""
La elección de la estructura es clave: las **listas** son ideales para colecciones dinámicas
(como una lista de compras o un historial) debido a su flexibilidad para agregar o eliminar elementos.

Las **tuplas** son perfectas para datos fijos y estructurados, como coordenadas (x, y) o
registros que no deben alterarse, ya que su inmutabilidad garantiza la integridad de la información.

Los **diccionarios** brillan en escenarios de búsqueda, ya que asocian valores complejos
a una clave única, permitiendo recuperar la información rápidamente (ej. catálogo de productos).

Encontré patrones comunes al combinarlas, como el **diccionario de listas** (ej. estudiante: [notas])
o la **lista de diccionarios** (ej. [ {producto: precio}, {otro_producto: precio} ]), lo que
permite modelar datos más complejos de manera eficiente.
"""

"""
References:
1) Python documentation - Learning_about_strings.py
2) Python web - https://docs.python.org/es/3/using/cmdline.html
3) Curso completo de python desde cero - https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1s
4) Curso de python para principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo&t=775s
5) El tutorial de Python - https://docs.python.org/es/3/tutorial/
"""