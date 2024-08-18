import cmath
import math
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#Define functions
def SSanalysis(Vlmag, Vlangle, Zlr, Zlj, Zt):
    Vpmag = Vlmag / math.sqrt(3)
    Vpangle = Vlangle - 30
    Va = cmath.rect(Vpmag, math.radians(Vpangle))
    Vb = cmath.rect(Vpmag, math.radians(Vpangle - 120))
    Vc = cmath.rect(Vpmag, math.radians(Vpangle - 240))

    Zl = Zlr + 1j * Zlj

    Ia = Va / (Zt + Zl)
    Ib = cmath.rect(abs(Ia), cmath.phase(Ia) - math.radians(120))
    Ic = cmath.rect(abs(Ia), cmath.phase(Ia) - math.radians(240))

    Iab = Ia
    Ibc = Ib
    Ica = Ic

    Vload = Va * (Zl / (Zt + Zl))
    Sl = 3 * Vload * np.conjugate(Ia)
    return Va, Vb, Vc, Ia, Ib, Ic, Iab, Ibc, Ica, Sl

def SDAnalysis(Vlmag, Vlangle, Zlr, Zlj, Zt):
    Vpmag = Vlmag / math.sqrt(3)
    Vpangle = Vlangle - 30
    Va = cmath.rect(Vpmag, math.radians(Vpangle))
    Vb = cmath.rect(Vpmag, math.radians(Vpangle - 120))
    Vc = cmath.rect(Vpmag, math.radians(Vpangle - 240))

    Zl = Zlr + 1j * Zlj

    Ia = Va / (Zt + (Zl / 3))
    Ib = cmath.rect(abs(Ia), cmath.phase(Ia) - math.radians(120))
    Ic = cmath.rect(abs(Ia), cmath.phase(Ia) - math.radians(240))

    Vl = cmath.rect(Vlmag, math.radians(Vlangle))
    Iab = (Vl - Zt * Ia) / Zl
    Ibc = cmath.rect(abs(Iab), cmath.phase(Iab) - math.radians(120))
    Ica = cmath.rect(abs(Iab), cmath.phase(Iab) - math.radians(240))

    Vload = Vl * (Zl / (Zt + Zl))
    Sl = 3 * Vload * np.conjugate(Iab)
    return Va, Vb, Vc, Ia, Ib, Ic, Iab, Ibc, Ica, Sl

def DSanalysis(Vlmag, Vlangle, Zlr, Zlj, Zt):
    Vpmag = Vlmag / math.sqrt(3)
    Vpangle = Vlangle - 30
    Va = cmath.rect(Vpmag, math.radians(Vpangle))
    Vb = cmath.rect(Vpmag, math.radians(Vpangle - 120))
    Vc = cmath.rect(Vpmag, math.radians(Vpangle - 240))

    Zl = Zlr + 1j * Zlj

    Ia = Va / (Zt + Zl)
    Ib = cmath.rect(abs(Ia), cmath.phase(Ia) - math.radians(120))
    Ic = cmath.rect(abs(Ia), cmath.phase(Ia) - math.radians(240))

    Iab = cmath.rect(abs(Ia)/(math.sqrt(3)), cmath.phase(Ia)+math.radians(30))
    Ibc = cmath.rect(abs(Iab), cmath.phase(Iab) - math.radians(120))
    Ica = cmath.rect(abs(Iab), cmath.phase(Iab) - math.radians(240))

    Vload = Va * (Zl / (Zt + Zl))
    Sl = 3 * Vload * np.conjugate(Ia)
    return Va, Vb, Vc, Ia, Ib, Ic, Iab, Ibc, Ica, Sl

def DDanalysis(Vlmag, Vlangle, Zlr, Zlj, Zt):
    Vpmag= Vlmag
    Vpangle=Vlangle
    Va = cmath.rect(Vpmag, math.radians(Vpangle))
    Vb = cmath.rect(Vpmag, math.radians(Vpangle - 120))
    Vc = cmath.rect(Vpmag, math.radians(Vpangle - 240))

    Zl = Zlr + 1j * Zlj

    Vload = Va * (Zl / (Zt + Zl))
    Iab= Vload/(Zl+Zt)
    Ibc = cmath.rect(abs(Iab), cmath.phase(Iab) - math.radians(120))
    Ica = cmath.rect(abs(Iab), cmath.phase(Iab) - math.radians(240))

    Ia= cmath.rect(math.sqrt(3)*abs(Iab), cmath.phase(Iab)-math.radians(30))
    Ib = cmath.rect(abs(Ia), cmath.phase(Ia) - math.radians(120))
    Ic = cmath.rect(abs(Ia), cmath.phase(Ia) - math.radians(240))

    Sl = 3 * Vload * np.conjugate(Iab)
    return Va, Vb, Vc, Ia, Ib, Ic, Iab, Ibc, Ica, Sl

