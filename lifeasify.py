import tkinter
import customtkinter
import modules.create


DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Lifeasify")
        self.geometry("720x480")

        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_container.pack(
            fill=tkinter.BOTH, padx=10, pady=10)

        self.main()

    def main(self):
        self.clear_frame()
        modules.create.main_page(self, self.main_container)

    def laundry(self):
        self.clear_frame()
        modules.create.laundry_page(self, self.main_container)

    def clear_frame(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

        return self


a = App()
a.mainloop()
