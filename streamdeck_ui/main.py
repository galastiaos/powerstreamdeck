# streamdeck_ui/main.py
import tkinter as tk

# Create a single hidden master root in the main thread
# (important: this MUST run in the process' main thread)
root_master = tk.Tk()
root_master.withdraw()

# Global state
root = None
states = [0] * 15
leave = False
result = None
buttons = []
tooltip = None
tooltip_after_ids = [None] * 15

def start_tk():
    """Create (or show) the Toplevel window for exempt buttons.
    Non-blocking: relies on the Qt side to call root_master.update() periodically.
    """
    global root, buttons, leave, tooltip, tooltip_after_ids

    # If window already exists, just deiconify and lift it
    if root is not None and tk.Toplevel.winfo_exists(root):
        try:
            root.deiconify()
            root.lift()
            return
        except Exception:
            # fall through and recreate if something's off
            try:
                root.destroy()
            except Exception:
                pass
            root = None

    leave = False
    tooltip = None
    tooltip_after_ids = [None] * 15

    root = tk.Toplevel(root_master)
    root.title("Exempt buttons from global state")
    root.protocol("WM_DELETE_WINDOW", on_close)  # user closed via window manager

    # layout
    frame = tk.Frame(root, bg="black", width=300, height=300)
    frame.pack(padx=20, pady=20)
    frame.pack_propagate(False)

    # Use a temporary button to fetch the default bg color for this platform
    tmp_btn = tk.Button(frame)
    default_color = tmp_btn.cget("bg")
    tmp_btn.destroy()
    buttons.clear()

    def toggle(i):
        states[i] = 0 if states[i] else 1
        update_button_color()

    def update_button_color():
        for idx, btn in enumerate(buttons):
            if states[idx]:
                btn.config(bg="red", activebackground="red")
            else:
                btn.config(bg=default_color, activebackground=default_color)

    def on_enter(i, event):
        # schedule tooltip after a short delay
        if tooltip_after_ids[i]:
            root.after_cancel(tooltip_after_ids[i])
            tooltip_after_ids[i] = None
        tooltip_after_ids[i] = root.after(500, lambda: show_tooltip(i, event))
        update_button_color()

    def on_leave(i, event):
        if tooltip_after_ids[i]:
            try:
                root.after_cancel(tooltip_after_ids[i])
            except Exception:
                pass
            tooltip_after_ids[i] = None
        hide_tooltip()
        update_button_color()

    def show_tooltip(i, event):
        global tooltip
        hide_tooltip()
        tooltip = tk.Toplevel(root)
        tooltip.wm_overrideredirect(True)
        tooltip.attributes("-topmost", True)
        # try/except for cases where event coordinates aren't available
        try:
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
        except Exception:
            tooltip.wm_geometry("+100+100")
        label = tk.Label(tooltip, text="Exempt" if states[i] else "Not exempt",
                         bg="yellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip():
        global tooltip
        if tooltip:
            try:
                tooltip.destroy()
            except Exception:
                pass
            tooltip = None

    # Build 3x5 button grid
    num = 1
    for r in range(3):
        for c in range(5):
            idx = num - 1
            btn = tk.Button(frame,
                            text=str(num),
                            width=4,
                            height=2,
                            command=lambda i=idx: toggle(i),
                            bg=default_color,
                            activebackground=default_color)
            btn.grid(row=r, column=c, padx=5, pady=5)
            # use lambda defaults to capture idx correctly
            btn.bind("<Enter>", lambda e, i=idx: on_enter(i, e))
            btn.bind("<Leave>", lambda e, i=idx: on_leave(i, e))
            buttons.append(btn)
            num += 1

    # action buttons (Set / Cancel)
    ctrl_frame = tk.Frame(root)
    ctrl_frame.pack(pady=(8, 12))

    def on_set():
        setexem()

    def on_cancel():
        cancexem()

    set_btn = tk.Button(ctrl_frame, text="Set", width=8, command=on_set)
    set_btn.pack(side="left", padx=6)
    cancel_btn = tk.Button(ctrl_frame, text="Cancel", width=8, command=on_cancel)
    cancel_btn.pack(side="left", padx=6)

    # Periodic poll to close window if leave is set
    def periodic_check():
        if leave:
            try:
                root.destroy()
            except Exception:
                pass
        else:
            try:
                root.after(20, periodic_check)
            except Exception:
                # if root is gone, ignore
                pass

    # start periodic_check
    try:
        root.after(20, periodic_check)
    except Exception:
        pass

def on_close():
    """Called when user closes window via window manager (X button)."""
    cancexem()

# --- SLOT FUNCTIONS CALLED BY Qt --- #

def exem():
    """Ensure the Toplevel is created/shown. Non-blocking; Qt must pump Tk events."""
    global result, leave
    result = None
    leave = False
    # Create or show the window (must be called in main thread)
    start_tk()
    return None

def setexem():
    """Mark Done (collect states)."""
    global leave, result, states
    result = states.copy()
    leave = True

def cancexem():
    """Cancel (exit without saving)."""
    global leave, result
    result = None
    leave = True

