import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Convert LANGUAGES dictionary to a sorted list of language names
language_names = sorted(LANGUAGES.values())

# Reverse map: name to code
lang_name_to_code = {v: k for k, v in LANGUAGES.items()}

def translate_text():
    src_lang_name = src_lang_combo.get()
    tgt_lang_name = tgt_lang_combo.get()
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Input Needed", "Please enter text to translate.")
        return

    try:
        translated = translator.translate(text, src=lang_name_to_code[src_lang_name],
                                                 dest=lang_name_to_code[tgt_lang_name])
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Simple Language Translator")
root.geometry("600x400")

# Input text
tk.Label(root, text="Enter text:").pack()
input_text = tk.Text(root, height=5)
input_text.pack()

# Language selection
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:").grid(row=0, column=0, padx=5)
src_lang_combo = ttk.Combobox(frame, values=language_names)
src_lang_combo.set("english")
src_lang_combo.grid(row=0, column=1)

tk.Label(frame, text="To:").grid(row=0, column=2, padx=5)
tgt_lang_combo = ttk.Combobox(frame, values=language_names)
tgt_lang_combo.set("french")
tgt_lang_combo.grid(row=0, column=3)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Output text
tk.Label(root, text="Translated text:").pack()
output_text = tk.Text(root, height=5)
output_text.pack()

root.mainloop()
