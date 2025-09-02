import json
from tkinter import filedialog, messagebox

def save_file(rows, filename):
    """
    rows: list of row objects or list of dicts with keys:
          'entry_id', 'entry_speaker', 'entry_line', 'entry_function'
    filename: full path of the file to save to
    """
    data = []
    for row in rows:
        data.append({
            "entry_id": row.entry_id.get(),
            "entry_speaker": row.entry_speaker.get(),
            "entry_line": row.entry_line.get(),
            "entry_function": row.entry_function.get()
        })
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save file:\n{e}")

def load_file(filename):
    """
    Loads the file and returns list of dicts with same keys as above.
    Returns None on error.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        messagebox.showerror("Load Error", f"Failed to load file:\n{e}")
        return None

def save_as_dialog(rows):
    filename = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    if filename:
        save_file(rows, filename)
        return filename
    return None

def open_dialog():
    filename = filedialog.askopenfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    if filename:
        return filename
    return None
