# 🔥 BURGERR X AI

A modern, lightweight **Phishing Detection Tool** with a hacker-style UI and rule-based AI engine.
Designed for fast domain analysis, threat detection, and educational cybersecurity usage.

---

## 🧠 About

**BURGERR X AI** is a desktop-based link analysis tool built with Python.
It combines a visually dynamic interface with a heuristic AI engine to detect suspicious and phishing domains.

This tool is designed for:

* Quick link verification
* Cybersecurity learning
* Demonstration of phishing detection logic

---

## ⚙️ Features

* 🧠 AI-based phishing detection (rule-based)
* 🌐 Domain & IP extraction
* 🔍 Suspicious pattern analysis
* 🎯 Whitelist security system
* 🎨 Matrix-style animated UI
* 🌈 RGB glow effects
* ⌨️ Terminal-style live typing output
* 🌍 Dual language support (EN 🇺🇸 / FA 🇮🇷)

---

## 🔐 Whitelisted Domains

The following domains are considered **trusted (SAFE)**:

* iran.gov.ir
* president.ir
* majlis.ir
* mfa.gov.ir
* moi.ir
* irib.ir
* judiciary.ir
* amar.org.ir
* tax.gov.ir

---

## 🧠 AI Detection Logic

The AI engine analyzes domains using:

* Suspicious keywords (login, verify, secure, bank, etc.)
* Domain length anomalies
* Excessive dashes (-)
* IP-based URLs
* Fake subdomain attacks
  (e.g. `mfa.gov.ir.fake.com`)
* Whitelist validation

---

## 📊 Status Types

| Status        | Meaning                   |
| ------------- | ------------------------- |
| ✅ SAFE        | Trusted domain            |
| ⚠️ SUSPICIOUS | Potential risk            |
| ❌ PHISHING    | High probability phishing |
| 🔴 ERROR      | Invalid or unreachable    |

---

## 🚀 Installation & Usage

### 🪟 Windows

1. Download the executable:
   👉 **[Download for Windows](PUT-YOUR-LINK-HERE)**

2. Run:

```bash
burgerr.exe
```

---

### 🐧 Linux

1. Download:
   👉 **[Download for Linux](PUT-YOUR-LINK-HERE)**

2. Make executable:

```bash
chmod +x burgerr
```

3. Run:

```bash
./burgerr
```

---

### 📱 Termux (Android)

1. Install Python:

```bash
pkg install python
```

2. Clone repository:

```bash
git clone YOUR-GITHUB-LINK
cd YOUR-REPO
```

3. Run:

```bash
python parsa2.py
```

---

## 📦 Build from Source

Install dependencies:

```bash
pip install pyinstaller
```

Build executable:

```bash
pyinstaller --onefile --windowed --icon=b.ico parsa2.py
```

---

## ⚠️ Limitations

* No SSL certificate validation
* No real-time threat intelligence APIs
* Rule-based AI (not machine learning)
* No page content scanning

---

## 🎯 Use Cases

* Quick phishing detection
* Cybersecurity education
* Demo/security projects
* UI/UX experimentation

---

## 👨‍💻 Authors

* **Parsa Shahsavari**
* **Mohammad Taha Khalili**

---

## 🧩 Future Improvements

* 🌐 Integration with VirusTotal API
* 🔒 SSL certificate validation
* 🧠 Machine Learning model
* 💀 Advanced hacker UI (glitch / sound effects)

---

## 📜 License

This project is for educational purposes only.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
