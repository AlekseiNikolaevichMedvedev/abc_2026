# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().
while True:
    try:
        A = float(input("Enter coefficient A (cannot be 0): "))       
        if A == 0:
            print("Error: Coefficient A cannot be zero. Please try again.\n")
            continue          
        B = float(input("Enter coefficient B: "))        
        x = -B / A
        print(f"Result: x = {x}")
        break    
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.\n")


