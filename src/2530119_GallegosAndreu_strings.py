#PORTADA
#NOMBRE: Andreu Alexandre Gallegos Martinez
#MATRICULA: 2530119
#GRUPO: IM 1-1

#Resumen Ejecutivo

"""
Un **string** (cadena de texto) en Python es una secuencia ordenada de caracteres. Es un tipo de
dato fundamental que se utiliza para almacenar texto. Los strings son **inmutables**,
lo que significa que no se pueden modificar una vez creados; cualquier operación de
"modificación" en realidad crea un nuevo string.
#
Las operaciones básicas incluyen **concatenar** (+) para unir cadenas, obtener su **longitud**
con `len()`, **extraer sub-cadenas** (slicing) con corchetes, **buscar patrones** y
**reemplazar texto** utilizando métodos como `.find()`, `.replace()`, etc.
#
Es crucial **validar y normalizar** el texto de entrada (como correos o nombres) para
asegurar la calidad y consistencia de los datos. Esto puede incluir convertir a minúsculas
o mayúsculas (`.lower()/.upper()`), eliminar espacios sobrantes (`.strip()`) y verificar formatos.
#
Este documento cubrirá: la descripción de cada problema, el diseño de entradas y salidas,
las validaciones aplicadas (normalización de texto) y el uso de métodos de string clave
con casos de prueba específicos (incluyendo el código).
"""
print("""
    ----------- 
    Full name formatter (name + initials)
    ----------
    """)

"""
Descripción:
El programa recibe el nombre completo de una persona en una sola cadena.
Primero normaliza el texto eliminando espacios extra y aplicando el
formato adecuado de mayúsculas/minúsculas. Después muestra el nombre en
Title Case y produce las iniciales formadas por cada palabra del nombre.
Input:
    - full_name (string; puede venir en mayúsculas, minúsculas o mezclado, con
      espacios extra).
Output:
    - "Formatted name: <Name In Title Case>"
    - "Initials: <X.X.X.>"
Validations:
    - full_name no debe estar vacío después de strip().
    - Debe contener al menos dos palabras.
    - No se aceptan cadenas que sean solo espacios.
"""


full_name = input("Enter your full name: ")


name = full_name.strip()


if name == "":
    print("Error: name cannot be empty.")
else:
    parts = name.split()  

    
    if len(parts) < 2:
        print("Error: please enter at least first name and last name.")
    else:
        
        formatted_name = " ".join(p.capitalize() for p in parts)

        
        initials = ".".join(p[0].upper() for p in parts) + "."

        print("Formatted name:", formatted_name)
        print("Initials:", initials)
"""
Test cases:
1) Normal: "Andreu Alexandre Gallegos Martinez" → "Andreu Alexandre Gallegos Martinez", "A.A.G.M."
2) Border: " Luis Roberto " → "Luis Roberto", "L.R."
3) Error: "CecyaJimenez" → Error: please enter at least first name and last name
"""
print("""
-----------------------
Simple email validator (structure + domain)
-----------------------
""")

"""
Descripción:
Este programa verifica si una cadena corresponde a un correo electrónico
con formato básico válido. Revisa que haya exactamente un '@', que después
de este exista al menos un punto y que no existan espacios en blanco.
Si es válido, también muestra el dominio (todo lo que sigue al '@').

Input:
        - email_text (string).
Output:
    - "Valid email: true" o "Valid email: false"
    - Si es válido: "Domain: <domain_part>"
Validations:
    - email_text no debe estar vacío tras strip().
    - Debe tener exactamente un '@'.
    - Debe tener al menos un punto después del '@'.
    - No debe contener espacios (aunque el código actual solo verifica la presencia de @ y .).
"""

email_text = input("Enter your email: ")
email = email_text.strip()
if email == "": 
    print("Valid email: false") 
else:
        if email.count("@") != 1: 
            print("Valid email: false") 
        else:
            
            local, domain = email.split("@", 1) 
            
            if local == "" or domain == "" or "." not in domain:
                print("Valid email: false")
            
            else:
                
                print("Valid email: true")
                print("Domain:", domain)
"""
Test cases:
 Normal: "2530119@upv.edu.mx" → válido: true → dominio: "upv.edu.mx"
 Border: "a@cl.co" → valido: true → dominio: "cl.co"
 Error: "user@@mail.com" → valido: false 
"""

print("""
-----------------
Palindore cheker (ignoring spaces and case)
-----------------
""")

"""
Descripción:
Este programa verifica si una frase o palabra es un palíndromo (se lee igual de
izquierda a derecha y viceversa). Para la verificación, ignora los espacios en
blanco y el uso de mayúsculas/minúsculas. Se requiere un mínimo de 3 caracteres.
Input:
    - phrase (string): La frase o palabra a verificar.
Output:
    - "Palindrome is: true" o "Palindrome is: false"
Validations:
    - La frase no debe estar vacía tras strip().
    - La frase normalizada (sin espacios) debe tener un mínimo de 3 caracteres.
"""

phrase = input("Enter your phrase: ")
palindrome_phrase = phrase.strip()

if palindrome_phrase == "":
    print("Palindrome is: false")
else:
    
    palindrome = palindrome_phrase.lower().replace(" ", "")

    
    if len(palindrome) < 3:
        print("Palindrome is: false")
    else:
       
        reversed_text = palindrome[::-1]

        
        if palindrome == reversed_text:
            print("Palindrome is: true")
        else:
            print("Palindrome is: false")
"""
Test cases:
1) Normal: "A luna ese anula" → Palindrome is: true
2) Border: "OSO" → Palindrome is: true
3) Error: "palabra" → Palindrome is: false
4) Error: "no" → Palindrome is: false (menos de 3 letras)
"""

