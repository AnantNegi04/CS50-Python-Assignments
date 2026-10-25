import re

email = input("What's your email? ").strip()

if re.search("^\w+(\.\w+)?@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")