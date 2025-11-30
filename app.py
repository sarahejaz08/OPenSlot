import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"resources": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

#clears main panel
def clear_main(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#Resource View
def show_resources():
    clear_main(main_frame)

    data = load_data()
    resources = data["resources"]

    title = ttk.Label(
        main_frame,
        text="Resources",
        font=("Segoe UI", 18, "bold")
    )
    title.pack(anchor="w", pady=(0, 10))

    card_container = ttk.Frame(main_frame)
    card_container.pack(fill="both", expand=True)

    if len(resources) == 0:
        empty = ttk.Label(
            card_container,
            text="No resources added yet.",
            font=("Segoe UI", 12)
        )
        empty.pack(pady=20)
        return

    for r in resources:
        card = ttk.Frame(
            card_container,
            padding=15,
            bootstyle="secondary"
        )
        card.pack(fill="x", pady=10)

        name_label = ttk.Label(card, text=r["name"], font=("Segoe UI", 14, "bold"))
        name_label.pack(anchor="w")

        desc_label = ttk.Label(card, text=r["desc"], font=("Segoe UI", 10))
        desc_label.pack(anchor="w")

def add_resource_popup():
    popup = ttk.Toplevel(app)
    popup.title("Add Resource")
    popup.geometry("350x250")
    popup.resizable(False, False)

    frame = ttk.Frame(popup, padding=20)
    frame.pack(fill="both", expand=True)

    title = ttk.Label(frame, text="Add New Resource", font=("Segoe UI", 14, "bold"))
    title.pack(pady=(0, 15))

    # Entry: Resource Name
    name_label = ttk.Label(frame, text="Resource Name:")
    name_label.pack(anchor="w")
    name_entry = ttk.Entry(frame)
    name_entry.pack(fill="x", pady=(0, 10))

    # Entry: Description
    desc_label = ttk.Label(frame, text="Description:")
    desc_label.pack(anchor="w")
    desc_entry = ttk.Entry(frame)
    desc_entry.pack(fill="x", pady=(0, 15))

    # Save button
    def save_resource():
        name = name_entry.get().strip()
        desc = desc_entry.get().strip()

        if name == "":
            ttk.Label(frame, text="Name is required!", bootstyle="danger").pack()
            return

        data = load_data()
        data["resources"].append({"name": name, "desc": desc})
        save_data(data)

        popup.destroy()
        show_resources()  # refresh main UI

    save_btn = ttk.Button(frame, text="Save", bootstyle="success", command=save_resource)
    save_btn.pack(pady=10)

# Create main window
app = ttk.Window(
    title="Open Slot",
    themename="darkly",     # clean dark theme
    size=(950, 600),
)

# -------------------------
# Sidebar (left panel)
# -------------------------
sidebar = ttk.Frame(app, padding=10)
sidebar.pack(side="left", fill="y")

sidebar.config(width=220)
sidebar.pack_propagate(False)

# App title
title_label = ttk.Label(
    sidebar,
    text="Open Slot",
    font=("Segoe UI", 20, "bold"),
    bootstyle="inverse-dark"
)
title_label.pack(pady=(0, 20))

# Sidebar buttons (text only)
btn_resources = ttk.Button(sidebar, text="Resources", bootstyle="dark", command=show_resources)
btn_resources.pack(fill="x", pady=5)

btn_add_resource = ttk.Button(sidebar, text="Add Resource", bootstyle="dark", command=add_resource_popup)
btn_add_resource.pack(fill="x", pady=5)

btn_bookings = ttk.Button(sidebar, text="Bookings", bootstyle="dark")
btn_bookings.pack(fill="x", pady=5)

btn_admin = ttk.Button(sidebar, text="Admin Panel", bootstyle="dark")
btn_admin.pack(fill="x", pady=5)

# -------------------------
# Main Content Area
# -------------------------
main_frame = ttk.Frame(app, padding=20)
main_frame.pack(side="right", expand=True, fill="both")

welcome_label = ttk.Label(
    main_frame,
    text="Welcome to Open Slot",
    font=("Segoe UI", 18)
)
welcome_label.pack(pady=20)

info_label = ttk.Label(
    main_frame,
    text="Select an option from the sidebar to begin.",
    font=("Segoe UI", 12)
)
info_label.pack()

# Start app
app.mainloop()
