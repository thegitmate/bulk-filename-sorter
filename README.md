# bulk-filename-sorter (macOs)
A simple, fast, and safe Python CLI mini tool for macOS that searches files by keyword in filename and automatically moves matching files into a dedicated folder.  Perfect for cleaning messy folders full of photos, PDFs, videos, downloads, or mixed file types.

Python script to replace Finder "Name contains" search for sorting files by name in bulk. Tested and works better than Finder. Finder search is often unable to find every file which names contains the keyword. This mini tool solves this issue. 

---

## ✨ Features

- 📁 Search inside any folder (supports names with spaces)
- 🔎 Finds files by **partial keyword match** in filenames  
  - Example: `shed` → `unsmushed-image.jpg`, `thebigshed.pdf`, `mashedpotato.png`
- 🧠 Case-insensitive search
- 🗂 Automatically creates a destination subfolder of keyword name
- 🔁 Avoids overwriting files (adds `(1)`, `(2)`, etc.)
- 🚫 Skips its own script file
- ⚡ Works with **all file types**
- 🍎 Designed for **macOS**, but technically compatible with Linux

---

## 📦 How It Works
1. You run the script from the terminal or IDLE
2. It asks:
   - Which folder to scan
   - What keyword to search for
3. It scans **all subfolders recursively**
4. Every matching file is **moved** into a newly created folder named after the keyword

---

## 🛠 Installation

### Requirements
- macOS
- Python **3.8+** (comes preinstalled on most macOS versions)

Check your Python version:
```bash
python3 --version
```

## Clone the repository
```bash
git clone https://github.com/yourusername/smart-file-finder.git
cd smart-file-finder
```

## ⚠️ Important Notes
- Files are moved, not copied
- A folder named after your keyword is created automatically
- If a folder already exists, _2, _3, etc. will be appended
- If filenames collide, (1), (2) will be added safely

## 🔐 Safety & Best Practices
- Test on a small folder first
- Keep backups if working with important files
- The script will avoid overwriting any file

## 🤝 Contributing
- Fork the repository
- Create a feature branch
- Submit a pull request
- Please keep the code clean and well-documented.

## 📄 License
MIT License — free to use, modify, and distribute.
Because file organization should be simple, fast, and accessible to everyone.

### If this mini-tool helped you, consider starring ⭐ the repo.
