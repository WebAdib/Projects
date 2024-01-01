import qrcode
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_qr():
    data_to_encode = link_entry.get().strip()  # Get data from the link input field
    file_name = filename_entry.get().strip()  # Get file name from the filename input field

    if data_to_encode == '' or file_name == '':
        messagebox.showerror("Error", "Please enter both link and file name")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data_to_encode)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    directory = os.path.dirname(os.path.abspath(__file__))
    img.save(os.path.join(directory, file_name + ".png"))
    messagebox.showinfo("Success", f"QR code saved as {file_name}.png")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y position for the Tk root window to be centered
x = (screen_width / 2) - (600 / 2)
y = (screen_height / 2) - (600 / 2)

root.geometry(f"600x600+{int(x)}+{int(y)}")  # Set window size and position
root.configure(bg="#f0f0f0")

label_font = ("Arial", 20)
entry_font = ("Arial", 20)

# Create a custom style for rounded button
style = ttk.Style()

style.theme_use('default')

style.map('RoundedButton.TButton',
        foreground=[('pressed', 'white'), ('active', 'white')],
        background=[('pressed', '!disabled', '#4CAF50'), ('active', '#4CAF50')]
        )

style.configure('RoundedButton.TButton',
                font=label_font,
                relief='flat',
                borderwidth=0,
                border='10px',
                padding=10
                )

# Create a frame to hold the content and center it in the window
content_frame = tk.Frame(root, bg="#f0f0f0")
content_frame.pack(expand=True)

# Create input fields and labels using the custom styles
link_label = tk.Label(content_frame, text="Enter Link:", font=label_font)
link_label.pack()

link_entry = ttk.Entry(content_frame, font=entry_font)
link_entry.pack()

filename_label = tk.Label(content_frame, text="Enter File Name:", font=label_font)
filename_label.pack()

filename_entry = ttk.Entry(content_frame, font=entry_font)
filename_entry.pack()

generate_button = ttk.Button(content_frame, text="Generate QR Code", command=generate_qr, style='RoundedButton.TButton')
generate_button.pack(pady=10)

root.mainloop()
