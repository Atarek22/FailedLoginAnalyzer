# FailedLoginAnalyzer 🔍

A simple, beginner-friendly Python tool to parse `auth.log` files and detect failed SSH login attempts.

---

## 📦 Repo structure

```
FailedLoginAnalyzer/
├── auth.log.sample
├── analyze_log.py
├── results.csv (generated)
└── README.md
```

---

## 🎯 Goal

Detect failed SSH login attempts from `auth.log`-style files, count occurrences per username and per IP, and export a CSV report for quick review. Great for SOC/log-analysis practice. 🛡️

---

## 🧪 Prerequisites

* Python 3.x installed
* Basic terminal knowledge
* (Optional) Virtual environment for Python

---

## 🚧 Step-by-step build & screenshots

If you want to creat it by yourself,Follow these steps. 

### 1. ✍️ Create the sample log file

Create `auth.log.sample` and add a few lines that simulate failed and successful SSH logins.

<img width="1103" height="256" alt="Capture d&#39;écran 2025-11-06 221633" src="https://github.com/user-attachments/assets/8f773585-7bd6-4aef-8e67-ea9253e31ae6" />


### 2. 🧾 Add the analyzer script (`analyze_log.py`)

<img width="890" height="378" alt="Capture d&#39;écran 2025-11-06 223612" src="https://github.com/user-attachments/assets/5df1624b-d7ae-41b8-8366-166a9bd28428" />


### 3. 🔐 Make the script executable (optional)

<img width="890" height="378" alt="Capture d&#39;écran 2025-11-06 223612" src="https://github.com/user-attachments/assets/c2a91dd5-b2e7-439a-a1d8-c650ab4dd3f2" />


### 4. ▶️ Run the analyzer and inspect output

<img width="890" height="378" alt="Capture d&#39;écran 2025-11-06 223612" src="https://github.com/user-attachments/assets/f1d77bb9-3598-4744-a02d-85508828df9a" />


### 5. 📁 Verify the generated CSV in the folder

Open the repository folder to confirm `results.csv` is created and contains the counts.

<img width="651" height="248" alt="Capture d&#39;écran 2025-11-06 223622" src="https://github.com/user-attachments/assets/9904e0dc-9b16-4816-8619-faa2dbf65417" />
