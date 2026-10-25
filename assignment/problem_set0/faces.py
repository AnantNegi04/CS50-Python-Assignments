def main():
    string = input("What's your mood?\n")
    ans = showEmoji(string)
    print(ans)


def showEmoji(mood):
    happy = "🙂"
    sad = "🙁"

    happyIcon = ":)"
    sadIcon = ":("

    split = mood.split()
    ans = ""
    for str in split:
        if str == happyIcon:
            str = happy
        elif str == sadIcon:
            str = sad

        ans += str

    return ans

main()