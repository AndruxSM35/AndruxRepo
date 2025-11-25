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
