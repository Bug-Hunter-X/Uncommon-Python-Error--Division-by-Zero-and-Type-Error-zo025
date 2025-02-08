def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2)
print(f"Result 1: {result1}")

result2 = function_with_uncommon_error(10, 0)
print(f"Result 2: {result2}")

result3 = function_with_uncommon_error(10, "hello")
print(f"Result 3: {result3}")