def display_results(result):
    print(result)  # Add this line to print the entire result list
    result_window = tk.Toplevel(root)
    result_window.title("Results")
    result_window.geometry("600x400")

    result_text = tk.Text(result_window, font=("Arial", 12))
    result_text.pack()

    result_text.insert(tk.END, "Results:\n\n")
    result_text.insert(tk.END, f"Va: {cmath.polar(result[0])[0]:.2f} ∠ {math.degrees(cmath.polar(result[0])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Vb: {cmath.polar(result[1])[0]:.2f} ∠ {math.degrees(cmath.polar(result[1])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Vc: {cmath.polar(result[2])[0]:.2f} ∠ {math.degrees(cmath.polar(result[2])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Ia: {cmath.polar(result[3])[0]:.2f} ∠ {math.degrees(cmath.polar(result[3])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Ib: {cmath.polar(result[4])[0]:.2f} ∠ {math.degrees(cmath.polar(result[4])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Ic: {cmath.polar(result[5])[0]:.2f} ∠ {math.degrees(cmath.polar(result[5])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Iab: {cmath.polar(result[6])[0]:.2f} ∠ {math.degrees(cmath.polar(result[6])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Ibc: {cmath.polar(result[7])[0]:.2f} ∠ {math.degrees(cmath.polar(result[7])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Ica: {cmath.polar(result[8])[0]:.2f} ∠ {math.degrees(cmath.polar(result[8])[1]):.2f} degrees\n")
    result_text.insert(tk.END, f"Sl: {result[9]}\n")

def on_button_click():
    # Get user input from entry boxes
    operation_type = operation_var.get()
    Vlmag = float(Vlmag_entry.get())
    Vlangle = float(Vlangle_entry.get())
    Zlr, Zlj = map(float, Zl_entry.get().split())
    L, r = map(float, Lr_entry.get().split())
    a, b= map(float, ab_entry.get().split())
    f= float(f_entry.get())
    w= 2*math.pi*f
    Ztr = (1.724 * 10**-8) * (L / (math.pi * r**2))
    Ind= (1.2566*10**-6)/(2*math.pi)*math.log(b/a)
    Cap= (2*math.pi)/math.log(b/a)
    Zt= Ztr+ 1j*w*Ind+(1/(1j*w*Cap))
    Zt=0
    

    if operation_type == "Star-Star":
        result = SSanalysis(Vlmag, Vlangle, Zlr, Zlj, Zt)
    elif operation_type == "Star-Delta":
        result = SDAnalysis(Vlmag, Vlangle, Zlr, Zlj, Zt)
    elif operation_type == "Delta-Star":
        result= DSanalysis(Vlmag, Vlangle, Zlr, Zlj, Zt)
    elif operation_type == "Delta-Delta":
        result= DDanalysis(Vlmag, Vlangle, Zlr, Zlj, Zt)
    else:
        messagebox.showerror("Error", "Invalid operation type. Please choose either Delta-Delta, Star-Star, Delta-Star, or Star-Delta.")
        return

    # Display the results in a new window
    display_results(result)

# Create the main window
root = tk.Tk()
root.title("Three Phase System Analysis")
root.geometry("500x500")

# Create labels and entry boxes for user input
operation_label = tk.Label(root, text="Operation Type:")
operation_label.pack(pady=5)

operation_var = tk.StringVar()
operation_dropdown = ttk.Combobox(root, textvariable=operation_var, values=["Star-Star", "Star-Delta", "Delta-Delta", "Delta-Star"])
operation_dropdown.set("Star-Star")  # Default to Star-Star
operation_dropdown.pack(pady=5)

Vlmag_label = tk.Label(root, text="Magnitude of Line Voltage (V):")
Vlmag_label.pack(pady=5)
Vlmag_entry = tk.Entry(root, width=20)
Vlmag_entry.insert(0, "100")  # Default magnitude of line voltage
Vlmag_entry.pack(pady=5)

Vlangle_label = tk.Label(root, text="Phase of Line Voltage (°):")
Vlangle_label.pack(pady=5)
Vlangle_entry = tk.Entry(root, width=20)
Vlangle_entry.insert(0, "0")  # Default phase of line voltage
Vlangle_entry.pack(pady=5)

Zl_label = tk.Label(root, text="Load Impedance (Real Imag):")
Zl_label.pack(pady=5)
Zl_entry = tk.Entry(root, width=20)
Zl_entry.insert(0, "10 5")  # Default load impedance
Zl_entry.pack(pady=5)

Lr_label = tk.Label(root, text="Length and Radius of Transmission Line (m m):")
Lr_label.pack(pady=5)
Lr_entry = tk.Entry(root, width=20)
Lr_entry.insert(0, "0 0.1")  # Default length and radius of transmission line
Lr_entry.pack(pady=5)

f_label= tk.Label(root, text="What is the frequency to compute transmission line Impedance(Hz):")
f_label.pack(pady=5)
f_entry= tk.Entry(root, width=20)
f_entry.insert(0, "60")
f_entry.pack(pady=5)

ab_label= tk.Label(root, text="Inner (a) and outer (b) radius of conductor (m m):")
ab_label.pack(pady=5)
ab_entry= tk.Entry(root, width=20)
ab_entry.insert(0, "5 10")
ab_entry.pack(pady=5)

# Create a button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=on_button_click)
calculate_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()