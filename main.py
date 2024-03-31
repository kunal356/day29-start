from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_input.delete(first=0, last=END)
    password_input.insert(index=0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwords():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty")
    else:
        user_resp = messagebox.askokcancel(title=f"{website}",
                                           message=f"This are the details you entered:\nEmail: {email}"
                                                   f"\nPassword: {password}\nIs it ok to save?")

        if user_resp:
            save_row = " | ".join([website, email, password])
            with open(file='data.txt', mode="a") as data:
                data.write(save_row + "\n")
            # deleting text inside the inputs
            website_input.delete(first=0, last=END)
            password_input.delete(first=0, last=END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# email label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# website input
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1)

# email input
email_input = Entry(width=35)
email_input.insert(index=0, string="gaikwadkunal@gmail.com")
email_input.grid(row=2, column=1)

# password input
password_input = Entry(width=35)
password_input.grid(row=3, column=1)

# generate password button
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=3)

# add button
add_button = Button(text="Add", width=36, command=save_passwords)
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

window.mainloop()
