

name_sn = str(input("name-surname; "))

#- Exam scores and class attendance score range between 0-100.
# The total number of lecture that a student should attend is 20.

a=True
while a:
    mid_ex = int(input("midterm exam score; "))
    if mid_ex>0 and mid_ex<= 100:
        b=True
        while b:
            fin_ex = int(input("final exam score; "))
            if fin_ex > 0 and fin_ex <= 100:
                c=True
                while c:
                    mis_lec = int(input("Write your missing lecture; "))
                    if mis_lec>=0 and mis_lec <= 20:
                        cou_po = 100 - (mis_lec * 5)
                        break
                    else:
                        print("You must enter your missing lecture between 0 and 20")

                break
            else:
                print("You must enter the final exam score between 1 and 100")

        break
    else:
        print("You must enter the midterm exam score between 1 and 100")

#Percentages:
# Midterm exam score: 30%
# Final exam score: 50%
# Course attendance score: 20%

fin_grade = (mid_ex*0.3)\
            +(fin_ex*0.5)\
            +(cou_po*0.2)
result = [name_sn,mid_ex,fin_ex,mis_lec,fin_grade]

print("\n*************************\n"
      "Name and surname; {}\n"
      "midterm exam score; {}\n"
      "final exam score; {} \n"
      "course attendance information; {} \n"
      "the final course grade; {}".format(result[0],result[1],result[2],result[3],result[4]))

# Print the name-surname, midterm and final exam scores,
# course attendance information and final course grade of a student on the screen.

# The End
