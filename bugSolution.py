def function_with_error_handling(a, b):
    try:
        if isinstance(b, (int, float)):
            if b == 0:
                print("Error: Division by zero")
                return None
            else:
                result = a / b
                return result
        else:
            print("Error: Cannot divide by a non-numeric value")
            return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
result1 = function_with_error_handling(10, 2)
print(f"Result 1: {result1}")

result2 = function_with_error_handling(10, 0)
print(f"Result 2: {result2}")

result3 = function_with_error_handling(10, "hello")
print(f"Result 3: {result3}")

result4 = function_with_error_handling(10, 0.0)
print(f"Result 4: {result4}") #Handles floating point zero

result5 = function_with_error_handling(10, 1/0) #Handles exception during argument evaluation
print(f"Result 5: {result5}") 