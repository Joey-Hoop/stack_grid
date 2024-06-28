import csv
import tkinter as tk
from tkinter import ttk
from math import ceil

def display_csv_rows(file_path):
    # Create the main window
    root = tk.Tk()
    root.title("CSV Viewer")

    # Create a frame for the canvas and scrollbar
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas
    canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to work with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas to hold the CSV rows
    frame = tk.Frame(canvas, bg="#f0f0f0")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Read the CSV file and create a box for each row
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Skip the header row

        row_count = 0
        col_count = 0
        max_columns = 3

        for row in csv_reader:
            if col_count == max_columns:
                col_count = 0
                row_count += 1
            col_count += 1

            # Create a frame for each row with a background color
            if (row[1] == "Up"):
                background_color = "lime green"
            elif(row[1] == "Maintenance"):
                background_color = "gold"
            else:
                background_color = "red"
            row_frame = tk.Frame(frame, bg=background_color, borderwidth=1, relief="solid")
            row_frame.grid(row=row_count, column=col_count, padx=5, pady=5, sticky="nsew")

            # Add the name as the header in large font
            name_label = tk.Label(row_frame, text=f"ID: {row[0]}", font=("Helvetica", 16, "bold"), bg=background_color)
            name_label.pack()

            # Add the age and city underneath in smaller font
            age_label = tk.Label(row_frame, text=f"[{row[1]}]", font=("Helvetica", 12), bg=background_color)
            age_label.pack()

            city_label = tk.Label(row_frame, text=f"Last Update: {row[2]}", font=("Helvetica", 12), bg="light gray")
            city_label.pack()


    root.mainloop()
display_csv_rows("testData.csv")