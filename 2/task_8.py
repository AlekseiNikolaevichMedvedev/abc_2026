# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".
def is_palindrome(n):
    s = str(abs(n))
    return s == s[::-1]


while True:
    try:
        x=int(input('Input the number to check: '))
    except ValueError:
        print(f"Try again.\n")
    break
print(f"Result is {is_palindrome(x)}")