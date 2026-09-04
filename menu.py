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
 print("3. View File Types")
 print("4. Organize by extension")
 print("5. Search Files")
 print("6. View Folder Statstics")
 print("7. Exit")

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

def view_files():
  enter_Path = input("Enter path Folder: ")

  base_dir = Path(enter_Path)
  for p in base_dir.iterdir():
    if p.is_file():
      print(f"File_Names: {p.name}" )

def view_filetypes():
   enetr_path = input("Enter Path File: ")

   count_1 = 0
   count_2 = 0
   count_3 = 0
   count_4 = 0
   count_5 = 0
   count_6 = 0

   base_dir = Path(enetr_path)
   for p in base_dir.iterdir():
     if p.suffix == '.jpg':
      count_1 += 1
     elif p.suffix == '.txt':
       count_2 += 1
     elif p.suffix == '.mp3':
       count_3 += 1
     elif p.suffix == '.mp4':
       count_4 += 1
     elif p.suffix == '.exe':
       count_5 += 1
     else:
       count_6 += 1
   print(f"Images: {count_1}")
   print(f"Text: {count_2}")
   print(f"Musics: {count_3}")
   print(f"Videos: {count_4}")
   print(f"Executable: {count_5}")
   print(f"Others: {count_6}")
   
def organize_extension():
  enter_path = input("Ener Folder Path: ")

  base_dir = Path(enter_path)
  for p in base_dir.iterdir():
    if p.is_file():
      s = Path(base_dir / p.suffix)
      s.mkdir(parents=True, exist_ok=True)
      shutil.move(p, base_dir/p.suffix)
      print("Organized Successfully!")

def search_files():
 
  while True:
    enter_path = input("Enter Path")
    name = input("Enter the name of the file: ")
    try: 
      base_dir = Path(enter_path)
      for p in base_dir.iterdir():
        if p.name == name:
          print("File Founded Successfully!")
          break
        else:
          print("File Not Foumd")
    except FileNotFoundError:
      print("File Not Found")

