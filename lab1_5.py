def check_multiple(number):
    if (number % 3 == 0 and number % 5 == 0):
        return True
    else:
        return False
def check_password(input_string):
    if (input_string == "Python123"):
        return ("access granted")
    else:
        return ("access denied")
    
def calculate_federal_tax(salary):
    if (salary <= 11000):
        return 0.1 * salary
    elif (salary > 11000 and salary <= 44725):
        return 0.12 * salary
    elif (salary > 44725 and salary <= 95375):
        return 0.22 * salary
    else:
        return 0.24 * salary