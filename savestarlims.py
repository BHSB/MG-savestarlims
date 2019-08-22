import tkinter
from tkinter import messagebox

class SaveStarlims():


    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)
        self.master.title("SaveStarlims")

        self.build_grid()
        self.build_banner()
        self.build_textboxes()
        self.build_check_result('white')
        self.build_buttons()

        self.master.bind("<Scroll_Lock>", self.secret)

        self.textbox1.focus()


    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=0)
        self.mainframe.rowconfigure(2, weight=1, minsize=200)
        self.mainframe.rowconfigure(3)


    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            bg='white',
            text='Barcode Checker',
            fg='blue',
            font=('helvetica',24)
        )
        banner.grid(
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )


    def build_textboxes(self):
        textbox_frame = tkinter.Frame(self.mainframe)
        textbox_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        textbox_frame.columnconfigure(0, weight=1)
        textbox_frame.columnconfigure(1, weight=1)

        self.textbox1 = tkinter.Entry(
            textbox_frame
        )
        self.textbox2 = tkinter.Entry(
            textbox_frame
        )
        self.textbox1.grid(row=0, column=0, sticky='ew')
        self.textbox2.grid(row=0, column=1, sticky='ew')
        self.textbox2.bind("<Return>", self.check_sampleID)
        self.textbox2.bind("<Tab>", self.check_sampleID)


    def build_check_result(self, result):
        self.result_white = tkinter.Label(
            self.mainframe,
            bg='white'
        )
        self.result_green = tkinter.Label(
            self.mainframe,
            bg='green'
        )
        self.result_red = tkinter.Label(
            self.mainframe,
            bg='red'
        )
        if result == 'white':
            self.result_white.grid(
            row=2, column=0, sticky='nsew', padx=10, pady=10
            )
        elif result == 'green':
            self.result_green.grid(
            row=2, column=0, sticky='nsew', padx=10, pady=10
            )
        elif result == 'red':
            self.result_red.grid(
            row=2, column=0, sticky='nsew', padx=10, pady=10
            )


    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
        buttons_frame.columnconfigure(2, weight=1)

        self.check_button = tkinter.Button(
            buttons_frame,
            text='Check',
            command=self.check_sampleID
        )
        self.clear_button = tkinter.Button(
            buttons_frame,
            text='Clear',
            command=self.clear_text_boxes
        )
        self.exit_button = tkinter.Button(
            buttons_frame,
            text='Exit',
            command=self.exit_application
        )
        self.check_button.grid(row=0, column=0, sticky='ew')
        self.clear_button.grid(row=0, column=1, sticky='ew')
        self.exit_button.grid(row=0, column=2, sticky='ew')
        self.check_button.bind("<Return>", self.check_sampleID)
        self.clear_button.bind("<Return>", self.clear_text_boxes)
        self.exit_button.bind("<Return>", self.exit_application)


    def check_sampleID(self, *args):
        sampleID_1 = self.textbox1.get()
        sampleID_2 = self.textbox2.get()

        if sampleID_1 == "" and sampleID_2 == "":
            messagebox.showinfo('Info', "No sample ID to check")
        elif sampleID_1[:9] == sampleID_2[:9]:
            self.build_check_result('green')
        else:
            self.build_check_result('red')

        self.check_button.config(state=tkinter.DISABLED)
        self.clear_button.config(state=tkinter.NORMAL)
        self.textbox1.config(state=tkinter.DISABLED)
        self.textbox2.config(state=tkinter.DISABLED)
        self.clear_button.focus()


    def clear_text_boxes(self, *args):
        self.textbox1.config(state=tkinter.NORMAL)
        self.textbox2.config(state=tkinter.NORMAL)
        self.textbox1.delete(0, 'end')
        self.textbox2.delete(0, 'end')
        self.build_check_result('white')
        self.check_button.config(state=tkinter.NORMAL)
        self.textbox1.focus()


    def exit_application(self, *args):
        root.quit()


    def secret(self, *args):
        messagebox.showinfo('Info', "Please don't press this button again.")


if __name__ == '__main__':
    root = tkinter.Tk()
    SaveStarlims(root)
    root.mainloop()
