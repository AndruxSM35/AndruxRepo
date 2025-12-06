#PORTADA
#NOMBRE: Andreu Alexandre Gallegos Martinez
#MATRICULA:2530119
#GRUPO: IM 1-1

"""
Una sucesion Fibonacci es una sucesion infinita de numeros enteros(o naturales)
que comienza con los numeros 0 y 1. En esta sucesion cada resultado va a ser la
suma de los ultimos dos numeros anteriores, que en conjunto da como resultado una
secuencia: (Ejemplo: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,etc..), en este caso
la secuencia esta limitada a lo que pones en la entrada, y se va a detener hasta 
que llegue a ese numero de vueltas.
"""

"""
Inputs:
num_total_loop: (Its the limit of the loop of the fibonacci series)

Fibonacci series: (its the number of terms to sum separated by spaces)

Validtaions:
- n must be an int
- n must be >= 1
"""

#Problem: Fibonacci series generator
#Description: Program that reads an integrer n and prints the first n terms of the
#Fibonacci series starting at 0 and 1, and then it finishes at the number that you
#set at the input.
num_1 = 0
num_2 = 1
num_total_loop = None 
count = 0
print("Fibonacci serie")
try:
    num_total_loop = int(input("Set quantity of times \n"))
    while count < num_total_loop:
        print(f"number 1: {num_1}")
        print(f"number 2: {num_2}")
        num_1 = num_1 + num_2
        num_2 = num_1 + num_2
        print(f"Your new number 1: {num_1}")
        print(f"Your new number 2: {num_2}")
        count = count +1
        print(f"End of loop number {count}")
except ValueError:
    print("ERROR value incorrect")

#Test cases:

"""
| Normal | 4 | 0,1,1,2,3,5,8,13,21,34 |
| Border | 2 |     0,1,1,2,3,5        |
|  Error | a |  ERROR value incorrect |
"""

"""
El uso de los bucles es importante ya que hece repetir el proceso
sin necesidad de escribir miles de lineas de codigo, ademas es mas
amigable y de facil uso, a la hora de manejar los casos n=1 y n=2 hay
que tomar en cuenta que son datos completamente diferentes ya que son
dos numeros diferentes que se usan con una operacion matematica, esta
logica de la programacion se puede implementar a la hora de hacer un
programa que requiere hacer imagenes e ilustraciones publicitarias para
lograr composiciones armoniosas.
"""

"""
References:
1) Python documentation - Learning_about_strings.py
2) Python web - https://docs.python.org/es/3/using/cmdline.html
3) Curso completo de python desde cero - https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=1s
4) Curso de python para principiantes - https://www.youtube.com/watch?v=chPhlsHoEPo&t=775s
5) El tutorial de Python - https://docs.python.org/es/3/tutorial/
"""