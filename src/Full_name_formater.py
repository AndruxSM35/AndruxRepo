temp_C=0

temp_C=input("set your celsius grade: ")
temp_C=(float(temp_C))
print(type(temp_C))
temp_f = temp_C* 9/5 + 32
temp_K = temp_C + 273.15
is_high_temp = temp_C>=30.0
if temp_K < 0.0:
    print("Error: This temperature is impossible")
    print(temp_K)

else:
    print("Temperature in Kelvin", temp_K)
print ("Temperature in Farenheit",temp_f)
print(is_high_temp)