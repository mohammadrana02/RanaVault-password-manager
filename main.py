from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Rana's Password Manager")

logo_image = PhotoImage(file="RanaVault.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)


web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

add_button = Button(text="Add", width=20)
add_button.grid(column=1,row=4, columnspan=2)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3)

window.mainloop()

