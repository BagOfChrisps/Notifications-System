import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import time
import threading
from plyer import notification

events = {}
# Check notifications and reminders
def check_notifications():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        for event, details in list(events.items()):
            event_time, reminder_time = details
            if current_time == reminder_time:  # Check for reminders
                notification.notify(
                    title="🔔 Reminder",
                    message=f"Upcoming: {event} in 5 minutes!",
                    timeout=10
                )
            if current_time == event_time:  # Check for event time
                notification.notify(
                    title="⏰ Event Notification",
                    message=f"📢 It's time for: {event}\n",
                    timeout=10
                )
                del events[event]
                refresh_events_list()
                break
        time.sleep(20)

# Add an event with optional reminder
def add_event():
    event_name = event_entry.get()
    event_time = time_entry.get()
    try:
        event_dt = datetime.strptime(event_time, "%H:%M")
        reminder_dt = event_dt - timedelta(minutes=5)  # 5-minute reminder
        reminder_time = reminder_dt.strftime("%H:%M")
        events[event_name] = (event_time, reminder_time)
        refresh_events_list()
        event_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Time must be in HH:MM format.")

# Refresh event display
def refresh_events_list():
    events_list.delete(0, tk.END)
    for event, details in events.items():
        event_time, _ = details
        events_list.insert(tk.END, f"{event} - {event_time}")

# GUI setup
root = tk.Tk()
root.title("⏰ Notification App")
root.geometry("600x450")

tk.Label(root, text="Event Name:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5)
event_entry = tk.Entry(root, width=30, font=("Arial", 14))
event_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Time (HH:MM):", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5)
time_entry = tk.Entry(root, width=30, font=("Arial", 14))
time_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Set Notification", font=("Arial", 14), command=add_event).grid(row=2, column=0, columnspan=2, pady=10)

events_list = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
events_list.grid(row=3, column=0, columnspan=2, pady=10)

thread = threading.Thread(target=check_notifications, daemon=True)
thread.start()

root.mainloop()
