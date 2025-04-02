import tkinter as tk
import random
import string

def generate_password():
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(18))
    password_textbox.delete(0, tk.END)
    password_textbox.insert(0, password)

def show_settings():
    settings_frame.tkraise()

def show_password_generator():
    generate_frame.tkraise()

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    if dark_mode:
        root.config(bg="#2c2f33")
        side_bar.config(bg="#23272a")
        generate_frame.config(bg="#2c2f33")
        settings_frame.config(bg="#2c2f33")
        password_label.config(bg="#2c2f33", fg="white")
        password_textbox.config(bg="#23272a", fg="white")
        generate_button.config(bg="#7289da", fg="white")
        theme_button.config(bg="#7289da", fg="white")
        back_button.config(bg="#7289da", fg="white")
    else:
        root.config(bg="white")
        side_bar.config(bg="#f0f0f0")
        generate_frame.config(bg="white")
        settings_frame.config(bg="white")
        password_label.config(bg="white", fg="black")
        password_textbox.config(bg="white", fg="black")
        generate_button.config(bg="#4CAF50", fg="black")
        theme_button.config(bg="#4CAF50", fg="black")
        back_button.config(bg="#4CAF50", fg="black")


dark_mode = True

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")


side_bar = tk.Frame(root, width=150, bg="#23272a")
side_bar.pack(side="left", fill="y")


settings_button = tk.Button(side_bar, text="Set", command=show_settings, font=("Arial", 12), bg="#7289da", fg="white", width=12, height=2)
settings_button.pack(pady=10)

password_generator_button = tk.Button(side_bar, text="Pass", command=show_password_generator, font=("Arial", 12), bg="#7289da", fg="white", width=12, height=2)
password_generator_button.pack(pady=10)


generate_frame = tk.Frame(root, bg="#2c2f33")
generate_frame.place(x=150, y=0, width=450, height=400)

password_label = tk.Label(generate_frame, text="Your password:", font=("Arial", 12), bg="#2c2f33", fg="white")
password_label.pack(pady=20)

password_textbox = tk.Entry(generate_frame, font=("Arial", 12), width=30, bg="#23272a", fg="white")
password_textbox.pack(pady=10)

generate_button = tk.Button(generate_frame, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#7289da", fg="white")
generate_button.pack(pady=10)


settings_frame = tk.Frame(root, bg="#2c2f33")
settings_frame.place(x=150, y=0, width=450, height=400)

theme_button = tk.Button(settings_frame, text="Toggle Dark/Light Mode", command=toggle_theme, font=("Arial", 12), bg="#7289da", fg="white")
theme_button.pack(pady=20)

back_button = tk.Button(settings_frame, text="Back to Generator", command=show_password_generator, font=("Arial", 12), bg="#7289da", fg="white")
back_button.pack(pady=20)


apply_theme()
generate_frame.tkraise()


root.mainloop()
