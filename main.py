from tkinter import *
from tkinter import messagebox
import random
import pyperclip


#---------------------------------PASSWORD GENERATOR-----------------------#

#Password Generator Project
def generate_password():
    global password_input
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(random.randint(0,10)) ]
    password_symbols = [random.choice(symbols) for sym in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for n in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers


    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)



# ----------------------------------SAVE PASSWORD-----------------------#
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()




    if len(website) ==0 or len(username) ==0 or len(password)==0:
        messagebox.showerror(title="Error", message="Enter the Details")
        return
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the entered details:\n Website:  "
                                                              f"{website} | Username: {username} | Password: {password} ")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"Website: {website} | Username: {username} | Password: {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, columnspan=2)

# Labels and Entry Fields
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="w")
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="w")
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky="w")
username_input.insert(0, "mohammedarmaand@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")

# Make Password Entry the same width as other entries
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="w")

# Generate Password Button - Now aligned properly
password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3, column=2, sticky="w")

# Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
