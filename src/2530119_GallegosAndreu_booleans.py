#PORTADA

#NOMBRE: Andreu Alexandre Gallegos Martinez
#MATRICULA: 2530119
#GRUPO: IM 1-1

# Resumen Ejecutivo
"""
Los int y float son parte escencial a la hora de programar en python
los tipos int son conversiones de un texto a un numero entero 'OJO, SIEMPRE
Y CUANDO NO HAYA UNA LETRA ADENTRO DEL TEXTO CONVERTIBLE todo va a funcionar
correctamente, mientras que los float son conversion a un numero real.

Un boohleano es un sistema que da valores verdadero/falso dependiendo de la condicion que
hemos dado adentro del codigo, ademas las condicionales son importantes ya que dependiendo de que si la
condicion se cumple o no te va a llevar a un resultado diferente, algunos de los boohleanos importantes
son: True/False(para obtener un valor verdadero/falso), las compuertas logicas (AND,OR,NOT).

La importancia de validar rangos es que gracias a la comparacion entre dos o varios valores es que puedes guiar
a distintos caminos si el numero es mayor, menor o igual a otro numero, es como decirle al programa de que 
haga distinta funcion dependiendo de los numeros que se quieran comparar.

Este documento cubrira como se implementan los booleanos en la practica y ademas veremos como estos afectan al codigo
dependiendo de que numero pone el usuario en la entrada.
"""

print(
"""
--------------
Temperature converter and range flag
--------------
"""
)
"""
In this code will conver the temp_c(Celsius) to temp_f(Fahrenheith) and temp_k(Kelvin).
Also verify if the Celsius temperature is >= 30.0, if it is: then is true, if it's not: then is false.
"""
"""
Inputs:
- temp_c(this is a input for a float number that is the temperature in °C)

Outputs:
- temp_f(This will print the temperature in °F)
- temp_k(This will print the temperature in °K)
- is_hight_temperature(This will print true or false depending if the
condition is completed)

Validations:
- Verify if the temp_c will transform into a float
- Don't allow any fisical temperatures impossibles on Kelvin (for example, temp_k<0)
"""
"""
Test cases table:
| Test cases |   temp_c  | temp_f  | temp_k   | is_high_temperature |
|   Normal   |    45°C   | 113.0°F | 318.15°K |       true          |
|   Border   |    -5°C   |  23.0°F | 268.15°K |       false         |
|   error    | -273.15°C |      Error: Temperature not valid        |

"""
try:
    temp_c=float(input("Set your grade: ")) 
    # In this code only inputs with floats activate the output
except Exception as err:
    temp_c = -274.15 
    # If the condition is'nt a float the code will alternate with another float to prevent errors

if temp_c <= -273.15: #The conditional if uses the input and compares it with the condition pre-assign in the code
   
   # if the input is different of the condition it will go to this function
   print("Error: Temperature not valid")
else:
    # on the contrary, it will go in this condition
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    """
    The condition prevents to divide by a number by 0 because 
    divide a number by 0 doesn't exist and this caused a error on the code.
    """
    if temp_k < 0.0:
        print("Error: Temperature not valid")
    else:
        print(f"Temperature in Celsius: {temp_c}°")
        print(f"Temperature in Kelvin: {temp_k}°")
        print(f"Temperature in Farenheit: {temp_f}°")
        is_high_temerature= (temp_c >= 30.0) #This formula sends a true or false text, it depends if the temperature is >= 30.
        print(f"High temperature: {is_high_temerature}")# Then it prints if is true or false.

print(
"""
-----------------
Work hours and overtime payment
-----------------
"""
)

"""
In this code will calculate the total weekly payment of the worker.
At least 40 hours has to pay hourly_rate wich is a float.

"""
"""
Inputs:
- hours_worked(this is the input of the weekly hours worked wich is a float)
- hourly_rate(this is a input of the pays per hour also float)
Outputs:
- regular_pay=(hourly_rate*regular_hours)
- overtime_pay=(overtime_hours*hourly_rate*1.5)
- has_overtime(it prints a value true/false)

Validations:
- verify if hours_worked >=0
- verify if hourly_rate > 0
- if one of them doesn't complete, it will print("Error: Invalid input")
"""
"""
Test cases table:
| Test cases | hours_worked | hourly_rate | regular_pay | overtime_pay | total_pay | has_ovetime |
|   Normal   |      48      |   1500.34   |   $60013.6  | 18004.079999 | $78017.68 |    true     |
|   Border   |      34      |     345     |   $11730.0  |      0.0     | $11730.0  |    false    |
|   error    |     one      |                        Error: Invalid input                        |

"""

try:
    hours_worked=float(input("How many hours do you work in the weekend? "))
    hourly_rate=float(input("How much they pay you per hour? "))
except Exception as err: #And this also works with two floats to prevent each error.
    hours_worked=8761
    hourly_rate=1800.1

