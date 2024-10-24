import tkinter as tk
from tkinter import filedialog, messagebox

def create_text_editor():
    root = tk.Tk()
    root.title("Basic Text Editor")
    text_area = tk.Text(root, wrap='word', undo=True)
    text_area.pack(expand=True, fill='both')

    def open_file():
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"),
                                                          ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                    text_area.delete(1.0, tk.END)
                    text_area.insert(tk.END, text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"),
                                                            ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    text = text_area.get(1.0, tk.END)
                    file.write(text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def close_editor():
        response = messagebox.askyesno("Exit", "Do you want to save changes before exiting?")
        if response:
            save_file()
        root.quit()

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=close_editor)

    root.bind('<Control-o>', lambda event: open_file())
    root.bind('<Control-s>', lambda event: save_file())
    root.bind('<Control-q>', lambda event: close_editor())

    root.mainloop()

if __name__ == "__main__":
    create_text_editor()
