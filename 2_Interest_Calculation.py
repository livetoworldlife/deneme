
pri_amo = int(input("Principal amount; "))
per_time = int(input("Period of Time (year); "))
rat_int = int(input("Annual Rate of interest; "))


tot_int = pri_amo*per_time*rat_int/100
mon_int = pri_amo*rat_int/(12*100)
dai_int = pri_amo*rat_int/(365*100)
tot_bal = tot_int+pri_amo

result = [tot_int,mon_int,dai_int,tot_bal]

print("\n*********************\n"
      "the total interest; {r[0]}\n"
      "average monthly interest; {r[1]}\n"
      "average daily interest; {r[2]}\n"
      "total balance; {r[3]}".format(r=result))

#After having the program calculate the interest,
# print out the total interest;
# average monthly interest
# and average daily interest;
# total balance (total interest + principal amount).


# The End
