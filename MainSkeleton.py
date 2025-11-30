import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# -------------------------
#   OPEN SLOT — SKELETON
# -------------------------

#clears main panel
def clear_main(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#Resource View
def show_resources():
    clear_main(main_frame)

    # Dummy data for now
    resources = [
        {"name": "Auditorium", "desc": "Large hall for events"},
        {"name": "Computer Lab", "desc": "25 PCs — reserved for classes"},
        {"name": "Meeting Room", "desc": "Small room | 6 seats"},
    ]

    title = ttk.Label(
        main_frame,
        text="Resources",
        font=("Segoe UI", 18, "bold")
    )
    title.pack(anchor="w", pady=(0, 10))

    # Container for cards
    card_container = ttk.Frame(main_frame)
    card_container.pack(fill="both", expand=True)

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

btn_add_resource = ttk.Button(sidebar, text="Add Resource", bootstyle="dark")
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
