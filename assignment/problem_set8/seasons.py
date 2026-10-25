from datetime import date, datetime
import time, sys, inflect

def main():
    try:
        dob = input("What's your date of birth? ")
        d = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid Date format")

    minutes = get_minutes(d)
    
    print(number_to_words(minutes))
    

def get_minutes(dob: date) -> int:
    today = date.today()
    delta = today - dob
    minutes = delta.days * 60 * 24
    return minutes

def number_to_words(num: int):
    p = inflect.engine()
    word = p.number_to_words(num, andword="")
    word = word.split(",")
    ans = ""
    for i in word:
        ans += i
    return ans.strip()

"""
def number_to_words(n: int) -> str:
    #Convert a number to English words (up to ~1,000,000,000).
    if n == 0:
        return "zero"

    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    scales = ["", "thousand", "million", "billion"]

    def helper(num: int) -> str:
        if num < 20:
            return ones[num]
        if num < 100:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 else "")
        return ones[num // 100] + " hundred" + (" " + helper(num % 100) if num % 100 else "")

    if n == 0:
        return "zero"

    parts = []
    scale_idx = 0
    while n > 0:
        chunk = n % 1000
        if chunk != 0:
            word = helper(chunk)
            if scales[scale_idx]:
                word += " " + scales[scale_idx]
            parts.insert(0, word)
        n //= 1000
        scale_idx += 1

    return " ".join(parts)
"""       

if __name__ == "__main__":
    main()