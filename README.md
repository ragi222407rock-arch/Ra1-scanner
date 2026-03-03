# 🔎 RA1 Scanner

RA1 Scanner is a beginner-friendly automated vulnerability scanning tool built using Python.
It integrates Nmap and Nikto to perform port scanning and basic web vulnerability detection, and generates structured reports.

---

## 🚀 Features

* 🔍 Port scanning using Nmap
* 🌐 Web vulnerability scanning using Nikto
* 📄 Automated report generation (TXT & PDF)
* 🖥 Simple CLI-based interface
* 🛡 Designed for learning and authorized testing

---

## 🛠 Tech Stack

* Python 3
* Nmap
* Nikto
* FPDF (for PDF report generation)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ra1-scanner.git
cd ra1-scanner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure Nmap and Nikto are installed in your system.

---

## ⚡ Usage

Run the tool:

```bash
python3 vuln_scanner.py
```

Enter the target IP address or domain when prompted.

Example:

```
Enter target (IP or domain): scanme.nmap.org
```

Reports will be saved inside the project directory.

---

## 📁 Project Structure

```
ra1-scanner/
│
├── vuln_scanner.py
├── scanner.py
├── report_generator.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🎯 Purpose

This project was created as part of cybersecurity learning to understand:

* Network scanning
* Web vulnerability detection
* Automation using Python
* Report generation for penetration testing

---

## ⚠ Disclaimer

This tool is created strictly for educational and authorized penetration testing purposes only.

Do NOT use this tool against systems without proper permission.
The developer is not responsible for any misuse.

---

## 👨‍💻 Author

Rahul Singh
Cybersecurity Enthusiast
Kali Linux | Python | Ethical Hacking
