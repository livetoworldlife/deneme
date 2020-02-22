

mon_inc=int(input("Write your monthly income value: "))
mon_exp=int(input("Write your monthly kitchen expenses: "))+\
        int(input("Write your monthly education expenses: "))+\
        int(input("Write your monthly clothing expenses: "))+\
        int(input("Write your monthly transportation expenses: "))


print("your monthly expenses to the income = % "+str(mon_exp*100/mon_inc))

# The End


