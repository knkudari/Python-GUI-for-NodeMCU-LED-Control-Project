import tkinter as tk
from tkinter import ttk
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

        self.led1_button = ttk.Button(self.root, text="Toggle LED 1", command=self.toggle_led1)
        self.led1_button.grid(row=0, column=0, padx=20, pady=20)

        self.led2_button = ttk.Button(self.root, text="Toggle LED 2", command=self.toggle_led2)
        self.led2_button.grid(row=0, column=1, padx=20, pady=20)

        self.led3_button = ttk.Button(self.root, text="Toggle LED 3", command=self.toggle_led3)
        self.led3_button.grid(row=1, column=0, padx=20, pady=20)

        self.led4_button = ttk.Button(self.root, text="Toggle LED 4", command=self.toggle_led4)
        self.led4_button.grid(row=1, column=1, padx=20, pady=20)

    def toggle_led1(self):
        self.toggle_led("led1")

    def toggle_led2(self):
        self.toggle_led("led2")

    def toggle_led3(self):
        self.toggle_led("led3")

    def toggle_led4(self):
        self.toggle_led("led4")

    def toggle_led(self, led):
        try:
            response = requests.get(f"http://<your_nodemcu_ip>/{led}")
            if response.status_code == 200:
                print(f"Successfully toggled {led}")
            else:
                print(f"Failed to toggle {led}")
        except requests.ConnectionError:
            print("Failed to connect to NodeMCU")

if __name__ == "__main__":
    root = tk.Tk()
    app = LEDControlGUI(root)
    root.mainloop()
