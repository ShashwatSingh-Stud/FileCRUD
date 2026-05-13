import streamlit as st
from pathlib import Path
import os

st.title("📂 File Handling CRUD Operations")

# ------------------ Helper Function ------------------

def show_files():
    p = Path(".")
    items = list(p.rglob("*"))

    st.subheader("Available Files & Folders")

    if items:
        for item in items:
            st.write(item)
    else:
        st.write("No files found")


# ------------------ Menu ------------------

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

show_files()

# ------------------ Create File ------------------

if menu == "Create File":

    st.header("Create File")

    file_name = st.text_input("Enter File Name")
    content = st.text_area("Enter File Content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("File Already Exists!")

        else:
            with open(file_name, "w") as file:
                file.write(content)

            st.success("File Created Successfully!")


# ------------------ Read File ------------------

elif menu == "Read File":

    st.header("Read File")

    file_name = st.text_input("Enter File Name")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, "r") as file:
                data = file.read()

            st.text(data)

        else:
            st.error("File Not Found!")


# ------------------ Update File ------------------

elif menu == "Update File":

    st.header("Update File")

    file_name = st.text_input("Enter File Name")

    option = st.radio(
        "Choose Update Option",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter New Content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            if option == "Overwrite":

                with open(file_name, "w") as file:
                    file.write(content)

            else:

                with open(file_name, "a") as file:
                    file.write(content)

            st.success("File Updated Successfully!")

        else:
            st.error("File Does Not Exist!")


# ------------------ Delete File ------------------

elif menu == "Delete File":

    st.header("Delete File")

    file_name = st.text_input("Enter File Name")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(p)

            st.success("File Deleted Successfully!")

        else:
            st.error("File Not Found!")


# ------------------ Rename File ------------------

elif menu == "Rename File":

    st.header("Rename File")

    old_name = st.text_input("Enter Current File Name")
    new_name = st.text_input("Enter New File Name")

    if st.button("Rename File"):

        p = Path(old_name)

        if p.exists():

            p.rename(new_name)

            st.success("File Renamed Successfully!")

        else:
            st.error("File Not Found!")


# ------------------ Create Folder ------------------

elif menu == "Create Folder":

    st.header("Create Folder")

    folder_name = st.text_input("Enter Folder Name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():
            st.error("Folder Already Exists!")

        else:
            p.mkdir()

            st.success("Folder Created Successfully!")


# ------------------ Delete Folder ------------------

elif menu == "Delete Folder":

    st.header("Delete Folder")

    folder_name = st.text_input("Enter Folder Name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            p.rmdir()

            st.success("Folder Deleted Successfully!")

        else:
            st.error("Folder Does Not Exist!")