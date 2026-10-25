def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
#coins = [100, 50, 25]

print(total(**coins), "knuts")


def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

f(100, 50, 25, 150, galleons=100, sickles=50, knuts=25)