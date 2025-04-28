

try:
    result = 10 / 0.0001
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
finally:
    print("execution complete")


