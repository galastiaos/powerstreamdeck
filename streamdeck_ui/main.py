import tkinter as tk

def toggle(btn_index):
    # flip the state
    states[btn_index] = 0 if states[btn_index] else 1
    buttons[btn_index].config(bg="red" if states[btn_index] else default_color)

def done():
    print(states)  # returns the array of states
    root.destroy()

def cancel():
    root.destroy()

root = tk.Tk()
root.title("Button Grid")

# black square frame
square = tk.Frame(root, bg="black", width=300, height=300)
square.pack(padx=20, pady=20)
square.pack_propagate(False)

buttons = []
states = [0]*15  # 15 buttons, all unpressed
default_color = tk.Button().cget("bg")  # system default button color

num = 1
for r in range(3):      # 3 rows
    for c in range(5):  # 5 columns
        index = num-1
        btn = tk.Button(square, text=str(num), width=4, height=2,
                        command=lambda i=index: toggle(i))
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons.append(btn)
        num += 1

# Done and Cancel buttons below the grid
ctrl_frame = tk.Frame(root)
ctrl_frame.pack(pady=10)

done_btn = tk.Button(ctrl_frame, text="Done", command=done)
done_btn.pack(side="left", padx=10)

cancel_btn = tk.Button(ctrl_frame, text="Cancel", command=cancel)
cancel_btn.pack(side="left", padx=10)

root.mainloop()
