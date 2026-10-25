def main():
    expression = input("Expression: ")
    answer = math(expression)
    print(f"{answer:.1f}")

def math(expression):
    exp = expression.split()
    x = int(exp[0])
    y = exp[1]
    z = int(exp[2])

    if y == "+":
        return x + z
    if y == "*":
        return x * z
    if y == "-":
        return x - z
    if y == "/":
        if z == 0:
            return 0
        else:
            return x / z

main()