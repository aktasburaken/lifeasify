from tkinter import *
from tkinter import ttk
import customtkinter


def create(app):
    # reminder type
    label_reminder_type = customtkinter.CTkLabel(
        app, text="Reminder Type", fg_color="transparent")
    label_reminder_type.grid(row=1, column=0, padx=10)

    reminder_types_optionMenu = customtkinter.CTkOptionMenu(
        app, values=["Do laundry", "Wash yourself", "Eat", "Sleep"])
    reminder_types_optionMenu.grid(row=2, column=0, padx=10)

    # reminder name
    label_reminder_name = customtkinter.CTkLabel(
        app, text="Reminder Name", fg_color="transparent")
    label_reminder_name.grid(row=1, column=1)

    reminder_name = customtkinter.CTkEntry(
        app, placeholder_text="New reminder...")
    reminder_name.grid(row=2, column=1)

    # submit button
    submit_button = customtkinter.CTkButton(
        app, text="Create a New Reminder", fg_color="#006D5B")
    submit_button.grid(row=2, column=2, padx=10)
