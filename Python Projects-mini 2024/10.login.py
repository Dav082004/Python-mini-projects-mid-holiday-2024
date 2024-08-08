import customtkinter

# Set the appearance mode and color theme
customtkinter.set_appearance_mode('dark')  # Use dark mode for the appearance
customtkinter.set_default_color_theme('blue')  # Set the default color theme to blue

# Define sample credentials (for demonstration purposes only)
valid_username = 'root'
valid_password = 'root'

def login():
    username = entry1.get()
    password = entry2.get()

    # Validate input
    if not username or not password:
        error_label.configure(text="Please enter both username and password.", fg="red")
    elif username == valid_username and password == valid_password:
        error_label.configure(text="Login successful!", fg="green")
        print(f'Welcome, {username}')
    else:
        error_label.configure(text="Invalid username or password.", fg="red")

# Create the main application window
root = customtkinter.CTk()
root.geometry('350x300')  # Set the window size
root.title('Login')  # Set the window title

# Create a frame to hold the widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)  # Pack the frame with padding and expand it

# Create and pack the login label
label = customtkinter.CTkLabel(master=frame, text='Login', font=('Arial', 24))
label.pack(pady=12, padx=10)  # Pack the label with padding

# Create and pack the username entry
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)  # Pack the entry with padding

# Create and pack the password entry
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(pady=12, padx=10)  # Pack the entry with padding

# Create and pack the login button
button = customtkinter.CTkButton(master=frame, text='Login', command=login)  # Fixed parameter name from 'comand' to 'command'
button.pack(pady=12, padx=10)  # Pack the button with padding

# Create and pack the error label
error_label = customtkinter.CTkLabel(master=frame, text='', font=('Arial', 12))
error_label.pack(pady=12, padx=10)  # Pack the error label with padding

# Run the main application loop
root.mainloop()
