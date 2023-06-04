from tkinter import *
from tkinter import messagebox


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    text = f"{website} | {email} | {password}\n"

    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \n Email: "f"{email}"
                                                          f" \nPassword: {password} \nIs it okay to save?")

    if is_ok:
        with open("data.txt", "a") as data:
            data.write(f"{text}")

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

generate_pass_button = Button(text="Generate Password", width=30)
generate_pass_button.grid(column=1, row=4)

window.mainloop()
