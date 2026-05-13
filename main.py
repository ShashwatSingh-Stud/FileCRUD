# Project - CRUD Operations
import os
from pathlib import Path
def readfileandfolder():
    try:
        p = Path("")
        items = list(p.rglob("*"))
        for index , file in enumerate(items):
            print(f"{index + 1} - {file}")
    except Exception as e:
        print(e)

def create_file():
    try:
        readfileandfolder()
        file_name = input("Enter Name of Your File :- ")
        p = Path(file_name)
        if p.exists():
            print("FILE ALREADY EXISTS")
        else:
            with open(file_name , "w") as file:
                content = input("Enter Your File content: ")
                file.write(content)
                print("FILE ADDED ! ")
    except Exception as e:
        print(e)
    
    
         
    


def read_file():
    try:
        readfileandfolder()
        file_name = input("Enter Your File Name : ")
        p = Path(file_name)
        if p.exists():
            with open(file_name , "r") as file:
                print(file.read())
        else:
            print("FILE NOT FOUND! ")
    except Exception as e:
        print(e)
    


def update_file():
    try:
        readfileandfolder()
        file_name = input("Enter Name of Your File :- ")
        p = Path(file_name)
        if p.exists():
            print("Press 1 to Overwrite the Content")
            print("Press 2 To Append New Content")

            option = int(input("Enter Your Choice For Updating a File : "))
            if option == 1:
                with open(file_name , "w") as file:
                    content = input("Enter Your Content : ")
                    file.write(content)
                    print("CONTENT CHANGED... ")
            elif option == 2:
                with open(file_name , "a") as file:
                    content = input("Enter Your Content : ")
                    file.write(content)
                    print("CONTENT CHANGED... ")
            else:
                print("INVALID INPUT")
        else:
            print("FILE DOES NOT EXISTS")
    except Exception as e:
        print(e)

def delete_file():
    try:
        readfileandfolder()
        file_name = input("Enter Name of Your File :- ")
        p = Path(file_name)
        if p.exists():
            os.remove(p)
            print("FILE DELETED")
        else:
            print("FILE DOES NOT EXISTS !!")
    except Exception as e:
        print(e)
    

def rename_file():
    readfileandfolder()
    file_name = input("Enter name of your File :")
    p = Path(file_name)
    if p.exists():
        new_file = input("Enter new Name of Your File :")
        p.rename(new_file)
        print("FILE RENAMED !")
    else:
        print("FILE NOT FOUND ! ")

def create_folder():
    readfileandfolder()
    folder_name = input("Enter Name of Your Folder: ")
    p = Path(folder_name)
    if p.exists():
        print("Folder already Exists! ")
    else:
        p.mkdir()
        print("FOLDER CREATED ! ")

def delete_folder():
    readfileandfolder()
    folder_name = input("Enter Name of Your Folder: ")
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        print("FOLDER REMOVED ! ")
    else:
        print("FOLDER DOES NOT EXISTS ! ")
        

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")
print("Press 5 for Renaming a file")
print("Press 6 for Creating a folder")
print("Press 7 for deleting a folder")
print("Press 0 for Exiting... ")




while True:
    option = int(input("Enter your choice: "))
    if option == 1:
        create_file()
    if option == 2:
        read_file()
    if option == 3:
        update_file()
    if option == 4:
        delete_file()
    if option == 5:
        rename_file()
    if option == 6:
        create_folder()
    if option == 7:
        delete_folder()
    if option == 0:
        break