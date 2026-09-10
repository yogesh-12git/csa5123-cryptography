<div align="center">

# 🔐 CSA5123 — CRYPTOGRAPHY

### Cryptography Laboratory • Python • Cybersecurity • 40 Practical Experiments

<img src="./assets/cryptography-3d.png" alt="CSA5123 Cryptography" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Cryptography](https://img.shields.io/badge/Cybersecurity-Cryptography-111827?style=for-the-badge&logo=letsencrypt&logoColor=white)](#)
[![Experiments](https://img.shields.io/badge/Experiments-40+-7C3AED?style=for-the-badge)](#-experiment-collection)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![GitHub](https://img.shields.io/badge/GitHub-yogesh--12git-181717?style=for-the-badge&logo=github)](https://github.com/yogesh-12git)

<br/>

**Welcome to the Cryptography Laboratory — Exploring the Science of Secure Communication** 🔐

</div>

---

## 📋 TABLE OF CONTENTS

- [About the Project](#-about-the-project)
- [Project Objectives](#-project-objectives)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Experiment Collection](#-experiment-collection)
- [Technology Stack](#-technology-stack)
- [Key Concepts](#-key-concepts)
- [Learning Path](#-learning-path)
- [Skills Developed](#-skills-developed)
- [Real-World Applications](#-real-world-applications)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🧠 ABOUT THE PROJECT

**CSA5123 — Cryptography** is a comprehensive practical academic repository focusing on understanding fundamental cryptographic concepts, algorithms, and programming techniques used to protect information.

This repository contains a collection of **40 Python-based cryptography experiments** covering:

- 🔑 **Encryption & Decryption** — Transform and restore data securely
- 🧮 **Mathematical Foundations** — Modular arithmetic, number theory, prime concepts
- 🔐 **Classical Techniques** — Caesar cipher, substitution, Vigenère, and more
- 🛡️ **Security Concepts** — Confidentiality, integrity, and authentication principles
- 🔢 **Key-Based Security** — Understanding symmetric and asymmetric cryptography
- 💻 **Algorithm Implementation** — Hands-on Python implementations
- 🧪 **Practical Experiments** — 40 independent, executable programs

### 🎯 Core Philosophy

Move beyond theoretical concepts and understand **how cryptographic algorithms work through implementation**. Each experiment is designed to be studied and executed independently.

---

## 🎯 PROJECT OBJECTIVES

```
┌──────────────────────────────────────────────────────────────┐
│              CRYPTOGRAPHY LEARNING OBJECTIVES                │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ✓ Understand encryption and decryption mechanisms           │
│  ✓ Learn mathematical foundations of cryptography            │
│  ✓ Implement cryptographic algorithms using Python           │
│  ✓ Explore symmetric and asymmetric key systems              │
│  ✓ Understand confidentiality, integrity & authentication    │
│  ✓ Develop practical cybersecurity programming skills        │
│  ✓ Strengthen algorithmic thinking and problem-solving       │
│  ✓ Gain hands-on experience with cryptographic concepts      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 🚀 QUICK START

### Prerequisites
- Python 3.6 or higher
- Basic understanding of Python programming
- A terminal or command-line interface

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yogesh-12git/csa5123-cryptography.git
cd csa5123-cryptography
```

### 2️⃣ Verify Python Installation

```bash
python --version
# or
python3 --version
```

### 3️⃣ Run Your First Experiment

```bash
# Run Experiment 1
python "EXP 1.py"

# Or try another experiment
python "EXP 10.py"
```

### 📝 Note
Keep filenames in quotation marks if they contain spaces or special characters.

---

## 💻 INSTALLATION

### Standard Setup

```bash
# Clone the repository
git clone https://github.com/yogesh-12git/csa5123-cryptography.git

# Navigate to directory
cd csa5123-cryptography

# Verify Python 3.x is installed
python --version
```

### (Optional) Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Deactivate when done
deactivate
```

### No External Dependencies Required
Most experiments use only Python's standard library. Some experiments may use:
- `cryptography` — For advanced cryptographic operations
- `hashlib` — For hashing algorithms (included in standard library)

---

## 📂 PROJECT STRUCTURE

```
csa5123-cryptography/
│
├── assets/
│   ├── cryptography-3d.png          # Project banner image
│   └── [Additional resources]
│
├── EXP 1.py  through  EXP 40.py     # 40 Cryptography Experiments
│
├── README.md                         # This file
├── .gitignore                        # Git ignore rules
└── LICENSE                           # MIT License

🔍 Experiment Naming Convention:
   EXP 1.py, EXP 2.py, ..., EXP 40.py
   Some experiments have subtasks: EXP 14.1.py, EXP 14.2.py
```

---

## 🧪 EXPERIMENT COLLECTION

### Complete List of 40 Experiments

The repository includes **40 comprehensive experiments** covering cryptographic algorithms and techniques:

| # | Experiment | Focus Area |
|---|---|---|
| 1-5 | Classical Ciphers | Caesar, ROT13, Substitution |
| 6-10 | Encryption Techniques | Vigenère, Playfair, Columnar |
| 11-15 | Mathematical Concepts | Modular Arithmetic, GCD, Primes |
| 16-20 | Key Generation | Random Keys, Key Derivation |
| 21-25 | Hash Functions | MD5, SHA-1, SHA-256 Concepts |
| 26-30 | Modern Encryption | DES, 3DES Concepts, Block Ciphers |
| 31-35 | Public Key Cryptography | RSA Concepts, Key Pairs |
| 36-40 | Advanced Topics | Digital Signatures, Certificate Basics |

### Run Any Experiment

```bash
# Single experiment
python "EXP 1.py"

# Batch run (example script)
for i in {1..40}; do python "EXP $i.py"; done
```

### Experiment Execution Flow

```
┌──────────────────────────┐
│   SELECT EXPERIMENT      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   READ PYTHON CODE       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  PROVIDE INPUT / KEY     │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   RUN ALGORITHM          │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   VIEW OUTPUT RESULTS    │
└──────────────────────────┘
```

---

## ⚙️ TECHNOLOGY STACK

| Technology | Purpose | Details |
|---|---|---|
| 🐍 **Python 3.x** | Core Language | Algorithm implementation, scripting |
| 🔐 **Cryptography** | Security Concepts | Encryption, decryption, key systems |
| 📊 **Mathematics** | Foundations | Modular arithmetic, number theory |
| 💻 **Git & GitHub** | Version Control | Repository management, collaboration |
| 🧮 **Standard Library** | Built-in Tools | hashlib, secrets, random modules |

---

## 🧩 KEY CONCEPTS

### 🔒 Encryption
Encryption transforms readable information into a protected form that cannot be understood without the correct key.

```
PLAINTEXT → [Encryption Algorithm + Key] → CIPHERTEXT
```

### 🔓 Decryption
Decryption converts protected information back into its original readable form.

```
CIPHERTEXT → [Decryption Algorithm + Key] → PLAINTEXT
```

### 🔑 Cryptographic Keys
A cryptographic key is information used by an algorithm to control the transformation of data.

```
                  CRYPTOGRAPHIC KEYS
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
        SYMMETRIC KEYS           ASYMMETRIC KEYS
             │                       │
        Same Key Used           Public + Private Keys
        for Enc/Dec            for Different Operations
```

### 🧠 Cryptographic Workflow

```
PLAINTEXT
    ↓
[Cryptographic Algorithm]
    ↓
[+] ENCRYPTION KEY
    ↓
CIPHERTEXT
    ↓
[Cryptographic Algorithm]
    ↓
[+] DECRYPTION KEY
    ↓
PLAINTEXT (Original)
```

---

## 📈 LEARNING PATH

```
START HERE ─────────────────────────────────────────────────→ MASTER

    ↓
    🔹 Cryptography Fundamentals
    ↓
    🔹 Mathematical Basics (Modular Arithmetic, Primes)
    ↓
    🔹 Classical Ciphers (Caesar, Vigenère, Substitution)
    ↓
    🔹 Encryption & Decryption Techniques
    ↓
    🔹 Key Generation & Management
    ↓
    🔹 Hash Functions & Integrity
    ↓
    🔹 Symmetric Cryptography (DES, 3DES)
    ↓
    🔹 Asymmetric Cryptography (RSA, Public Key)
    ↓
    🔹 Digital Signatures & Certificates
    ↓
    🚀 ADVANCED CRYPTOGRAPHY MASTERY
```

---

## 💡 HANDS-ON LEARNING

Each experiment includes:

✅ **Clear Python Implementation** — Direct, understandable code  
✅ **Input/Output Examples** — Sample execution and results  
✅ **Algorithm Explanation** — How and why it works  
✅ **Security Perspective** — Real-world context and applications  
✅ **Independent Execution** — Study each experiment separately  

### Example: Caesar Cipher (EXP 1)

```
INPUT:  Message = "HELLO", Shift = 3
PROCESS: H→K, E→H, L→O, L→O, O→R
OUTPUT: "KHOOR"

DECRYPTION: Reverse the shift by 3
OUTPUT: "HELLO" ✓
```

---

## 🛡️ SECURITY PERSPECTIVE

The experiments provide a foundation for understanding how secure communication systems are designed:

```
                 CYBERSECURITY
                       │
      ┌────────────────┼────────────────┐
      │                │                │
      ▼                ▼                ▼
CONFIDENTIALITY    INTEGRITY       AUTHENTICATION
 (Keep Secret)  (Verify Genuine)   (Verify Identity)
      │                │                │
      └────────────────┼────────────────┘
                       │
                       ▼
                 CRYPTOGRAPHY
                       │
                       ▼
              SECURE COMMUNICATION
```

---

## 📊 SKILLS DEVELOPED

### 💻 Programming Skills
- Python algorithm implementation
- Efficient code writing
- Input/output handling
- Debugging and testing
- Problem-solving techniques

### 🔐 Cybersecurity Knowledge
- Cryptographic concepts and terminology
- Encryption and decryption principles
- Security design patterns
- Key management concepts
- Secure communication protocols

### 🧠 Computer Science Fundamentals
- Algorithm analysis and design
- Mathematical reasoning
- Modular arithmetic mastery
- Computational thinking
- Logical problem-solving

### 🛠️ Professional Development
- Git and GitHub proficiency
- Repository management
- Technical documentation
- Code organization
- Version control best practices

---

## 🌐 REAL-WORLD APPLICATIONS

Cryptography is used in many technologies we interact with daily:

```
                     CRYPTOGRAPHY
                          │
         ┌────────────────┼────────────────┐
         │                │                │
         ▼                ▼                ▼
       HTTPS          BANKING           MESSAGING
         │                │                │
         ▼                ▼                ▼
   Websites         Transactions      Private Data
         │                │                │
         └────────────────┼────────────────┘
                          │
                          ▼
                   DIGITAL SECURITY
```

### Use Cases

🌐 **HTTPS/TLS** — Secure website connections  
💳 **Online Banking** — Secure financial transactions  
🏦 **Digital Payments** — Credit card and payment security  
📱 **Messaging Apps** — End-to-end encrypted communications  
🔐 **Password Protection** — Secure authentication systems  
☁️ **Cloud Security** — Data protection in cloud storage  
🖥️ **System Authentication** — Device and user verification  
📧 **Email Encryption** — Secure email communications  
🪪 **Digital Identity** — Blockchain and digital certificates  
✍️ **Digital Signatures** — Document authenticity and non-repudiation  

---

## 🚀 FUTURE ENHANCEMENTS

This repository can be expanded with:

```
┌──────────────────────────────────────────────────────┐
│            PLANNED ENHANCEMENTS                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  ▶ Detailed documentation for every experiment      │
│  ▶ Algorithm flowcharts and visualizations          │
│  ▶ Sample input/output examples                     │
│  ▶ Complexity analysis (Time & Space)               │
│  ▶ Modern cryptographic demonstrations              │
│  ▶ Interactive cryptography tools                   │
│  ▶ Automated unit tests for all experiments         │
│  ▶ Security-focused detailed documentation          │
│  ▶ Performance benchmarking tools                   │
│  ▶ Visual algorithm animations                      │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🤝 CONTRIBUTING

Contributions are welcome! Here's how you can help:

### Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/improvement`)
3. **Make** your changes with clear commit messages
4. **Test** your code thoroughly
5. **Push** to your branch (`git push origin feature/improvement`)
6. **Submit** a Pull Request with a detailed description

### Contribution Areas

- 🐛 Bug fixes and improvements
- 📖 Documentation enhancements
- 🧪 Additional experiments
- ⚡ Performance optimizations
- 🎨 Code quality improvements

---

## 📄 LICENSE

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

**You are free to:**
- Use this project for personal and commercial purposes
- Modify and distribute the code
- Include it in your own projects

**With the condition:**
- Include a copy of the license and copyright notice

---

## 👨‍💻 AUTHOR

<div align="center">

### **YOGESH S.**

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                      👨‍💻 YOGESH S.                           ║
║                                                              ║
║            B.Tech Information Technology Student             ║
║                                                              ║
║            💻 Full-Stack Developer                           ║
║            🐍 Python Developer                               ║
║            🔐 Cybersecurity & Cryptography Enthusiast        ║
║            🤖 AI & Technology Enthusiast                     ║
║                                                              ║
║            ─────────────────────────────────────────         ║
║                                                              ║
║            LEARN  •  BUILD  •  SECURE  •  INNOVATE           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-yogesh--12git-181717?style=for-the-badge&logo=github)](https://github.com/yogesh-12git)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Yogesh%20S.-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/yogesh-subramanian-b65935315/)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail)](mailto:your.email@example.com)

</div>

---

## 📞 SUPPORT & FEEDBACK

Have questions or feedback? Here's how to reach out:

- **Issues** — Report bugs or suggest features via [GitHub Issues](https://github.com/yogesh-12git/csa5123-cryptography/issues)
- **Discussions** — Join conversations in [GitHub Discussions](https://github.com/yogesh-12git/csa5123-cryptography/discussions)
- **Email** — Direct inquiries to the author
- **Star** — If you find this helpful, please star ⭐ the repository!

---

<div align="center">

### Made with ❤️ for the Cryptography Community

**Explore • Learn • Secure • Innovate**

![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python)
![Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red?style=flat-square)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green?style=flat-square)

</div>
