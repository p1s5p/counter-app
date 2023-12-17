import tkinter as tk

class CounterApp:
    def  __init__(self, root):
        self.root = root
        self.root.title("Counter App")

        self.counter = 0

        #create and configure widgets
        self.label = tk.Label(root, text="Counter: 0", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.increment_button = tk.Button(root, text="Increment", command=self.increment)
        self.increment_button.pack(side="left", padx=10)

        
        self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement)
        self.decrement_button.pack(side="right", padx=10)

    def increment(self):
        self.counter += 1
        self.update_label()

    def decrement(self):
        self.counter -= 1
        self.update_label()

    def update_label(self):
        self.label.config(text=f"Counter: {self.counter}")

def main():
    root = tk.Tk()
    app =CounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
