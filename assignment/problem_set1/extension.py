def main():
    userInput = input("flie name: ")
    answer = extensions(userInput)
    print(answer)

def extensions(name):
    if name.endswith(".gif") or name.endswith(".GIF"):
        return "image/gif"
    elif name.endswith(".jpg") or name.endswith(".JPG"):
        return "image/jpg"
    elif name.endswith(".jpeg") or name.endswith(".JPEG"):
        return "image/jpeg"
    elif name.endswith(".pdf") or name.endswith(".PDF"):
        return "application/pdf"
    elif name.endswith(".png") or name.endswith(".PNG"):
        return "image.png"
    elif name.endswith(".txt") or name.endswith(".TXT"):
        return "text/plain"
    elif name.endswith(".zip") or name.endswith(".ZIP"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()