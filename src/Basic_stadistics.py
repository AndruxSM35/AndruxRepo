try:
    n1=int(input("Set your first number (n1): "))
    n2=int(input("Set your second number (n2): "))
    n3=int(input("Set your third number (n3): "))
except Exception as err:
    n1 = "NO"
    n2 = "NO"
    n3 = "NO"

if not(n1=="NO" and n2=="NO" and n3=="NO"):
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