import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    # Create a table named 'users' if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT
                )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_user(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    try:
        # Insert a new user into the 'users' table
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        print(f"User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    # Check if the provided username and password match a user in the 'users' table
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    # Close the database connection
    conn.close()

    return user is not None

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login App")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self.root, text="Register", command=self.register_user).pack(pady=10)
        ttk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            add_user(username, password)
            messagebox.showinfo("Registration Successful", f"User '{username}' registered successfully.")
        else:
            messagebox.showerror("Error", "Both username and password are required.")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if authenticate_user(username, password):
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

if __name__ == "__main__":
    create_database()
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
