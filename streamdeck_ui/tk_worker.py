# streamdeck_ui/tk_worker.py
import tkinter as tk
from multiprocessing import Process, Queue
import time

def tk_worker(queue_in: Queue, queue_out: Queue):
    root = tk.Tk()
    root.withdraw()
    
    root.title("Exempt buttons from global state")
    tooltip = None
    states = [0] * 15
    last_mouse_pos = (100, 100)
    current_hover = None

    frame = tk.Frame(root, bg="black", width=300, height=300)
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    # default button color
    tmp_btn = tk.Button(frame)
    default_color = tmp_btn.cget("bg")
    tmp_btn.destroy()

    buttons = []

    # helper functions
    def update_button_color():
        for idx, btn in enumerate(buttons):
            if states[idx]:
                btn.config(bg="red", activebackground="red")
            else:
                btn.config(bg=default_color, activebackground=default_color)

    def show_tooltip(i):
        nonlocal tooltip
        hide_tooltip()
        tooltip = tk.Toplevel(root)
        tooltip.wm_overrideredirect(True)
        tooltip.attributes("-topmost", True)
        x, y = last_mouse_pos
        tooltip.wm_geometry(f"+{x+10}+{y+10}")
        label = tk.Label(tooltip, text="Exempt" if states[i] else "Not exempt",
                         bg="yellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip():
        nonlocal tooltip
        if tooltip:
            try:
                tooltip.destroy()
            except:
                pass
            tooltip = None

    def toggle(i):
        states[i] = 0 if states[i] else 1
        update_button_color()
        if current_hover == i:
            show_tooltip(i)

    # create buttons
    for idx in range(15):
        btn = tk.Button(frame, text=str(idx+1), width=4, height=2,
                        command=lambda i=idx: toggle(i))
        btn.grid(row=idx//5, column=idx%5, padx=5, pady=5)
        buttons.append(btn)

        # hover bindings
        def make_enter(i):
            def on_enter(e):
                nonlocal current_hover, last_mouse_pos
                current_hover = i
                last_mouse_pos = (e.x_root, e.y_root)
                root.after(500, lambda: show_tooltip(i))
                update_button_color()
            return on_enter

        def make_leave(i):
            def on_leave(e):
                nonlocal current_hover
                if current_hover == i:
                    current_hover = None
                hide_tooltip()
                update_button_color()
            return on_leave

        btn.bind("<Enter>", make_enter(idx))
        btn.bind("<Leave>", make_leave(idx))

    # action buttons
    ctrl_frame = tk.Frame(root)
    ctrl_frame.pack(pady=(8,12))
    def send_set():
        queue_out.put(("result", states.copy()))
    def send_cancel():
        queue_out.put(("cancel", None))

    set_btn = tk.Button(ctrl_frame, text="Set", width=8, command=send_set)
    set_btn.pack(side="left", padx=6)
    cancel_btn = tk.Button(ctrl_frame, text="Cancel", width=8, command=send_cancel)
    cancel_btn.pack(side="left", padx=6)

    # Tk periodic poll to handle messages from Qt
    def poll_queue():
        nonlocal states, last_mouse_pos, current_hover
        while not queue_in.empty():
            msg = queue_in.get_nowait()
            if msg[0] == "set_states":
                states = msg[1].copy()
                update_button_color()
                # if hover is on a button, update tooltip
                if current_hover is not None:
                    show_tooltip(current_hover)
            elif msg[0] == "user_action":
                if msg[1] == "set":
                    queue_out.put(("result", states.copy()))
                elif msg[1] == "cancel":
                    queue_out.put(("cancel", None))
        root.after(50, poll_queue)

    root.after(50, poll_queue)
    root.mainloop()


def start(queue_to_tk: Queue, queue_from_tk: Queue) -> Process:
    p = Process(target=tk_worker, args=(queue_to_tk, queue_from_tk))
    p.start()
    return p