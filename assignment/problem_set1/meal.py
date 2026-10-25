def main():
    time = input("What time is it? ")
    timeStr = convert(time)
    if 7.0 <= timeStr <= 8.0:
        print("breakfast time")
    elif 12.0 <= timeStr <= 13.0:
        print("lunch time")
    elif 18.0 <= timeStr <= 19.0:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hourInt = float(hour)
    minuteInt = float(minute)

    finaltime = hourInt + (minuteInt/60)

    return finaltime


if __name__ == "__main__":
    main()