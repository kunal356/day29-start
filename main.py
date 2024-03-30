from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1)
email_input = Entry(width=35)
email_input.grid(row=2, column=1)
password_input = Entry(width=35)
password_input.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(row=3, column=3)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

window.mainloop()
