import tkinter as tk
from tkinter import messagebox
import os


# -----------------------------
# CLASS: User
# -----------------------------
class User:
    def __init__(self, username):
        self.username = username


# -----------------------------
# CLASS: Post
# -----------------------------
class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def save_to_file(self):
        try:
            filename = f"{self.user.username}_{self.title}.txt"
            with open(filename, "w") as file:
                file.write(f"Author: {self.user.username}\n")
                file.write(f"Title: {self.title}\n\n")
                file.write(self.content)
            return filename
        except Exception as e:
            messagebox.showerror("Error", str(e))


# -----------------------------
# MAIN APPLICATION CLASS
# -----------------------------
class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog App")

        # -----------------------------
        # INPUT FIELDS
        # -----------------------------
        tk.Label(root, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1)

        tk.Label(root, text="Title").grid(row=1, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=1, column=1)

        tk.Label(root, text="Content").grid(row=2, column=0)
        self.content_text = tk.Text(root, height=10, width=30)
        self.content_text.grid(row=2, column=1)

        # -----------------------------
        # BUTTONS
        # -----------------------------
        tk.Button(root, text="Save Post", command=self.save_post).grid(row=3, column=1)

        tk.Button(root, text="Load Posts", command=self.load_posts).grid(row=4, column=1)

        # -----------------------------
        # LISTBOX (Saved Posts)
        # -----------------------------
        self.post_listbox = tk.Listbox(root, width=40)
        self.post_listbox.grid(row=5, column=0, columnspan=2)

        tk.Button(root, text="View Selected Post", command=self.view_post).grid(row=6, column=1)

    # -----------------------------
    # FUNCTION: Save Post
    # -----------------------------
    def save_post(self):
        username = self.username_entry.get()
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END).strip()

        if not username or not title or not content:
            messagebox.showwarning("Warning", "All fields are required!")
            return

        user = User(username)
        post = Post(user, title, content)

        filename = post.save_to_file()

        if filename:
            messagebox.showinfo("Success", f"Post saved as {filename}")
            self.clear_fields()
            self.load_posts()

    # -----------------------------
    # FUNCTION: Load Posts
    # -----------------------------
    def load_posts(self):
        self.post_listbox.delete(0, tk.END)

        try:
            files = [f for f in os.listdir() if f.endswith(".txt")]

            for file in files:
                self.post_listbox.insert(tk.END, file)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # -----------------------------
    # FUNCTION: View Post
    # -----------------------------
    def view_post(self):
        try:
            selected = self.post_listbox.get(self.post_listbox.curselection())

            with open(selected, "r") as file:
                content = file.read()

            messagebox.showinfo("Post Content", content)

        except IndexError:
            messagebox.showwarning("Warning", "Please select a post!")

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")

    # -----------------------------
    # FUNCTION: Clear Fields
    # -----------------------------
    def clear_fields(self):
        self.username_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)


# -----------------------------
# RUN APPLICATION
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()