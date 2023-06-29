from tkinter import *
from tkinter import ttk
import customtkinter


def redirect_create_reminder(self, reminder_type, reminder_name):
    if (reminder_name == ""):
        # TODO: Handle this error
        print("Please enter a reminder name")
        return

    if reminder_type == "Do laundry":
        self.laundry()
        print("Do laundry")


def create(self, frame):
    # reminder type
    self.label_reminder_type = customtkinter.CTkLabel(
        frame, text="Reminder Type", fg_color="transparent")
    self.label_reminder_type.grid(row=1, column=0, padx=10)

    self.reminder_types_optionMenu = customtkinter.CTkOptionMenu(
        frame, values=["Do laundry", "Wash yourself", "Eat", "Sleep"])
    self.reminder_types_optionMenu.grid(row=2, column=0, padx=10)

    self.label_reminder_name = customtkinter.CTkLabel(
        frame, text="Reminder Name", fg_color="transparent")
    self.label_reminder_name.grid(row=1, column=1)

    self.reminder_name = customtkinter.CTkEntry(
        frame, placeholder_text="New reminder...")
    self.reminder_name.grid(row=2, column=1)

    # submit button
    submit_button = customtkinter.CTkButton(
        frame, text="Create a New Reminder", fg_color="#006D5B", command=lambda: redirect_create_reminder(self, self.reminder_types_optionMenu.get(), self.reminder_name.get())
    )
    submit_button.grid(row=2, column=2, padx=10)
