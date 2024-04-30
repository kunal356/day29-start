from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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
            new_data = {website: {"email": email, "password": password}}
            print(new_data)

            try:
                with open(file='data.json', mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file='data.json', mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open(file='data.json', mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(first=0, last=END)
                password_input.delete(first=0, last=END)
                website_input.focus()


def search_password():
    try:
        with open('data.json', 'r') as data_file:
            all_pass = json.load(data_file)
            search_key = website_input.get()
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File Not Found ")
    else:
        if search_key in all_pass:
            website = all_pass[search_key]
            print(website)
            messagebox.showinfo(title=f"{website}",
                                message=f"Email: {website['email']}"
                                        f"\nPassword: {website['password']}")
        else:
            messagebox.showinfo(title="Error",
                                message="No Records Found")


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
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1)

# email input
email_input = Entry(width=35)
email_input.insert(index=0, string="gaikwadkunal@gmail.com")
email_input.grid(row=2, column=1)

# password input
password_input = Entry(width=35)
password_input.grid(row=3, column=1)

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2)

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
