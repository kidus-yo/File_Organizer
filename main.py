from menu import *

def main():
    choice = main_menu()
    running = True

    while running:
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
            view_filetypes()

        elif choice == 4:
            print("Welcome to organize file by extension")
            print("-" * 30)
            organize_extension()

        elif choice == 5:
            print("Welcome to Search Files")
            print("-" * 30)
            search_files()

        elif choice == 6:
            print("Welcome to View Statstics📊")
            print("-" * 30)
            folder_statstics()
        elif choice == 7:
            running = False
            print("Thanks for Organizing your files and Folders")
            break



if __name__ == "__main__":
    main()