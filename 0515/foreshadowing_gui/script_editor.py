import tkinter as tk
from collections import Counter
from color_related import ENTRY_BG, MAIN_BG, color_map_dict_number_and_color_code# color_map_dict_number_and_color_code={"1": "#ffffff", ... 
import tkinter.font as tkfont
import file_handler

class Row():
    def __init__(self, master, row_num, insert_callback, delete_callback, entry_id_change_callback):
        self.master = master
        self.row_num = row_num
        self.insert_callback = insert_callback
        self.delete_callback = delete_callback

        self.frame = tk.Frame(master, bg=MAIN_BG, relief='flat')
        self.frame.grid(row=row_num, column=0, sticky="w")

        # Entry
        self.entry_id = tk.Entry(self.frame, width=2, bg=ENTRY_BG, relief='flat', insertbackground="white")
        self.entry_id.grid(row=0, column=0, padx=1)
        self.entry_id_change_callback = entry_id_change_callback
        self.entry_id.bind("<KeyRelease>", self.on_entry_id_change)

        self.entry_speaker = tk.Entry(self.frame, width=2, bg=ENTRY_BG, relief='flat', insertbackground="white")
        self.entry_speaker.grid(row=0, column=1, padx=1)

        self.entry_line = tk.Entry(self.frame, width=70, bg=ENTRY_BG, relief='flat', insertbackground="white")
        self.entry_line.grid(row=0, column=2, padx=1)
        self.entry_line.bind("<KeyRelease>", self.on_line_change)

        self.entry_function = tk.Entry(self.frame, width=30, bg=ENTRY_BG, relief='flat', insertbackground="white")
        self.entry_function.grid(row=0, column=3, padx=1)
        
        self.all_entries = [self.entry_id, self.entry_speaker, self.entry_line, self.entry_function]

        # row num
        self.label_row_num = tk.Label(self.frame, text="", width=2, anchor="e", bg=MAIN_BG)
        self.label_row_num.grid(row=0, column=4, padx=1)
        self.normal_font = tkfont.Font(font=self.label_row_num.cget("font"))
        self.bold_font = tkfont.Font(font=self.label_row_num.cget("font"))
        self.bold_font.configure(weight="bold")

        # Create right-click context menu for this row
        self.menu = tk.Menu(self.frame, tearoff=0)
        self.menu.add_command(label="Insert row above", command=self.insert_above)
        self.menu.add_command(label="Insert row below", command=self.insert_below)
        self.menu.add_command(label="Delete this row", command=self.delete_row)

        # Bind right-click event to show the menu
        self.frame.bind("<Button-3>", self.show_right_click_menu)
        for widget in self.all_entries:
            widget.bind("<Button-3>", self.show_right_click_menu)
        
        self.colorize_entry_var()

    # related to right click
    def show_right_click_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def insert_above(self):
        self.insert_callback(self.row_num)

    def insert_below(self):
        self.insert_callback(self.row_num + 1)

    def delete_row(self):
        self.delete_callback(self)


    def on_entry_id_change(self, event):
        self.colorize_entry_var()
        self.entry_id_change_callback()

    def on_line_change(self, event):
        self.entry_id_change_callback()  # call the callback to update count

    def colorize_entry_var(self):
        """colorize entry vars depend on its entry_id"""
        entry_id_val = self.entry_id.get().strip()
        if entry_id_val:
            if entry_id_val in color_map_dict_number_and_color_code:
                for i in self.all_entries:
                    i.config(fg=color_map_dict_number_and_color_code[entry_id_val])
                self.entry_id.config(bg=color_map_dict_number_and_color_code[entry_id_val], fg="black")
            elif entry_id_val.lower() == "r":
                for i in self.all_entries:
                    i.config(fg="#CC0000", bg="#2B0000")
            elif entry_id_val.lower() == "g":
                for i in self.all_entries:
                    i.config(fg="#FFFFFF", bg="#474747")
        if not entry_id_val:
            for i in self.all_entries:
                i.config(fg="#c9c9c9", bg=ENTRY_BG)



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor Example")
        self.root.configure(bg=MAIN_BG)

        # Add label to show count of non-empty entry_line entries
        self.summary_label = tk.Label(root, text="", bg=MAIN_BG, fg="#FFFFFF", font=tkfont.Font(size=9, weight="bold"))
        self.summary_label.grid(row=0, column=0, sticky="w", pady=(5, 10))

        # related to file_handler.py
        self.current_filename = None
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

        self.rows = []
        for i in range(25):
            self.add_row(i)
        
        self.update_summary()


    def add_row(self, index):
        self.rows.insert(index, Row(
            self.root, index,
            self.insert_row,
            self.delete_row,
            self.on_any_change
        ))
        self.update_rows()


    def insert_row(self, index):
        self.add_row(index)

    def delete_row(self, row_obj):
        # Destroy the frame of the row to remove it from UI
        row_obj.frame.destroy()
        # Remove from list
        self.rows.remove(row_obj)
        # Update grid to reassign row numbers and shift rows up
        self.update_rows()

    def update_rows(self):
        for i, row in enumerate(self.rows):
            row.row_num = i
            row.frame.grid(row=i+1, column=0, sticky="w")  # shifted by 1 because of label

            display_num = i + 1
            is_bold = (display_num % 5 == 0)
            
            row.label_row_num.config(
                text=str(display_num),
                font=row.bold_font if is_bold else row.normal_font,
                fg="#FFFFFF" if is_bold else "#C4C4C4"
            )

        self.update_summary()

    def update_summary(self):
        count_entry_line_non_empty = sum(1 for row in self.rows if row.entry_line.get().strip() != "")
        count_entry_id_empty       = sum(1 for row in self.rows if row.entry_line.get().strip() != "" and row.entry_id.get().strip() == "")
        count_entry_id_is_g        = sum(1 for row in self.rows if row.entry_id.get().strip() == "g")
        count_entry_id_is_r        = sum(1 for row in self.rows if row.entry_id.get().strip() == "r")

        entry_ids = [row.entry_id.get().strip() for row in self.rows if row.entry_id.get().strip() != "" and row.entry_id.get().strip() != "g" and row.entry_id.get().strip() != "r"]
        counts = Counter(entry_ids)
        count_entry_id_non_empty = sum(count - 1 for count in counts.values() if count > 1)

        total_joke = count_entry_id_non_empty + count_entry_id_is_g + count_entry_id_is_r

        self.summary_label.config(text=f"{count_entry_line_non_empty}: Total Line\n{count_entry_id_empty}: Total Non-Role Line\n{total_joke}: Total Jokes")


    def on_any_change(self):
        self.update_rows()


    # related to file_handler.py
    def save_file(self):
        if self.current_filename:
            file_handler.save_file(self.rows, self.current_filename)
        else:
            self.save_as_file()

    def save_as_file(self):
        filename = file_handler.save_as_dialog(self.rows)
        if filename:
            self.current_filename = filename

    def open_file(self):
        filename = file_handler.open_dialog()
        if not filename:
            return
        data = file_handler.load_file(filename)
        if data is None:
            return

        # Clear existing rows
        for row in self.rows:
            row.frame.destroy()
        self.rows.clear()

        # Populate rows from loaded data
        for i, row_data in enumerate(data):
            self.add_row(i)
            row = self.rows[i]
            row.entry_id.delete(0, tk.END)
            row.entry_id.insert(0, row_data.get('entry_id', ''))
            row.entry_speaker.delete(0, tk.END)
            row.entry_speaker.insert(0, row_data.get('entry_speaker', ''))
            row.entry_line.delete(0, tk.END)
            row.entry_line.insert(0, row_data.get('entry_line', ''))
            row.entry_function.delete(0, tk.END)
            row.entry_function.insert(0, row_data.get('entry_function', ''))

            # Call colorize explicitly after loading entry_id
            row.colorize_entry_var()

        self.current_filename = filename
        self.update_rows()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
