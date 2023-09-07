from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog, ttk




root = Tk()

# size declare
root.geometry("700x600")
# title in main window
root.title("Untitled - Notepad")
# icons in main window
icon = ImageTk.PhotoImage(Image.open("a.png"))
root.iconphoto(True, icon)
# new page logic here


# Function to open a new window
def new_document():
    # Clear the content of the Text widget
    if ask_to_save_changes():
        text.delete(1.0, END)

def new_window():
    messagebox.showerror(title="Notification", message="This function currently now working please wait ...")
# open exits file 
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, END)
            text.insert(END, file.read())

# def new_window():
#     new_tab = Frame(notebook)
#     notebook.add(new_tab, text="New Document")

#     # Create a Text widget for the new tab
#     text_widget = Text(new_tab, wrap=WORD)
#     text_widget.pack(expand=YES, fill=BOTH)

def ask_to_save_changes():
    # Check if there are any changes in the text widget
    if text.get("1.0", "end-1c") != "":
        response = messagebox.askyesnocancel(
            "Save Changes", "Do you want to save your changes?"
        )
        if response is None:
            return False  # User clicked Cancel
        elif response is True:
            save_file()  # User clicked Yes, so save the changes
        return True  # User clicked Yes or No, so proceed
    return True  # No changes, so proceed


# this function any change in text chanege the title
def on_text_change(event=None):
    text_content = text.get("1.0", "end-1c")  # Get the text from the Text widget
    if text_content == '':
        root.title("Untitled - Notepad")
    else:
        root.title("*Untitled - Notepad")

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                text_content = text.get("1.0", END)
                file.write(text_content)
            print(f"File saved as: {file_path}")
            root.title(f"{file_path} - Notepade")
        except Exception as e:
            print(f"Error saving file: {str(e)}")



def exitquite():
    root.destroy()

# Create a Text widget for editing
text = Text(root)

# notebook = ttk.Notebook(root)
# notebook.pack(expand=YES, fill=BOTH)


# Bind the on_text_change function to the Text widget's modifications
# command here 
text.bind("<KeyRelease>", on_text_change)
# Bind Ctrl+S to the save_file function
root.bind("<Control-s>", save_file)
text.pack(expand=True, fill=BOTH)


# navigation bar
nav = Menu(root)

d1 = Menu(nav, tearoff=0)

d1.add_command(
    label="New                                      Ctrl+N", command=new_document
)
d1.add_command(label="New Window            Ctrl+Shift+N", command=new_window)
d1.add_command(label="Open...                                  Ctrl+O", command=open_file)
d1.add_command(label="Save                                       Ctrl+S", command=save_file)
d1.add_command(label="Save as                        Ctrl+Shift+S")
d1.add_command(label="Page Setup")
d1.add_command(label="Print...                                    Ctrl+P")
d1.add_command(label="Exit", command=exitquite)
root.config(menu=nav)
nav.add_cascade(label="File", menu=d1)


nav.add_command(label="Edit")
nav.add_command(label="Format")
nav.add_command(label="View")
nav.add_command(label="Help")





root.mainloop()
