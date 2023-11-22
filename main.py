import tkinter as tk
import pytz
import datetime


def update_display():
    timezone = dropdown.get()
    current_time = datetime.datetime.now(pytz.timezone(timezone)).strftime("%H:%M:%S")
    current_date = datetime.datetime.now(pytz.timezone(timezone)).strftime("%B %d, %Y")
    day_of_week = datetime.datetime.now(pytz.timezone(timezone)).strftime("%A")
    time_label.config(text=current_time + "\n" + current_date + "\n" + day_of_week)
    time_label.after(1000, update_display)


root = tk.Tk()
root.title("Digital Watch")
root.geometry("400x200")
root.configure(bg="#7e69c9")
options = ['Europe/Moscow', 'Europe/Astrakhan', 'US/Pacific', 'Japan', 'Mexico/General', 'Europe/Brussels']
dropdown = tk.StringVar(value=options[0])
dropdown_menu = tk.OptionMenu(root, dropdown, *options)
dropdown_menu.config(bg="#98f5b1")
dropdown_menu.pack(pady=10)
time_label = tk.Label(root, font=("Arial", 30), bg="#c1b2f7")
time_label.pack(pady=10)
update_display()
root.mainloop()
