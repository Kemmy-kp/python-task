class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def module(self, x, y):
        return x % y
    
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"


calc = Calculator()

result_add = calc.add(5, 3)
result_subtract = calc.subtract(10, 4)
result_multiply = calc.multiply(6, 2)
result_divide = calc.divide(15, 3)
result_module=calc.module(5,7)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
print("module:",result_module)