print("""
--------------------------------
Sentence word stats (lengths and first/last word)
--------------------------------
""")

"""
Descripción:
Este programa toma una frase y calcula varias estadísticas sobre las palabras
que la componen: el conteo total de palabras, la primera y última palabra,
y la palabra más corta y la más larga.
Input:
    - sentence (string): La frase de la cual se extraerán las estadísticas.
Output:
    - "Word count: <count>"
    - "First word: <word>"
    - "Last word: <word>"
    - "Shortest word: <word>"
    - "Longest word: <word>"
Validations:
    - La frase no debe estar vacía tras strip().
    - La frase debe contener al menos una palabra válida (tras split()).
"""


sentence = input("Enter a sentence: ")


text = sentence.strip()


if text == "":
    print("Sentence is empty.")
else:
    
    words = text.split()

    
    if len(words) == 0:
        print("Sentence is invalid.")
    else:
        
        count = len(words)

        
        first_word = words[0]
        last_word = words[-1]

        
        shortest = min(words, key=len)
        longest = max(words, key=len)

        
        print("Word count:", count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest)
        print("Longest word:", longest)
"""
Test cases:
1) Normal: "El rápido zorro salta sobre el perro" → Count: 6, First: El, Last: perro, Shortest: El, Longest: rápido
2) Border: "hola" → Count: 1, First: hola, Last: hola, Shortest: hola, Longest: hola
3) Error: "   " → Sentence is empty.
"""

print("""
------------------
Password strength classifier
------------------
""")

"""
Descripción:
Este programa clasifica la fuerza de una contraseña ingresada como 'weak',
'medium' o 'strong', basándose en su longitud y la presencia de diferentes
tipos de caracteres: mayúsculas, minúsculas, dígitos y símbolos.
Input:
    - password_input (string): La contraseña a analizar.
Output:
    - "Password strength: <weak/medium/strong>"
Validations:
    - La contraseña vacía o muy corta (<8 caracteres) se considera débil.
    - Se verifica la presencia de los 4 tipos de caracteres para ser 'strong'.
"""


password_input = input("Enter a password: ")


if password_input.strip() == "":
    print("Password strength: weak")  
else:
    password = password_input  

    
    has_upper = False  
    has_lower = False  
    has_digit = False  
    has_symbol = False  

    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum(): 
            has_symbol = True

    length = len(password)

    if length < 8 or (has_lower and not has_upper and not has_digit and not has_symbol):
        print("Password strength: weak")

    
    elif length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")


    else:
        print("Password strength: medium")
"""
Test cases:
1) Strong: "P4ssw0rd!_" → strong
2) Medium: "pass12345" → medium (le faltan mayúsculas y símbolo)
3) Weak: "password" → weak (es >8 pero solo minúsculas)
4) Weak: "" → weak
"""

print("""
-------------------
Product label formater (fixed-width text)
-------------------
""")

"""
Descripción:
Este programa formatea la etiqueta de un producto y su precio en una cadena
de ancho fijo (30 caracteres). Si la etiqueta es más corta, se rellena con
espacios a la derecha (`ljust`). Si es más larga, se trunca a 30 caracteres.
Input:
    - product_name (string): Nombre del producto.
    - price_value (string): Precio del producto.
Output:
    - 'Label: "<etiqueta_formateada>"'
Validations:
    - product_name no debe estar vacío.
    - price_value debe ser un número positivo (float).
"""


product_name = input("Enter product name: ")
price_value = input("Enter price: ")


name = product_name.strip()
if name == "":
    print('Error: product name cannot be empty.')
else:
    try:
        price_num = float(price_value)
        if price_num <= 0:
            raise ValueError("non-positive")
    except:
        print('Error: price must be a positive number.')
    else:
        
        price_str = f"{price_num:.2f}"

        
        label_base = f"Product: {name} | Price: ${price_str}"

        
        if len(label_base) < 30:
            label = label_base.ljust(30)  
        else:
            label = label_base[:30]

        
        print('Label: "' + label + '"')
"""
Test cases:
1) Normal (Llenado): Name: "Pen" Price: 1.5 → "Product: Pen | Price: $1.50   "
2) Normal (Truncado): Name: "Long Product Name Here 12345" Price: 99.99 → "Product: Long Product Name"
3) Error: Price: "cero" → Error: price must be a positive number.
"""
"""
El manejo de **strings** es fundamental, ya que toda interacción con el usuario (entrada/salida)
y la lectura de archivos se basa en texto. Es el puente entre el humano y el código.

Métodos como `.strip()`, `.lower()`, y `.upper()` son clave para **normalizar** el texto,
asegurando que comparaciones de contraseñas o nombres no fallen por un error de tipografía.
Usar `.split()` y `.join()` nos permite dividir una frase en palabras o iniciales y reconstruirla.

Las **validaciones** son esenciales para proteger el sistema de "datos basura", asegurando que
el texto tenga el formato, longitud y contenido esperados (ej., validar estructura de correos).

Aprendí que la **inmutabilidad** de los strings implica que métodos como `.replace()` crean una
nueva cadena, y el uso de *slices* (ej., `[::-1]` para invertir) es una herramienta muy poderosa
para manipular secuencias de caracteres eficientemente.
"""

"""
References:
1) Python documentation - Learning_about_strings.py
2) Python web - https://docs.python.org/es/3/using/cmdline.html
3) Curso completo de python desde cero - https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1s
4) Curso de python para principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo&t=775s
5) El tutorial de Python - https://docs.python.org/es/3/tutorial/
"""