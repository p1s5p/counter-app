import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")

        self.counter = 0
        self.step = 1  # Default step for increment and decrement

        # Create and configure widgets
        self.label = tk.Label(root, text="Counter: 0", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.increment_button = tk.Button(root, text="Increment", command=self.increment)
        self.increment_button.pack(side="left", padx=10)

        self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement)
        self.decrement_button.pack(side="right", padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_counter)
        self.reset_button.pack(pady=10)

        self.step_label = tk.Label(root, text="Step:")
        self.step_label.pack(side="left")

        self.step_entry = tk.Entry(root, width=5)
        self.step_entry.pack(side="left")
        self.step_entry.insert(0, "1")  # Set default step value

        self.set_step_button = tk.Button(root, text="Set Step", command=self.set_step)
        self.set_step_button.pack(side="left")

    def increment(self):
        self.counter += self.step
        self.update_label()

    def decrement(self):
        self.counter -= self.step
        self.update_label()

    def reset_counter(self):
        self.counter = 0
        self.update_label()

    def set_step(self):
        try:
            New_step = int(self.step_entry.get())
            if new_step > 0:
                self.step = new_step
                self.update_label()
            else:
                raise ValueError("Step must be a positive integer.")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid step value. Please enter a positive integer.")

    def update_label(self):
        self.label.config(text=f"Counter: {self.counter}")

def main():
    Root = tk.Tk()
    App = CounterApp(Root)
    Root.mainloop()

if __name__ == "__main__":
    main()

