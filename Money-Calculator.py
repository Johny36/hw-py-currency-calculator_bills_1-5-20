# Money-Calculator

# INS:
# * amount of money $
# * bills (1,5,20)
# OUT:
# * number of bills
# 

# HW1:
#   what if bills (1,5,20 )  

money = int(input("Enter $: ") )

bills_20 = money // 20 
bills_5 = (money % 20) // 5
# 
# * (money <= 20) //
bills_1 =  money % 5

print(bills_20, "x $20 +", bills_5, "x $5 +", bills_1, "x $1" )
