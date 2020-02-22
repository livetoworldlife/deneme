
whl_bol=True
while whl_bol:
    nam_gra = str(input("Enter the name of the course you want to convert grades: "))
    whl_bol2=True
    while whl_bol2:
        num_gra = int(input("Enter your numerical grade for the course: "))
        let_gra = ""

        if 90 <= num_gra <= 100:
            let_gra = "A"
        elif 80 <= num_gra <= 89:
            let_gra = "B"
        elif 70 <= num_gra <= 79:
            let_gra = "C"
        elif 60 <= num_gra <= 69:
            let_gra = "D"
        elif 60 > num_gra >= 0:
            let_gra = "F"
        else:
            print("Please! Enter between 0 to 100 your numerical grade for the course: ")
            continue

        break

    print("\n************************\n"
          f"Your course name: {nam_gra}\n"
          f"Your letter grade for the course: {let_gra}")



    while num_gra!="":
        con_gra = str(input("\n##########################\n"
                            "If you want to continue converting grades for another course "
                            "press 'Y',  for exit program  press 'Q' : "))
        if con_gra == "y":
            whl_bol = True
            break
        elif con_gra == "q":
            whl_bol = False
            break
        else:
            print("WARNING! press 'Y', or  press 'Q' : ")



# The End


"""
