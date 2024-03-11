from tkinter import *
from PyDictionary import PyDictionary
import requests

def search():
    text.delete('1.0', END)
    status_label.config(text="Searching...")

    word = entry.get()
    if not word:
        status_label.config(text="Please enter a word")
        return

    try:
        # Checking for internet connectivity
        requests.get("http://www.google.com", timeout=1)
    except requests.ConnectionError:
        status_label.config(text="No internet connection. Please check your connection.")
        return

    dictionary = PyDictionary()

    try:
        definition = dictionary.meaning(word)
        if definition:
            status_label.config(text=f"Definitions for '{word}':")
            for key, value in definition.items():
                text.insert(END, key + '\n\n')
                for item in value:
                    text.insert(END, f'- {item}\n\n')
        else:
            status_label.config(text=f"No definitions found for '{word}'")
    except Exception as e:
        status_label.config(text=f"An error occurred: {str(e)}. Please try again later.")

def clear_status():
    status_label.config(text="")

root = Tk()
root.title('My Dictionary')
root.geometry('800x800+50+50')
root.configure(bg="#001233")

label = Label(root, font=("Acme", 14), text="Enter A Word")
label.pack(pady=20)

entry = Entry(root, font=("Acme", 18))
entry.pack(padx=50, pady=50)

search_button = Button(root, text="Search", command=search,  font=("Acme", 14), bg="#FE3A4A")
search_button.pack(padx=10)

status_label = Label(root, text="", fg="#B2B5E0", bg="#001233", font=("Acme", 12))
status_label.pack()

# Creating the Text widget
text = Text(root, height=130, width=130, wrap=WORD, font=("Acme", 14), fg="black", bg="#B2B5E0")  
text.pack(pady=10)

# Adding a scrollbar to the Text widget
scrollbar = Scrollbar(root, command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

text.config(yscrollcommand=scrollbar.set)

clear_status_button = Button(root, text="Clear Status", command=clear_status, font=("Dancing Script", 12), bg="lightblue")
clear_status_button.pack(pady=5)

root.mainloop()
