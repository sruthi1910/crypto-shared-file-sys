
#This is the main function for the file-split cryptography


from split import split, recreate_file
import os
import pyfiglet


def main():
    result = pyfiglet.figlet_format("FILE SHARDER", font = "slant" )
    print(result)
    print("Welcome to the file-split cryptography")
    filename = str(input("Enter the filepath : "))
    if filename == "":
        print("Please enter the name of the file : ")
    
    pwd = str(input("Enter the password: "))
    mode = str(input("Enter the mode for the file operation (read/create): "))
    if mode == "read":
        recreate_file(filename, pwd)
    elif mode == "create":
        split(filename,pwd,1)
    else:
        print("Wrong Option. Try again !")
    


if __name__ == "__main__":
    main()
