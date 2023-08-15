import tkinter as tk
from tkinter import messagebox
import time

# Dictionary of usernames and corresponding passwords
user_credentials = {
    "Kanha": "randua gudu",
     "Gudu": "Gudu1"
}

# Dictionary to store the last login time for each user
last_login_time = {}

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Validate that both fields are not empty
    if not username or not password:
        messagebox.showerror("Validation Error", "Both username and password are required.")
        return
    
    # Check if it's been more than 4 hours since the last login
    current_time = time.time()
    if username in last_login_time and current_time - last_login_time[username] < 4 * 60 * 60:
        messagebox.showerror("Login Error", "You can only log in once every 4 hours.")
        return
    
    # Check if the entered credentials match the stored values
    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        last_login_time[username] = current_time
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create labels and entry widgets
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Show * instead of actual password characters

# Create login button
login_button = tk.Button(root, text="Login", command=login)

# Grid layout
label_username.grid(row=0, column=0, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
