try:
    div = 10/0
    print("div")
except ZeroDivisionError:
    print("Cannot divide by zero")