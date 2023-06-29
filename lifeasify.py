from tkinter import *
from tkinter import ttk
import customtkinter
from datetime import datetime
import modules.create

# Set the appearance mode and color theme
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# Create the app
app = customtkinter.CTk()

main_frame = customtkinter.CTkFrame(app)
already_created_reminder_frame = customtkinter.CTkFrame(app)
create_reminder_frame = customtkinter.CTkFrame(app)

modules.create.initial_page(app)

# main_frame.tkraise()

app.geometry('720x480')
app.title("Lifeasify")
# reminder_options.pack(side=LEFT)
# reminder_options.add_option("Add Reminder")

# now = datetime.now()
# print(now.diff)

# Run the app
app.mainloop()
