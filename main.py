import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)

    new_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
    else:
        with open("data.json", "w") as data:
            json.dump(new_data, data, indent=4)

        web_entry.delete(0, END)
        password_entry.delete(0, END)


window = Tk()
window.config(padx=50, pady=50)
window.title("Rana's Password Manager")

logo_image = PhotoImage(file="RanaVault.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=0, row=0, columnspan=2)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "mohammadrana02@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=5)

generate_pass_button = Button(text="Generate Password", width=30, command=generate_password)
generate_pass_button.grid(column=1, row=4)

window.mainloop()
