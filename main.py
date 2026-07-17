import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from modules.scanner import scan_mods  # ① 一番上にこれを追加しました

def select_mods_folder():
    folder = filedialog.askdirectory(title="modsフォルダを選択してください")

    if not folder:
        return

    folder = Path(folder)

    # ② ここから下の処理を、画像の指示通りに新しく置き換えました
    mods = scan_mods(folder)

    output.delete("1.0", tk.END)

    output.insert(tk.END, f"MOD数: {len(mods)}\n\n")

    for mod in mods:
        if mod["has_lang"]:
            output.insert(tk.END, f"✅ {mod['name']}\n    {mod['lang_path']}\n\n")
        else:
            output.insert(tk.END, f"❌ {mod['name']}\n    翻訳ファイルなし\n\n")

# --- ここから下は変更なし（元のGUI設定のまま）です ---
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