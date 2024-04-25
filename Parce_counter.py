import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import json
import os


class PressTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Press Tracker")
        self.data_file = 'tracker_data.json'
        self.items = self.load_data()

        # Manage Items button
        manage_items_btn = tk.Button(root, text="Manage Items", command=self.manage_items)
        manage_items_btn.pack(pady=10)

        # Reset button
        reset_btn = tk.Button(root, text="Reset All", command=self.reset_all)
        reset_btn.pack(pady=10)

        # Load items from data file
        for item_name in self.items:
            self.add_item(item_name)

    def manage_items(self):
        manage_window = tk.Toplevel(self.root)
        manage_window.title("Manage Items")

        tk.Label(manage_window, text="Add a new item:").pack(pady=(10, 5))
        new_item_name = tk.Entry(manage_window)
        new_item_name.pack(pady=5)
        tk.Button(manage_window, text="Add", command=lambda: self.add_new_item(new_item_name.get())).pack(pady=(0, 20))

        tk.Label(manage_window, text="Rename an existing item:").pack(pady=(10, 5))
        old_name = tk.Entry(manage_window)
        old_name.pack(pady=5)
        new_name = tk.Entry(manage_window)
        new_name.pack(pady=5)
        tk.Button(manage_window, text="Rename", command=lambda: self.rename_item(old_name.get(), new_name.get())).pack(pady=(0, 20))

    def add_item(self, item_name):
        # Convert item name to a Tkinter-friendly format
        frame_name = f"frame_{item_name.replace(' ', '_').lower()}"
        frame = tk.Frame(self.root, name=frame_name)
        frame.pack(padx=10, pady=5)

        label = tk.Label(frame, text=item_name)
        label.pack(side=tk.LEFT)

        press_btn = tk.Button(frame, text="+", command=lambda: self.update_press(item_name))
        press_btn.pack(side=tk.LEFT)

        day_label = tk.Label(frame, text="0 Днів з останнього парсу")
        day_label.pack(side=tk.LEFT)
        count_label = tk.Label(frame, text="0 Парсів цього місяця")
        count_label.pack(side=tk.LEFT)

        if item_name not in self.items:
            self.items[item_name] = {"last_press": None, "monthly_count": 0}

        self.items[item_name].update({"day_label": day_label, "count_label": count_label})
        self.update_labels(item_name)

    def add_new_item(self, item_name):
        if item_name and item_name not in self.items:
            self.add_item(item_name)
            self.save_data()

    def rename_item(self, old_name, new_name):
        if old_name in self.items and new_name and new_name not in self.items:
            self.items[new_name] = self.items.pop(old_name)
            self.update_labels(new_name)
            self.save_data()
            # Update UI for the renamed item
            item_frame = self.root.nametowidget(old_name)
            item_frame.config(name=new_name)
            item_frame.winfo_children()[0].config(text=new_name)

    def update_press(self, item_name):
        item = self.items[item_name]
        item["last_press"] = datetime.now().isoformat()
        item["monthly_count"] += 1
        self.save_data()
        self.update_labels(item_name)

    def update_labels(self, item_name):
        item = self.items[item_name]
        last_press = item["last_press"]
        if last_press:
            last_press_date = datetime.fromisoformat(last_press)
            days_since_press = (datetime.now() - last_press_date).days
            item["day_label"].config(text=f"{days_since_press} Днів з останнього парсу")
        item["count_label"].config(text=f"{item['monthly_count']} Парсів цього місяця")

    def reset_all(self):
        response = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset all counts?")
        if response:
            for item_name in self.items:
                self.items[item_name]["last_press"] = None
                self.items[item_name]["monthly_count"] = 0
                self.update_labels(item_name)
            self.save_data()

    def save_data(self):
        serializable_data = {key: {'last_press': value['last_press'], 'monthly_count': value['monthly_count']}
                             for key, value in self.items.items()}
        with open(self.data_file, 'w') as file:
            json.dump(serializable_data, file)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

root = tk.Tk()
app = PressTrackerApp(root)
root.mainloop()
