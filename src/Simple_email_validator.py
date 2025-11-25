
try:
    hours_worked=float(input("How many hours do you work in the weekend? "))
    hourly_rate=float(input("How much they pay you per hour? "))
except Exception as err:
    hours_worked=8761
    hours_worked=1800.1

if (hours_worked>=0 and hours_worked<8760) and (hourly_rate>0 and hourly_rate<1800):
    regular_hours=min(hours_worked,40)
    overtime_hours=max(0,hours_worked-40)

    overtime_pay=overtime_hours*hourly_rate*1.5
    has_overtime=(hours_worked>40)

    regular_pay=hourly_rate*regular_hours

    total_pay=regular_pay+overtime_pay

    print(f"Your regular pay is: ${regular_pay}")
    print(f"Your overtime pay is: ${overtime_pay}")
    print(f"Your Total Pay is: ${total_pay}")
    print(f"Has Overtime: ${has_overtime}")
    
else:
    print("Error: Invalid Input")
    