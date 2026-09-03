from pathlib import Path 

def main_menu():
 print("=" * 30)
 print("")
 print("File Organizer" )
 print()
 print("=" * 30)
 print()
 print("-" * 30)
 print("Main Menu ")
 print("-" * 30)

 print("1. Organize Folder")
 print("2. View Files")
 print("3. View File Catagories")
 print("4. Organize by extension")
 print("5. Search Files")
 print("6. View Folder Statstics")
 try:
    choice = int(input("Enter your choice: "))
    return choice 
 except ValueError:
   print("Enter the required inputs only!")
 except Exception:
   print("Something went Wrong!")


def organizer_folder():

  
   
   enter_path = input("Enter the path of folder you want to organize: ")

   base_dir = Path(enter_path)

   if base_dir.exists():
     if base_dir.is_dir():
       print("Directory founded Successfully!")

   else:
     print("Not Founded!")

