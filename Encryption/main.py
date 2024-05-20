from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == '1234':
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        decrypt_message = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt_message)
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    else:
        messagebox.showerror("encryption", "Invalid Password")

def encrypt():
    password = code.get()

    if password == '1234':
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt_message)
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    else:
        messagebox.showerror("encryption", "Invalid Password")

def main_screen():
    global screen
    global code
    global text1
    screen = Tk()
    screen.geometry("375x398")

    # Icon
    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    # Label
    Label(screen, text="Enter text for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)

    # Text widget
    text1 = Text(screen, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=40, width=355, height=100)

    Label(screen, text="Enter secret key for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=20, y=200)

    Button(text="ENCRYPTION", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPTION", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
