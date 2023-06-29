from tkinter import *
from tkinter import ttk
import customtkinter
import modules.new_reminder_section


def initial_page(app):
    # Create the main frame
    title = customtkinter.CTkLabel(app, text="All Reminders")
    title.grid(row=0, column=0)

    # reminder_list = ctk.CTkListbox(app)
    modules.new_reminder_section.create(app)
