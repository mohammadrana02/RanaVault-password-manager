from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    text = f"{web_entry.get()} | {email_entry.get()} | {password_entry.get()}"
    with open("data.txt", "a") as data:
        data.write(f"{text}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Rana's Password Manager")

logo_image = PhotoImage(file="RanaVault.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "mohammadrana02@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3)

window.mainloop()
