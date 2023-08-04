a=50
b=3

print("the value of",a,"+",b,"is:",a+b)
print("the value of",a,"-",b,"is:",a-b)
print("the value of",a,"*",b,"is:",a*b)
print("the value of",a,"/",b,"is:",a/b)
print("the value of",a,"%",b,"is:",a%b)
print("the value of",a,"//",b,"is:",a//b)


#-------type casting-------
a="2"
b="3"
print(int(a+b))

#------explicit type convertion---
string="15"
number=7
string_number=int(string)
sum=number+string_number
print("the sum of the number is: ",sum)


#variable declaration:container

'''rules to variable:

  1.can be form only with alphabet,numer or underscore(_)
  2.never contain any spaces
     eg:my var=90<---wrong
        my_var=90<----right
  3.var name never same as inbuilt keyword(33keyword)
  4. var name are case sensitive
      eg: age=67,age=43,age=90(all these three are different var name)
'''
#no variable declaration
#:"everything in python is an object"

#static var:
name="pammy"
age=45

print("=======simple snippets======")
print("your age is:",age, end=' & ')
print("your name is:",name)

print("========with formated string : f''=====")
print(f'your age is :{age} & your name is: {name}')

print("======with.format()method=====")
print("your age is:{1} & your name is : {0}".format(name,age))
#.format()is indexible
#the index will start from zero

#dynamic variable:  A variable which value depend on user input

#input():use to take user input
#input hh


a=int(input("enter val 1:"))
b=int(input("enter val 2:"))


print("addition is :",a+b)
print("subtract is :",a-b)
print("multiplication is :",a*b)
print("divition is :",a/b)
print("moduls is :",a%b)

TASK: 1
take num input from user in km &convert it into yard and meters

task:2 
take user input as radius and find area of circle

task:3


