# 📁 File Organizer

A Python-based File Organizer that automatically organizes files into appropriate folders based on their file types and extensions.

The application helps users clean up messy directories by scanning files, identifying their extensions, creating category folders, and moving files into their corresponding locations.

This project focuses on learning Python filesystem automation and working with files and directories using modules such as `pathlib` and `shutil`.

---

## ✨ Features

### 📂 File Organization

* Scan files inside a selected directory
* Identify file names and extensions
* Automatically categorize files
* Create category folders when needed
* Move files into their appropriate folders
* Handle unknown file types

### 🗂️ File Categories

Files can be organized into categories such as:

* 🖼️ Images
* 📄 Documents
* 🎵 Music
* 🎬 Videos
* 📦 Archives
* 💻 Code Files
* 📁 Other Files

### 🔍 File Management

* View files inside a directory
* View file extensions
* Search for files
* Organize files by category
* Prevent duplicate file conflicts

### 📊 Folder Statistics

* Total number of files
* Number of files in each category
* File type distribution
* Total folder size

---

## 🛠️ Technologies Used

* Python 3
* `pathlib`
* `shutil`
* `os`

---

## 📂 Project Structure

```text
file-organizer/
│
├── main.py
├── menu.py
├── organizer.py
├── categories.py
├── utils.py
│
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

The program follows a simple workflow:

```text
Select Folder
      │
      ▼
Scan Directory
      │
      ▼
Identify Files
      │
      ▼
Check File Extension
      │
      ▼
Determine Category
      │
      ▼
Create Category Folder
      │
      ▼
Move File
      │
      ▼
Display Summary
```

For example, a folder containing:

```text
Downloads/
│
├── photo.jpg
├── document.pdf
├── song.mp3
├── video.mp4
├── project.zip
└── script.py
```

Can be organized into:

```text
Downloads/
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── document.pdf
│
├── Music/
│   └── song.mp3
│
├── Videos/
│   └── video.mp4
│
├── Archives/
│   └── project.zip
│
└── Code/
    └── script.py
```

---

## 📚 Concepts Practiced

This project is designed to strengthen practical knowledge of:

* File System Operations
* Path Handling
* File Extensions
* Directories and Folders
* Python Automation
* Exception Handling
* Modular Programming
* Dictionaries
* Functions
* File Manipulation
* Operating System Interaction

---

## 🚀 Future Improvements

Potential improvements for future versions include:

* Recursive folder organization
* Undo previous organization
* Custom file categories
* Duplicate file detection
* File size filtering
* Automatic scheduled organization
* Logging system
* GUI version
* Drag and drop support
* Configuration file for custom extensions
* Preview changes before organizing files

---

## ⚠️ Safety Note

Because this application moves files on the computer, it is recommended to test the program on a sample folder before using it on important directories.

---

## 🎯 Learning Objectives

This project was created to practice:

* Automating real-world tasks with Python
* Working with files and directories
* Understanding file paths
* Using the `pathlib` module
* Using the `shutil` module
* Building practical automation tools
* Writing clean and modular Python applications

---

## 👨‍💻 Author

**Kidus Yonas**

Computer Science Student | Python Developer | Aspiring AI Engineer

If you found this project helpful or interesting, feel free to ⭐ the repository.
