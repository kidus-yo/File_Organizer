from menu import *

def main():
    choice = main_menu()
    if choice == 1:
        print("Welcome to File Organizer")
        print("-"  * 30)
        organizer_folder()

    elif choice == 2:
        print("Welcome to View Files")
        print("-" * 30)
        view_files()

    elif choice == 3:
        print("Welcome to view file catagories")
        print("-" * 30)
        view_catagories()

if __name__ == "__main__":
    main()