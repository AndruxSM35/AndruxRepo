
try:
    temp_c=float(input("Set your grade: "))
except Exception as err:
    temp_c = -274.15

if temp_c >= 0 and temp_c > -273.15:
   print("Error: Temperature not valid")
else:
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: Temperature not valid")
    else:
        print(f"Temperature in Farenheit: {temp_c}°")
        print(f"Temperature in Kelvin: {temp_k}°")
        print(f"Temperature in Celsius: {temp_f}°")
        is_high_temerature= (temp_c >= 30.0)
        print(f"High temperature: {is_high_temerature}")