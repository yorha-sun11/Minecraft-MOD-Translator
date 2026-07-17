from pathlib import Path
import zipfile


def scan_mods(folder_path):
    """
    modsフォルダを調査し、
    各MODに en_us.json があるかを確認する。
    """

    mods = []

    folder = Path(folder_path)

    for jar in sorted(folder.glob("*.jar")):

        has_lang = False
        lang_path = None

        try:
            with zipfile.ZipFile(jar, "r") as zip_file:

                for file in zip_file.namelist():

                    if file.endswith("/lang/en_us.json"):

                        has_lang = True
                        lang_path = file
                        break

        except Exception:
            pass

        # ▽ ここから下の辞書（dict）の中身を画像の通りに変更しました
        mods.append({
            "name": jar.stem,
            "jar_name": jar.name,
            "jar_path": jar,
            "has_lang": has_lang,
            "lang_path": lang_path
        })

    return mods