if (hours_worked>=0 and hours_worked<8760) and (hourly_rate>0 and hourly_rate<1800):
    """
    We use the boolean AND for complete both conditionals and then send a true value.
    0+1=0
    1+0=0
    1+1=1
    0+0=0
    """
    regular_hours=min(hours_worked,40)
    overtime_hours=max(0,hours_worked-40)

    overtime_pay=overtime_hours*hourly_rate*1.5
    has_overtime=(hours_worked>40) #This sends a true/false value depending if the conditional is completed

    regular_pay=hourly_rate*regular_hours

    total_pay=regular_pay+overtime_pay

    print(f"Your regular pay is: ${regular_pay}")
    print(f"Your overtime pay is: ${overtime_pay}")
    print(f"Your Total Pay is: ${total_pay}")
    print(f"Has Overtime: {has_overtime}") # This prints the true/false value
    
else:
    print("Error: Invalid Input")
    
print(
"""
----------------
Discount elegibility with booleans
----------------
"""
)

"""
Check if the client has a discount with his purchase comparing with the 
booleans: AND, OR, NOT. Also calculate the total purchase applying a 10%
of discount if it is elegible.
"""
"""
Inputs:
- purchase_total (total of the purchase with a float)
- is_student_text (You have to write YES or NO depending if your student)
- is_senior_text (You have to write YES or NO depending if your a senior)

Outputs:
- discount_elegible (the output is going to be a true/false value)
- final_total (it will be the total of multiplying the purchase total*0.9)

Validations:
- Verify if purchase_total >=0
- Convert is_student_text and is_senior_text to mayusc and then
convert it a boolean is_student, is_senior
"""
"""
Test cases table:
| Test cases | purchase_total | is_student_text | is_senior_text | discount_elegible | final_total |
|   Normal   |     25.45      |       yes       |       no       |       true        |    21.105   |
|   Border   |     245.67     |        no       |      yes       |       true        | 221.1029999 |
|   error    |      hola      |                        Error: Not valid number                     |
"""

try:
    purchase_total=float(input("Set your total purchase: "))
except Exception as err:
    purchase_total= -1

if purchase_total>=0:
    is_student_text=input("Are you a student? (YES|NO): ")
    is_senior_text=input("Are you a senior? (YES|NO): ")

    is_student_text=is_student_text.upper()
    is_senior_text=is_senior_text.upper()

    if (is_student_text=="YES" or is_student_text=="NO")and(is_senior_text=="YES" or is_senior_text=="NO"):
        """
        The boolean OR compares both conditionals and if one of the two
        is completed it will send a true value.
        0+1=1
        1+0=1
        1+1=1
        0+0=0
        """
        is_student=(is_student_text=="YES")
        is_senior=(is_senior_text=="YES")

        discount_elegible=(is_student or is_senior or purchase_total>=1000.0)

        print(f"Discount Elegible: {discount_elegible}.")

        if discount_elegible:
            final_total=purchase_total*0.9
            print(f"Your total is: {final_total}")
        else:
            print(f"Your total is: {purchase_total}")
    else:
        print("Error: Invalid Input")
        
else:
    print("Error: Not valid number.")

print(
"""
---------------
Basic stadistics of three integrers
---------------
"""
)

"""
In this code will read three int numbers and calculate: sum, average(float), max value,
min value, and a boolean all_even wich indicates if the three numbers are pairs.
"""
"""
Inputs:
- n1 (its the first number and it's a int number)
- n2 (its the second number and it's a int number)
- n3 (its the third number and it's a int number)

Outputs:
- sum_value (It will sum all the values an then put the result in the output)
- avg_value (It will put the result of the average of the values in the output)
- max_value (The max value of the three nums set in the input)
- min_value (The minimun value of the three nums set in the input)
- all_even (the true/false value if the condition is completed)

Validations:
- Verify if the three values can be converted to int
- They don't required any additional restrictions (it works with negatives too)
"""
"""
Test cases table:
| Test cases |   n1,n2,n3  | sum_value | average_value | max_value | min_value | all_even |
|   Normal   |  578,54,76  |   708     |      236.0    |    578    |      54   |   true   |
|   Border   |   23,56,-3  |    76     |       25.3    |    56     |      -3   |   false  |
|   error    | 23,56,holii |                 Error: Number not valid                      |

"""
try:
    n1=int(input("Set your first number (n1): "))
    n2=int(input("Set your second number (n2): "))
    n3=int(input("Set your third number (n3): "))
except Exception as err:
    # The exeption also works with text
    n1 = "NO"
    n2 = "NO"
    n3 = "NO"

if not(n1=="NO" and n2=="NO" and n3=="NO"):
    """
    The boolean NOT is for making the contrary of the conditional,
    in this case if the values are completed it will send a false value.
    0+1=1
    1+0=1
    1+1=0
    0+0=1
    """
    sum_value=n1+n2+n3
    print(f"Your sum is: {sum_value}")

    avg_value=sum_value/3
    print(f"Your Average is: {avg_value}")

    max_value=max(n1,n2,n3)
    print(f"Your Max Value is: {max_value}")

    min_value=min(n1,n2,n3)
    print(f"Your Min Value is: {min_value}")

    all_even=(n1 % 2 ==0) and (n2 % 2==0) and (n3 % 2==0)
    print(f"All Even: {all_even}")
