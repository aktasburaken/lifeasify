from tkinter import *
from tkinter import ttk
import customtkinter
from datetime import datetime
import modules.new_reminder_section

# Set the appearance mode and color theme
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Create the app
app = customtkinter.CTk()
app.geometry('720x480')
app.title("Lifeasify")

# Create the main frame
title = customtkinter.CTkLabel(app, text="All Reminders")
title.grid(row=0, column=0)

# reminder_list = ctk.CTkListbox(app)

modules.new_reminder_section.create(app)

# reminder_options.pack(side=LEFT)
# reminder_options.add_option("Add Reminder")

now = datetime.now()
# print(now.diff)

# Run the app
app.mainloop()
