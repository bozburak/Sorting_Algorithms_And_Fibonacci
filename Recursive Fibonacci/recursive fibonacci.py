def fibonacci(number):
    if number < 0:
        return 0
    elif number == 1:
        return 1
    else:
        result = fibonacci(number - 2) + fibonacci(number - 1)
        return result

element = int(raw_input("Which Element: "))
print fibonacci(element)