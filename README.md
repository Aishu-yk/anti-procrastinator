# 🧠 Anti-Procrastinator – Focus Timer & Website Blocker

A simple, beginner-friendly productivity tool that helps you **stay focused and avoid distractions** by blocking distracting websites during your focus sessions.

> 🚫 No AI, No distractions. Just pure logic + motivation.

---

## ✨ Features

- ⏲️ Start a custom focus timer (like Pomodoro)
- 🔒 Blocks distracting websites (e.g., YouTube, Instagram)
- 🧠 Clean GUI using Tkinter
- 🔔 Automatically unblocks sites after the session
- 💻 Beginner-friendly Python code

---

## 📸 Preview

> ![screenshot](screenshot.png)  
> _Simple interface to boost your focus!_

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tkinter** (for GUI)
- **Built-in libraries:** `time`, `threading`, `platform`, `tkinter`

---

## 🚀 How It Works

- Modifies the system's `hosts` file to redirect listed sites to `127.0.0.1`, effectively blocking them.
- Once the timer ends, it removes those redirects, unblocking the sites.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/anti-procrastinator.git
cd anti-procrastinator
