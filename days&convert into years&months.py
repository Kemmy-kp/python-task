#'''lecture task 1:'''

# given number of days to years, months and days

# Reading number of days from user
number_of_days = int(input("Enter number of days: "))

# Calculating years
years = number_of_days // 365

# Calculating months
months = (number_of_days - years *365) // 30

# Calculating days
days = (number_of_days - years * 365 - months*30)

# Displaying results
print("Years = ", years)
print("Months = ", months)
print("Days = ", days)


#'''second method'''

a=int(input("enter no of days:"))

print("number of years :",a/365)
print("number of months:",a//30)
