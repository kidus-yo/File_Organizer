from pathlib import Path
import shutil 

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
   for p in base_dir.iterdir():
    
      if p.is_file():
       if p.suffix == '.png' or p.suffix == '.jpg':
         s = Path(base_dir / "images")
         s.mkdir(parents=True, exist_ok=True)
         shutil.move(p, base_dir / "images")
         print("Organized Successfully✅")

       elif p.suffix == '.txt':
         s = Path(base_dir / "Text")
         s.mkdir(parents=True, exist_ok=True)
         shutil.move(p, base_dir / "Text")
         print("Organized Successfully")

       elif p.suffix == '.mp3':
         s = Path(base_dir / "Musics")
         s.mkdir(parents=True, exist_ok=True)
         shutil.move(p, base_dir / "Musics")
         print("Organized Successfully!")

       elif p.suffix == ".exe":
         s = Path(base_dir / "Executable")
         s.mkdir(parents=True, exist_ok=True)
         shutil.move(p, base_dir / "Executable")
         print("Organized Successful!✅")

       elif p.suffix == ".mp4" or p.suffix == ".mov":
         s = Path(base_dir / "Videos")
         s.mkdir(parents=True, exist_ok=True)
         shutil.move(p, base_dir / "Videos")
         print("Organized Successful✅")
       else:
          print("File Not Supported")

