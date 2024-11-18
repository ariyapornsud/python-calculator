class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0:
            for i in range(-b):
                result = self.subtract(result, a)  # Subtract a
        else:
            for i in range(b):  # Loop for positive
                result = self.add(result, a)  # Add a
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")  # Handle division by zero
        result = 0
        while a >= b:  # subtracting until a less than b
            a = self.subtract(a, b)
            result = self.add(result, 1)  # Add 1 
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")  # Handle modulo by zero
        while a >= b:  # subtracting until a is less than b
            a = self.subtract(a, b)
        return a  # Return the remainder



# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))