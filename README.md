# Olympiad Project 🏆

📅 **Date:** December 18, 2023  
👨‍💻 **Author:** Andrii Mikhnevych

This project was created as part of a school Olympiad in programming. The main goal was to design a system that can automatically compile and evaluate source code written in different languages (C++, C#, Pascal), analyze results, and manage submissions in a user-friendly environment.

---

## 🧠 Key Features

- 🔄 **Cross-language support:** Easily compiles C++, C#, and Pascal files.
- 📥 **Submissions basket:** All user submissions are handled through a centralized folder.
- 🧠 **AI-based prompt handling:** Integrates basic prompt processing logic (via `AIprompt.py`).
- 📤 **FTP interaction:** Supports transferring results over FTP.
- 📊 **Result tracking:** Automatically generates `.csv` reports.
- 🖥️ **GUI application:** Simple GUI interface for loading and viewing submissions.

---

## 📁 Folder Structure

```
olimp/
├── main.py               # Entry point of the project
├── compiler.py           # Compilation logic
├── DB.py                 # Result database interactions
├── AIprompt.py           # Prompt evaluation logic
├── fileFTP.py            # FTP file transfer
├── Basket/               # Contains student submissions
│   ├── Etalon.*          # Reference solution in multiple languages
│   └── arguments.txt     # Submission parameters
├── report.csv            # Output results
├── .bat files            # Compile scripts for each language (Windows only)
├── logo.png              # Project logo
```

---

## ▶️ How to Run

> ✅ Recommended OS: **Windows**  
> ✅ Required: **Python 3.9+**

```bash
python main.py
```

> You can also use the included `.bat` files to test compiling C++, C# or Pascal files manually.

---

## 🛠️ Technologies Used

- Python 3.9
- Tkinter GUI
- Batch scripting (.bat)
- Windows OS

---

## 📸 Preview

![logo](logo.png)

---

## 📘 License

This project was created for educational use only during a school competition and is shared as-is for archival and learning purposes.
