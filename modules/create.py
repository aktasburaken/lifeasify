from tkinter import *
from tkinter import ttk
import customtkinter
import modules.new_reminder_section


def main_page(self, frame):
    # Create the main frame
    self.title = customtkinter.CTkLabel(frame, text="All Reminders")
    self.title.grid(row=0, column=0)

    # reminder_list = ctk.CTkListbox(self)
    modules.new_reminder_section.create(self, frame)


def laundry_page(self, frame):
    self.title = customtkinter.CTkLabel(frame, text="Laundry")
    self.title.grid(row=0, column=0)

    # ask total item
    self.label_item_count = customtkinter.CTkLabel(
        frame, text="How much item do you have?", fg_color="transparent")
    self.label_item_count.grid(row=1, column=0, padx=10)
    self.item_count = customtkinter.CTkEntry(
        frame, placeholder_text="For example: 5")
    self.item_count.grid(row=2, column=0)

    # ask how often they change their clothes
    self.label_change_frequency = customtkinter.CTkLabel(
        frame, text="How often do you change your clothes?", fg_color="transparent")
    self.label_change_frequency.grid(row=3, column=0, padx=10)
    self.change_frequency = customtkinter.CTkEntry(
        frame, placeholder_text="For example: 2")
    self.change_frequency.grid(row=4, column=0)

    # submit button
    submit_button = customtkinter.CTkButton(
        frame, text="Create a New Reminder", fg_color="#006D5B", command=lambda: print("test")
    )
    submit_button.grid(row=5, column=0, padx=10, pady=(10, 0))

    # back button
    def back(self, frame):
        self.clear_frame()
        main_page(self, frame)

    back_button = customtkinter.CTkButton(
        frame, text="Back", fg_color="#8F1600", command=lambda: back(self, frame)
    )
    back_button.grid(row=6, column=0, padx=10, pady=5)
