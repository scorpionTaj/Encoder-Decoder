from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("TajScorpion - Message Encode and Decode")

Label(root, text='ENCODE DECODE', font='Algerian 20 bold').pack()

Text = StringVar()
private_key = StringVar()
mode_var = StringVar()  # Rename the variable to mode_var
Result = StringVar()

def encode_message_base64(key, message):
    """Encode the message using base64 encoding."""
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode_message_base64(key, message):
    """Decode the message using base64 decoding."""
    dec = []
    try:
        padding = len(message) % 4
        if padding != 0:
            message += '=' * (4 - padding)

        decoded_message = base64.urlsafe_b64decode(message).decode()
        for i in range(len(decoded_message)):
            key_c = key[i % len(key)]
            dec.append(chr((256 + ord(decoded_message[i]) - ord(key_c)) % 256))

        return "".join(dec)
    except Exception as e:
        print(f"Error decoding message: {e}")
        return "Error decoding message"

def process_mode():  # Rename the function to process_mode
    """Determine the mode of operation (encode or decode) based on the selected mode."""
    if mode_var.get() == 'e':  # Update references to mode_var
        Result.set(encode_message_base64(private_key.get(), Text.get()))
    elif mode_var.get() == 'd':  # Update references to mode_var
        Result.set(decode_message_base64(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

def exit_app():
    """Exit the application."""
    root.destroy()

def reset_fields():
    """Reset all input fields."""
    Text.set("")
    private_key.set("")
    mode_var.set("")  # Update references to mode_var
    Result.set("")

Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

Label(root, font='arial 12 bold', text='KEY').place(x=60, y=90)
Entry(root, font='arial 10', textvariable=private_key, bg='ghost white').place(x=290, y=90)

Label(root, font='arial 12 bold', text='MODE(e: encode ; d: decode)').place(x=60, y=120)
Entry(root, font='arial 10', textvariable=mode_var, bg='ghost white').place(x=290, y=120)

Entry(root, font='arial 10 bold', textvariable=Result, bg='ghost white').place(x=290, y=150)

Button(root, font='arial 10 bold', text='RESULT', padx=2, bg='LightGray', command=process_mode).place(x=60, y=150)
Button(root, font='arial 10 bold', text='RESET', width=6, bg='LimeGreen', padx=2, command=reset_fields).place(x=80, y=190)
Button(root, font='arial 10 bold', text='EXIT', width=6, bg='OrangeRed', padx=2, pady=2, command=exit_app).place(x=180, y=190)

root.mainloop()
