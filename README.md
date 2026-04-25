# 🚀 ISS Overhead Notifier (Python - API + SMTP)

A Python automation script that tracks the International Space Station (ISS) in real-time and sends an email alert when it is above your location at night.

---

## How it works:-

* 🌍 Uses real-time ISS location API
* 🌙 Checks if it is night at your location
* 📡 Combines multiple APIs
* ✉️ Sends instant email alerts
* ⚡ Runs continuously (automation-ready)

---

## Update your details in `main.py`:

   ```python
   MY_LAT = your_latitude
   MY_LONG = your_longitude
   email = "your_email@gmail.com"
   app_password = "your_app_password"
   ```

---

## 🔐 Gmail Setup

1. Enable **2-Step Verification**
2. Generate **App Password**
3. Use it in the script

---

## ☁️ Run Automatically (PythonAnywhere)

Run this script 24/7 without keeping your PC ON.

### Steps:

1. Create account → https://www.pythonanywhere.com
2. Upload your project
3. Go to **Tasks → Scheduled Tasks**
4. Add command:

```id="k9z2xp"
python3 /home/yourusername/iss-notifier/main.py
```

5. Set it to run every few minutes

⚠️ Note: Since the script already loops every 60 seconds, you can also:

* Run it once (always running task), OR
* Modify it to run once and schedule every 1–5 minutes
