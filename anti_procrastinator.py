import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread
from datetime import datetime as dt
import os
import platform

# === CONFIG ===
WEBSITES_TO_BLOCK = [
    "www.youtube.com", "youtube.com",
    "www.instagram.com", "instagram.com",
    "www.facebook.com", "facebook.com"
]

# OS-specific hosts file path
if platform.system() == "Windows":
    HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
else:
    HOSTS_PATH = "/etc/hosts"

REDIRECT = "127.0.0.1"

# === CORE FUNCTIONS ===
def block_websites():
    try:
        with open(HOSTS_PATH, 'r+') as file:
            content = file.read()
            for site in WEBSITES_TO_BLOCK:
                if site not in content:
                    file.write(f"{REDIRECT} {site}\n")
    except PermissionError:
        messagebox.showerror("Permission Denied", "Run the script as Administrator (Windows) or with sudo (Linux/Mac).")

def unblock_websites():
    try:
        with open(HOSTS_PATH, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(site in line for site in WEBSITES_TO_BLOCK):
                    file.write(line)
            file.truncate()
    except PermissionError:
        messagebox.showerror("Permission Denied", "Run the script as Administrator (Windows) or with sudo (Linux/Mac).")

def start_focus(duration):
    block_websites()
    countdown_thread = Thread(target=countdown, args=(duration,))
    countdown_thread.start()

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        seconds -= 1

    unblock_websites()
    timer_label.config(text="00:00")
    messagebox.showinfo("Session Complete", "Time's up! Websites are now unblocked.")

# === GUI ===
def start_session():
    try:
        minutes = int(entry.get())
        if minutes <= 0:
            raise ValueError
        start_focus(minutes)
        messagebox.showinfo("Focus Mode", f"Blocking distractions for {minutes} minutes!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

# GUI Setup
root = tk.Tk()
root.title("🧠 Anti-Procrastinator")
root.geometry("350x200")
root.config(bg="#fefae0")

tk.Label(root, text="Enter Focus Time (mins):", font=("Arial", 12), bg="#fefae0").pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
entry.pack()

tk.Button(root, text="Start Focus Session", font=("Arial", 12), bg="#90be6d", fg="white", command=start_session).pack(pady=10)

timer_label = tk.Label(root, text="00:00", font=("Arial", 20, "bold"), fg="#e63946", bg="#fefae0")
timer_label.pack(pady=10)

root.mainloop()
