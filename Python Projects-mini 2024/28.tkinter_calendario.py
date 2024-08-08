import tkinter as tk
from tkcalendar import Calendar  # Corrected the import statement

def print_date():
    """
    Prints the selected date from the calendar.
    """
    selected_date = cal.get_date()
    print(f'Selected date: {selected_date}')

# Create the main application window
root = tk.Tk()
root.title('Interactive Calendar')

# Create and configure the calendar widget
cal = Calendar(root, selectmode='day', year=2024, month=5, day=16)
cal.pack(pady=20)

# Create and place the button to print the selected date
tk.Button(root, text='Select Date', command=print_date).pack(pady=20)

# Start the main event loop
root.mainloop()
