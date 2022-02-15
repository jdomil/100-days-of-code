from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Generate string of characters from valid password sources
    random_source = string.ascii_letters + string.digits + string.punctuation

    # Create list with each character type for added security and website requirements
    password_must = [choice(string.ascii_lowercase), choice(string.ascii_uppercase), choice(string.digits),
                     choice(string.punctuation)]

    # Fill list with random characters from valid characters string
    password_random = [choice(random_source) for _ in range(8)]
    password_list = password_must + password_random

    # Shuffle everything
    shuffle(password_list)

    # Turn into string
    password = "".join(password_list)

    # Insert into entry field
    password_entry.insert(END, password)

    # Copy to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get data fields from window
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Fields validation
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empy fields", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"Password: {password}\nIs it ok to save?")
        # Save and clear fields after user indicates fields are correct
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                # Clear inputs
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title = "Password Manager"
window.config(pady=50, padx=50)

# Image canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=0, column=1)

# Website section
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=39)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email/Username section
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=39)
email_entry.insert(0, "j.dominguezllata@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password section
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
