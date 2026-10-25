def main():
    while True:
        t = input("Fraction: ")
        try:
            res = convert(t)
            break
        except:
            pass
    
    print(gauge(res))


def convert(fraction):
    try:
        x = int(fraction[0])
        y = int(fraction[2])
        p = (x / y) * 100
    except ValueError:
        return "Input should be positive integer"
    except ZeroDivisionError:
        return "tank capacity cannot be zero"
    return p


def gauge(percentage):
    if percentage > 99:
        return "F"
    
    if percentage < 1:
        return "E"

    ans = str(percentage) + "%"

    return ans


if __name__ == "__main__":
    main()