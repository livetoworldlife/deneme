
use_kont = False
while not use_kont:
    use_nam = input("create a user name composed of 3-18 characters: ")
    if use_nam.isalpha():
        use_kont=True
    else:
        print("WARNING!!! a user name cannot include a number.")


pas_kont = False
while not pas_kont:
    pas_nam = input("create a password composed of 6-12 characters: ")
    if 6<=len(pas_nam)<=12:
        pas_kont=True
    else:
        print("WARNING!!! the number of characters in the password is less than 6 or more than 12.")


print("\n***********************\n"
      f"Your user name; {use_nam}\n"
      f"Your password; {pas_nam}")



# The End