else:
    print("Error: Number not valid")

print(
"""
----------------------
Loan eligibility (income and debt ratio)
----------------------
"""
)


"""
In this code will verify if a person is elegible for a loan with:
the montly cash and the montly debt and with the credit score.
"""
"""
Inputs:
- monthly_income (the montly cash earn, float)
- monthly_debt (the monthly debt, float)
- credit_score (the credit score earned, int)

Outputs:
- debt_ratio (to set how much the person debts dividing the monthly_debt/monthly_income)
- elegible (if the monthly income, debt_ratio and credit_score are elegible, it will print true)

Validations:
- if the monthly_income > 0.0 (and also prevent the division by 0)
- if monthly_ debt >= 0.0
- if credit_score >= 0
- and if none of them is completed it will print("Error: invalid input")
"""
"""
Test cases table:
| Test cases |  monthly_income | monthly_debt | credit_score | debt_ratio | elegible |
|   Normal   |     45067.34    |   1500.15    |     1450     |   0.03328  |   true   |
|   Border   |     2700.25     |    1000.0    |      45      |   0.37033  |   false  |
|   error    |     34500.0     |    6780.0    |    three     | Error: Invalid Input  |

"""
try:
    monthly_income=float(input("Set your monthly income: "))
    monthly_debt=float(input("Set your monthly debt: "))
    credit_score=int(input("Set your credit score: "))
except Exception as err:
    monthly_income = -1
    monthly_debt = -1
    credit_score = -1

if monthly_income>0 and monthly_debt>=0 and credit_score>=0:
    debt_ratio=monthly_debt / monthly_income
    print( )
    print(f"Debt Ratio: {debt_ratio}")

    elegible=(monthly_income>=8000.0)and(debt_ratio<=0.4)and(credit_score>=650)
    print(f"Elegible: {elegible}.")
else:
    print("Error: invalid input.")

print(
"""
------------------
Body Mass index (BMI) and category flag
------------------
"""
)

"""
In this code will calculate the mass of the person in base of the weight
and the height with a formula: bmi = weight_kg / (height_m * height_m).
"""
"""
Inputs:
- weight_kg (the weight of the person in kilograms (float))
- height_m (the height of the person in meters (float))

Outputs:
- bmi_round (the bmi with round of 2 for the result of the bmi)
- is_underweight (if the person is underweight print true)
- is_normal (if the person is normal print true)
- is_overweight (if the person is overweight print true)

Validations:
- if weight_kg > 0.0
- if height_m > 0.0
- if doesn't complete, print("Error: Invalid Input")
"""
"""
Test cases table:
| Test cases | weight_kg | height_m | bmi_round | is_underweight | is_normal | is_overweight |
|   Normal   |     70    |   1.80   |   21.6    |      false     |   true    |     false     |
|   Border   |    1.80   |  35.46   |    0.0    |      true      |   false   |     false     |
|   error    |     21    |   hola   |                  Error: Invalid Input                  |

"""

try:
    weight_kg=float(input("Set your weight in KG: "))
    height_m=float(input("Set your height in m: "))
except Exception as err:
    weight_kg=-1
    height_m=-1

if weight_kg>0 and height_m>0:
    bmi=weight_kg/(height_m*height_m)
    bmi_round=round(bmi,2)
    print(f"BMI: {bmi_round}")

    is_underweight=(bmi<18.5)
    print(f"Underweight: {is_underweight}.")

    is_normal=(18.5<=bmi<25)
    print(f"Normal: {is_normal}.")

    is_overweight=(bmi>=25)
    print(f"Overweight: {is_overweight}")
else:
    print("Error: invalid input.")

"""
Los enteros y los flotantes se usan de forma conjunta para calcular 
valores reales, ya que los enteros son para formar un valor cortado
pero mas ordenado, mientras que los flotantes se usan como valores reales
y ademas para hacer divisiones y que de el resultado mas cercano posible.

Las comparaciones generan booleanos para tomar una decision y hacer distintas
funciones dependiendo de que si se alcanza el objetivo o no. Ademas, aprendi que
a la hora de trabajar en conjunto con las compuertas logicas hace ahorrar muchas
lineas de codigo inecesarias, ademas nos sirve a la hora de aplicar la logica y
preguntarnos que pasaria si se cumple o no la condicion?

Es importante validar rangos y evitar division entre 0 ya que a la hora de correr el
codigo y no corregir los errores pues genera que el codigo se pare y no vuelva a funcionar
asi que hay que corregir la mayoria de los errores posibles.

Los patrones se repiten ya que nos ayuda a ver el limite que tienen que tener
ya que no todos los prestamos, descuentos, prestamos, etc son infinitos, tienen
un limite, y hay que respetar ese limite.
"""

"""
References:
1) Python documentation - Learning_about_strings.py
2) Python web - https://docs.python.org/es/3/using/cmdline.html
3) Curso completo de python desde cero - https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1s
4) Curso de python para principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo&t=775s
5) El tutorial de Python - https://docs.python.org/es/3/tutorial/
"""