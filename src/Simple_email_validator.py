email_text=input("Set your email: ")
if strip(email_text)=="":
    print("Error: Email text not valid")
else:
    if email_text.found("@")>1:
        print("Error: You must put 1 (@)")