import math

#Prints out information regarding investment and bond
print('''Please read the following information before continuing:
- Investment: to calculate the amount of interest you'll earn on your investment
- Bond: - to calculate the amount you'll have to pay on a home loan''')

#Variable for user to enter which calculation would like to do (Investment or Bond)
Calculation = input("Please enter 'investment' or 'bond' from the above options to proceed: ").capitalize()

#Calculation of the investment options
if Calculation == "Investment" :
    Deposit = int(input("Please insert the amount of money that you are depositing: "))     #Variable to store amount of money that user will deposit
    Interest_rate = int(input("Please enter the interest rate: "))     #Variable to store the interest rate that user entered
    r = Interest_rate / 100     #Variable which contains the interest rate divided by 100
    Years = int(input("Please enter the number of years you plan on investing: "))     #Variable to store the number of years that user will plan to invest
    Interest = input("Which interes you prefer? Simple or Compound: ").capitalize()     #Variable for user to insert which interest will choose
    
    #Calculation of simple interest 
    if Interest == "Simple" :
        Total_amount = Deposit * (1 + r * Years)
        Total_amount = round(Total_amount, 2)     #Round to 2 decimals the result of Total_amount
        print(f"After {Years} years you will earn a total of: £{Total_amount}" )     #Prints out the total amount after the period of investing time has finished
    
    #Calculation of compound interes
    elif Interest == "Compound" :
        Total_amount = Deposit * math.pow((1 + r), Years)
        Total_amount = round(Total_amount, 2)     #Round to 2 decimals the result of Total_amount
        print(f"After {Years} years you will earn a total of: £{Total_amount}" )     #Prints out the total amount after the period of investing has finished

    #Out put if user insert in Calculation another thing that is not 'simple' or 'compound'
    else :
        print("Selection not recorgnised. Please make sure that you write 'Simple' or 'Compound'.")

#Calculation if user selects bond
elif Calculation == "Bond" :
    Value_house = int(input("Please enter the present value of the house: "))     #Variable to store the present value of the house entered by the user
    Interest_rate = int(input("Please enter the interest rate: "))     #Variable to store the interest rate that user entered
    monthly_interest = (Interest_rate / 100) / 12     #Variable to store the monthly interest rate
    Months = int(input("Please enter the number of months that you plan to repay the bond: "))     #Variable to store the total number of months that user entered to pay the bond
    Repayment = (monthly_interest * Value_house) / (1 - (1 + monthly_interest) ** (-Months))
    Repayment = round(Repayment, 2)     #Round to 2 decumals the result of Repayment
    print(f"You will have to pay £{Repayment} for {Months} months")     #Print out the amount of money that user will pay monthly

#Prints out if user entered another thing that is not 'investment' or 'bond'
else :
    print("Error! You did not insert any of the above choices. Make sure that you write 'investment' or 'bond'.  ")