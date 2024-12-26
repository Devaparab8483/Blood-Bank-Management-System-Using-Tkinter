import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store data locally
DATA_FILE = "blood_donors.json"

# Function to load existing data from the file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save data to the file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a donor
def add_donor():
    name = name_entry.get()
    age = age_entry.get()
    blood_type = blood_group.get()  # Get the selected blood group
    contact = contact_entry.get()

    if not name or not age or not blood_type or not contact:
        messagebox.showerror("Validation Error", "All fields must be filled out.")
        return

    if not age.isdigit():
        messagebox.showerror("Validation Error", "Age must be a number.")
        return

    if len(contact) != 10 or not contact.isdigit():
        messagebox.showerror("Validation Error", "Contact number must be 10 digits.")
        return

    # Load existing data
    donors = load_data()

    # Add the new donor to the list
    donors.append({
        "name": name,
        "age": int(age),
        "blood_type": blood_type,
        "contact": contact
    })

    # Save updated data to the file
    save_data(donors)

    messagebox.showinfo("Success", "Donor added successfully!")
    clear_fields()

# Function to search for donors by blood type
def search_donor():
    # Get selected blood groups from checkboxes
    selected_blood_groups = [bt for bt, var in search_blood_group_vars.items() if var.get()]

    if not selected_blood_groups:
        messagebox.showerror("Validation Error", "Please select at least one blood group to search.")
        return

    # Load existing data
    donors = load_data()

    # Filter donors by the selected blood groups
    matching_donors = [donor for donor in donors if donor["blood_type"] in selected_blood_groups]

    # Display results in the non-editable text box
    result_text.configure(state="normal")  # Temporarily enable editing to update the content
    result_text.delete(1.0, tk.END)  # Clear previous results
    if matching_donors:
        for donor in matching_donors:
            result_text.insert(tk.END, f"Name: {donor['name']}, Age: {donor['age']}, Blood Type: {donor['blood_type']}, Contact: {donor['contact']}\n")
    else:
        result_text.insert(tk.END, "No donors found with the selected blood group(s).\n")
    result_text.configure(state="disabled")  # Disable editing after inserting the results

# Function to clear all input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)
    blood_group.set(None)  # Reset radio button selection

    for var in search_blood_group_vars.values():
        var.set(0)  # Reset all checkboxes

# Creating the Tkinter window
root = tk.Tk()
root.title("Blood Bank Management System")
root.geometry("800x600")
root.resizable(False, False)

BGC = "rosy brown"
root.configure(bg=BGC)

# Main frame to center widgets
main_frame = tk.Frame(root, bg=BGC, padx=20, pady=20)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Heading Title
heading = tk.Label(main_frame, text="Blood Bank Management System", font=("Elephant", 20, "bold"), bg=BGC, fg="red3")
heading.grid(row=0, column=0, columnspan=6, pady=10)

# Labels and input fields
tk.Label(main_frame, text="Donor Name", font=("Arial", 12, "bold"), bg=BGC).grid(row=1, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(main_frame, width=30)
name_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=5)

tk.Label(main_frame, text="Age", font=("Arial", 12, "bold"), bg=BGC).grid(row=2, column=0, padx=10, pady=5, sticky="w")
age_entry = tk.Entry(main_frame, width=30)
age_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

tk.Label(main_frame, text="Blood Type", font=("Arial", 12, "bold"), bg=BGC).grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Radio buttons for blood group selection
blood_group = tk.StringVar()
blood_group.set(None)  # Default value: None
blood_types = ["A+", "B+", "O+", "AB+"]  # Example blood groups

for i, bt in enumerate(blood_types):
    tk.Radiobutton(main_frame, text=bt, value=bt, variable=blood_group, bg=BGC, font=("Arial", 12, "bold"),fg="red4").grid(row=3, column=i+1, padx=5, pady=5)

tk.Label(main_frame, text="Contact", font=("Arial", 12, "bold"), bg=BGC).grid(row=4, column=0, padx=10, pady=5, sticky="w")
contact_entry = tk.Entry(main_frame, width=30)
contact_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=5)

# Buttons
add_button = tk.Button(main_frame, text="Add Donor", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", command=add_donor)
add_button.grid(row=5, column=0, columnspan=6, pady=15)

# Search section
tk.Label(main_frame, text="Search by Blood Type", font=("Arial", 12, "bold"), bg=BGC).grid(row=6, column=0, padx=10, pady=5, sticky="w")

# Checkboxes for blood groups
search_blood_group_vars = {bt: tk.IntVar() for bt in blood_types}
for i, (bt, var) in enumerate(search_blood_group_vars.items()):
    tk.Checkbutton(main_frame, text=bt, variable=var, bg=BGC, font=("Arial", 12, "bold"),fg="red4").grid(row=6, column=i+1, padx=5, pady=5)

search_button = tk.Button(main_frame, text="Search Donor", font=("Arial", 12, "bold"), bg="#2196f3", fg="white", command=search_donor)
search_button.grid(row=7, column=0, columnspan=6, pady=15)

# Display search results (non-editable)
result_text = tk.Text(main_frame, height=8, width=60, wrap="word", bg="tomato", state="disabled")
result_text.grid(row=8, column=0, columnspan=6, padx=10, pady=10)

# Clear fields button
clear_button = tk.Button(main_frame, text="Clear Fields", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=clear_fields)
clear_button.grid(row=9, column=0, columnspan=6, pady=10)

# Start the Tkinter event loop
root.mainloop()
