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
