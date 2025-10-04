# temperature_converter_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import converter_utils as cu

def convert_temperature():
    try:
        temp = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == to_unit:
            result.set(f"{temp:.2f} {from_unit} = {temp:.2f} {to_unit}")
            return

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            value = cu.celsius_to_fahrenheit(temp)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            value = cu.celsius_to_kelvin(temp)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            value = cu.fahrenheit_to_celsius(temp)
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            value = cu.fahrenheit_to_kelvin(temp)
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            value = cu.kelvin_to_celsius(temp)
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            value = cu.kelvin_to_fahrenheit(temp)
        else:
            messagebox.showerror("Error", "Invalid conversion")
            return

        result.set(f"{temp:.2f} {from_unit} = {value:.2f} {to_unit}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.resizable(False, False)

# Variables
from_var = tk.StringVar(value="Celsius")
to_var = tk.StringVar(value="Fahrenheit")
result = tk.StringVar()

# Widgets
tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
from_menu = ttk.Combobox(frame, textvariable=from_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
from_menu.grid(row=0, column=1)

tk.Label(frame, text="To:", font=("Arial", 10)).grid(row=0, column=2, padx=5)
to_menu = ttk.Combobox(frame, textvariable=to_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
to_menu.grid(row=0, column=3)

convert_btn = tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 12), bg="blue", fg="white")
convert_btn.pack(pady=10)

tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="green").pack(pady=10)

root.mainloop()
