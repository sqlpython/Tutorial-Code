import tkinter as tk


# Simple calculator functions

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


def calculate(operation, entry1, entry2, result_var):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        result_var.set("Enter valid numbers")
        return

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        result = "Unknown operation"

    result_var.set(str(result))


def clear_fields(entry1, entry2, result_var):
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")


def create_gui():
    root = tk.Tk()
    root.title("Calculator")
    root.resizable(False, False)
    root.geometry("320x220")

    heading = tk.Label(root, text="Simple Calculator", font=("Segoe UI", 14, "bold"))
    heading.pack(pady=(10, 5))

    frame = tk.Frame(root)
    frame.pack(padx=15, pady=5)

    tk.Label(frame, text="First number:").grid(row=0, column=0, sticky="w", pady=2)
    entry1 = tk.Entry(frame, width=20)
    entry1.grid(row=0, column=1, pady=2)

    tk.Label(frame, text="Second number:").grid(row=1, column=0, sticky="w", pady=2)
    entry2 = tk.Entry(frame, width=20)
    entry2.grid(row=1, column=1, pady=2)

    result_var = tk.StringVar()
    tk.Label(root, textvariable=result_var, font=("Segoe UI", 12), fg="blue").pack(pady=(5, 0))

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    buttons = [
        ("Add", "add"),
        ("Subtract", "subtract"),
        ("Multiply", "multiply"),
        ("Divide", "divide"),
    ]

    for idx, (label, op) in enumerate(buttons):
        btn = tk.Button(
            button_frame,
            text=label,
            width=10,
            command=lambda op=op: calculate(op, entry1, entry2, result_var),
        )
        btn.grid(row=idx // 2, column=idx % 2, padx=5, pady=5)

    clear_button = tk.Button(root, text="Clear", width=22, command=lambda: clear_fields(entry1, entry2, result_var))
    clear_button.pack(pady=(0, 10))

    root.mainloop()


if __name__ == "__main__":
    create_gui()
 
 