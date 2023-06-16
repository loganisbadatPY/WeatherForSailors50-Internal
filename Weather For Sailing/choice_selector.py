
import tkinter as tk
from tkinter import messagebox

directory_path = "/Users/logan/Documents/Weather For Sailing"

def save_choices():
    selected_choices = [choice_var.get() for choice_var in choice_vars]
    selected_choices = [choice for choice in selected_choices if choice != 0]  # Remove unselected choices

    if len(selected_choices) == 3:
        with open(r""+directory_path+"/db/choices.txt", "w") as file:
            for i, choice_var in enumerate(choice_vars):
                if choice_var.get() != 0:
                    option_name = choices[i]
                    file.write(f"{option_name}, {choice_var.get()}\n")
        messagebox.showinfo("Success", "Choices saved successfully!")
        root.destroy()
    else:
        messagebox.showwarning("Invalid Selection", "Please select exactly three choices.")

root = tk.Tk()
root.title("Choice Selection")
root.geometry("300x250")

choices = ["Windspeed", "Tide", "Windgusts", "Current", "Weather", "Temperature"]
choice_vars = []

for i, choice in enumerate(choices):
    choice_var = tk.IntVar(value=0)  # Initialize as 0 (off)
    choice_vars.append(choice_var)

    checkbox = tk.Checkbutton(root, text=choice, variable=choice_var)
    checkbox.pack(anchor=tk.W)

save_button = tk.Button(root, text="Save", command=save_choices)
save_button.pack(pady=10)

root.mainloop()