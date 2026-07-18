import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from modules.scanner import scan_mods

def select_mods_folder():
    folder = filedialog.askdirectory(title="modsフォルダを選択してください")

    if not folder:
        return

    folder = Path(folder)

    mods = scan_mods(folder)

    output.delete("1.0", tk.END)

    output.insert(tk.END, f"MOD数: {len(mods)}\n\n")

    for mod in mods:
        # ▽ 画像の指示通り、表示を詳しく豪華に修正しました
        if mod.has_lang:
            output.insert(
                tk.END,
                f"✅ {mod.name}\n"
                f"    英語ファイル : {mod.lang_path}\n"
                f"    言語数 : {mod.language_count}\n\n"
            )
        else:
            output.insert(
                tk.END,
                f"❌ {mod.name}\n"
                f"    言語ファイルなし\n\n"
            )

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