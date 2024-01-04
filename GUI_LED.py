import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

class LEDControlGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Control GUI")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Helvetica', 12))

        self.ip_label = ttk.Label(self.root, text="Enter NodeMCU IP:")
        self.ip_label.grid(row=0, column=0, padx=20, pady=20)

        self.ip_entry = ttk.Entry(self.root, width=20)
        self.ip_entry.grid(row=0, column=1, padx=20, pady=20)

        self.connect_button = ttk.Button(self.root, text="Connect", command=self.connect_to_nodemcu)
        self.connect_button.grid(row=0, column=2, padx=20, pady=20)

        self.led1_button = ttk.Button(self.root, text="Toggle Red LED", command=lambda: self.toggle_led("led1"))
        self.led1_button.grid(row=1, column=0, padx=20, pady=20)
        self.led1_button.configure(style='Red.TButton')

        self.led2_button = ttk.Button(self.root, text="Toggle Blue LED", command=lambda: self.toggle_led("led2"))
        self.led2_button.grid(row=1, column=1, padx=20, pady=20)
        self.led2_button.configure(style='Blue.TButton')

        self.led3_button = ttk.Button(self.root, text="Toggle Green LED", command=lambda: self.toggle_led("led3"))
        self.led3_button.grid(row=2, column=0, padx=20, pady=20)
        self.led3_button.configure(style='Green.TButton')

        self.led4_button = ttk.Button(self.root, text="Toggle Yellow LED", command=lambda: self.toggle_led("led4"))
        self.led4_button.grid(row=2, column=1, padx=20, pady=20)
        self.led4_button.configure(style='Yellow.TButton')

        self.create_button_styles()

    def create_button_styles(self):
        ttk.Style().configure('Red.TButton', background='red', foreground='white')
        ttk.Style().configure('Blue.TButton', background='blue', foreground='white')
        ttk.Style().configure('Green.TButton', background='green', foreground='white')
        ttk.Style().configure('Yellow.TButton', background='yellow', foreground='black')

    def connect_to_nodemcu(self):
        node_ip = self.ip_entry.get()
        if not node_ip:
            messagebox.showerror("Error", "Please enter NodeMCU IP address.")
            return

        try:
            response = requests.get(f"http://{node_ip}/")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Successfully connected to NodeMCU.")
            else:
                messagebox.showerror("Error", "Failed to connect to NodeMCU.")
        except requests.ConnectionError:
            messagebox.showerror("Error", "Failed to connect to NodeMCU.")

    def toggle_led(self, led):
        node_ip = self.ip_entry.get()
        if not node_ip:
            messagebox.showerror("Error", "Please enter NodeMCU IP address.")
            return

        try:
            response = requests.get(f"http://{node_ip}/{led}")
            if response.status_code == 200:
                messagebox.showinfo("Success", f"Successfully toggled {led}")
            else:
                messagebox.showerror("Error", f"Failed to toggle {led}")
        except requests.ConnectionError:
            messagebox.showerror("Error", "Failed to connect to NodeMCU")

if __name__ == "__main__":
    root = tk.Tk()
    app = LEDControlGUI(root)
    root.mainloop()
