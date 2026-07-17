import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from modules.scanner import scan_mods


def select_mods_folder():
    folder = filedialog.askdirectory(title="modsフォルダを選択してください")

    if not folder:
        return

    folder = Path(folder)

    jars = list(folder.glob("*.jar"))

    if not jars:
        messagebox.showwarning("エラー", "このフォルダには.jarファイルがありません。")
        return

    output.delete("1.0", tk.END)

    output.insert(tk.END, f"MOD数: {len(jars)}\n\n")

    for jar in sorted(jars):
        output.insert(tk.END, jar.name + "\n")


root = tk.Tk()
root.title("Minecraft MOD Translator")
root.geometry("700x500")

button = tk.Button(
    root,
    text="modsフォルダを選択",
    command=select_mods_folder,
    height=2
)
button.pack(pady=10)

output = tk.Text(root)
output.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()