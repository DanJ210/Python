password = input("Enter a Password: ")
tries = 1
while(not(password == "cop1000") and tries < 3):
    print("Not Correct. Try Again: ")
    if(tries == 2):
        print("You Only Have 2 Tries Left")
    tries += 1
    password = input("Enter Password ")

if(password == "cop1000"):
    print("Success")
else:
    print("You Ran Out of Tries")
