import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100
        weight = float(entry_weight.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        category_label.config(text=f"Category: {category}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values for height and weight.")

root = tk.Tk()
root.title("BMI Calculator")

label_height = tk.Label(root,
     text="Enter your height (cm):")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

label_weight = tk.Label(root,
     text="Enter your weight (kg):")
label_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

calculate_button = tk.Button(root,
         text="Calculate BMI", 
         command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

category_label = tk.Label(root, text="")
category_label.pack()

root.mainloop()