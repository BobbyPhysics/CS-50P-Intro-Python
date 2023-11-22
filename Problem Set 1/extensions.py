# In a file called extensions.py, implement a program that prompts the user for the name of a file 
# and then outputs that file’s media type if the file’s name ends, case-insensitively, in an inlcuded suffix

#.gif = image/gif
#.jpg = image/jpeg
#.jpeg = image/jpeg
#.png = image/png
#.pdf = application/pdf
#.txt = text/plain
#.zip = application/zip

def main():
    file = input("What's your file name?")
    file = file.casefold().strip()

    if file[file.rfind("."):] == ".gif" or file[file.rfind("."):] == ".png":
        print("image/",file[((file.rfind("."))+1):], sep='')
    elif file[file.rfind("."):] == ".jpg" or file[file.rfind("."):] == ".jpeg":
        print("image/jpeg")
    elif file[file.rfind("."):] == ".pdf" or file[file.rfind("."):] == ".zip":
        print("application/",file[((file.rfind("."))+1):], sep='')
    elif file[file.rfind("."):] == ".txt":
        print("text/plain")
    else:
        print("application/octet-stream")

main()