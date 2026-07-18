import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from modules.scanner import scan_mods
from modules.extractor import extract_language_files
from modules.resourcepack import build_resource_pack  # ① 一番上に追加

# スキャンしたMOD一覧を記憶しておくグローバル変数
current_mods = []


def select_mods_folder():
    global current_mods

    folder = filedialog.askdirectory(title="modsフォルダを選択してください")

    if not folder:
        return

    folder = Path(folder)

    current_mods = scan_mods(folder)

    output.delete("1.0", tk.END)

    output.insert(tk.END, f"MOD数: {len(current_mods)}\n\n")

    for mod in current_mods:
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


def extract():
    if not current_mods:
        messagebox.showwarning("警告", "先にスキャンしてください")
        return

    success, failed = extract_language_files(current_mods)

    messagebox.showinfo(
        "完了", f"{success}個抽出しました\n" f"失敗:{failed}"
    )


# ② リソースパック生成ボタンを押したときの関数を追加
def build_pack():
    success, failed = build_resource_pack()
    
    messagebox.showinfo(
        "完成",
        f"Resource Packを生成しました\n\n"
        f"成功 : {success}\n"
        f"失敗 : {failed}"
    )


# --- ここから下はGUI設定 ---
root = tk.Tk()
root.title("Minecraft MOD Translator")
root.geometry("700x500")

# スキャンボタン
button = tk.Button(
    root, text="modsフォルダを選択", command=select_mods_folder, height=2
)
button.pack(pady=10)

# 抽出ボタン
tk.Button(root, text="en_us.jsonを抽出", command=extract).pack(pady=5)

# ③ 抽出ボタンの下に「Resource Pack生成」ボタンを追加
tk.Button(root, text="Resource Pack生成", command=build_pack).pack(pady=5)

output = tk.Text(root)
output.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()