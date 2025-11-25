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