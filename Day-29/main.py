import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 0]
    symbols = ['!', '@', '$', '#', '^', '&', '*', '+', '(', ')']
    password_letters = [random.choice(letters) for i in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if web=="" or password=="":
        messagebox.showerror(message="Website or Password are empty")
    else:
        is_okay=messagebox.askokcancel(title=web, message=f" These are the details entered : \nEmail: {email} \nPassword: {password}\nIs it OK to save?")
        if is_okay:
            with open("data.txt","a") as data:
                data.write(f"{web} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(height=200, width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
#Entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "faheem@gmail.com")
password_entry=Entry(width=17)
password_entry.grid(row=3,column=1)
gen_pass_button=tkinter.Button(text="Generate Password", command=password_generator)
gen_pass_button.grid(row=3,column=2)
add_button=tkinter.Button(text="Add",width=35, command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
