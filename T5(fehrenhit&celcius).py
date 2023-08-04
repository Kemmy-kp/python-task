#''' TASK :5 take input in fehrenhit and convert in celcius & vise versa'''

'''<===Program to Convert Celsius To Fahrenheit===>'''

#Celsius = (Fahrenheit – 32) * 5/9
#Fahrenheit = (Celsius * 9/5) + 32

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))


'''<===Program to Convert Fahrenheit to Celsius===>'''

fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

