from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(row=3, column=3)

# add button
add_button = Button(text="Add", width=36, command=save_passwords)
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

window.mainloop()
