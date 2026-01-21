# main.py

import tkinter as tk
from tkinter import messagebox
from patient import Patient
from priority_queue import AdaptablePriorityQueue

queue = AdaptablePriorityQueue()


def add_patient():
    try:
        name = entry_name.get()
        age = int(entry_age.get())
        temp = float(entry_temp.get())
        bp = int(entry_bp.get())
        weight = float(entry_weight.get())

        patient = Patient(name, age, temp, bp, weight)
        queue.add_patient(patient)

        messagebox.showinfo(
            "Patient Added",
            f"Patient added successfully.\nAssigned ID: {patient.id}"
        )

        clear_fields()
        update_queue_display()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid values")


def serve_patient():
    patient = queue.serve_next_patient()
    if patient:
        messagebox.showinfo("Serving Patient", str(patient))
        update_queue_display()
    else:
        messagebox.showinfo("Queue Empty", "No patients to serve")


def update_priority():
    try:
        pid = int(entry_update_id.get())
        new_temp = float(entry_update_temp.get())
        new_bp = int(entry_update_bp.get())
        new_weight = float(entry_update_weight.get())

        success = queue.update_patient_priority(
            pid, new_temp, new_bp, new_weight
        )

        if success:
            messagebox.showinfo("Success", "Patient priority updated")
            update_queue_display()
        else:
            messagebox.showerror("Error", "Patient ID not found")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid values")


def update_queue_display():
    listbox.delete(0, tk.END)
    for patient in queue.get_all_patients():
        listbox.insert(tk.END, str(patient))


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_temp.delete(0, tk.END)
    entry_bp.delete(0, tk.END)
    entry_weight.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Hospital Priority Queue System")
root.geometry("900x650")

tk.Label(root, text="RECEPTION", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Name").grid(row=0, column=0, sticky="e")
tk.Label(frame, text="Age").grid(row=1, column=0, sticky="e")
tk.Label(frame, text="Temperature").grid(row=2, column=0, sticky="e")
tk.Label(frame, text="Blood Pressure").grid(row=3, column=0, sticky="e")
tk.Label(frame, text="Weight (kg)").grid(row=4, column=0, sticky="e")

entry_name = tk.Entry(frame)
entry_age = tk.Entry(frame)
entry_temp = tk.Entry(frame)
entry_bp = tk.Entry(frame)
entry_weight = tk.Entry(frame)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_temp.grid(row=2, column=1)
entry_bp.grid(row=3, column=1)
entry_weight.grid(row=4, column=1)

tk.Button(root, text="Add Patient", command=add_patient, bg="green", fg="white").pack(pady=10)

tk.Label(root, text="ARRIVAL AREA (WITH PATIENT IDs)", font=("Arial", 16, "bold")).pack(pady=10)

listbox = tk.Listbox(root, width=120)
listbox.pack()

tk.Button(root, text="Serve Next Patient", command=serve_patient, bg="blue", fg="white").pack(pady=10)

tk.Label(root, text="Update Patient Priority", font=("Arial", 14, "bold")).pack(pady=10)

update_frame = tk.Frame(root)
update_frame.pack()

tk.Label(update_frame, text="Patient ID").grid(row=0, column=0)
tk.Label(update_frame, text="New Temperature").grid(row=1, column=0)
tk.Label(update_frame, text="New Blood Pressure").grid(row=2, column=0)
tk.Label(update_frame, text="New Weight").grid(row=3, column=0)

entry_update_id = tk.Entry(update_frame)
entry_update_temp = tk.Entry(update_frame)
entry_update_bp = tk.Entry(update_frame)
entry_update_weight = tk.Entry(update_frame)

entry_update_id.grid(row=0, column=1)
entry_update_temp.grid(row=1, column=1)
entry_update_bp.grid(row=2, column=1)
entry_update_weight.grid(row=3, column=1)

tk.Button(root, text="Update Priority", command=update_priority, bg="orange").pack(pady=10)

root.mainloop()
