from pathlib import Path
import zipfile


def extract_lang(mod, export_root):
    """
    mod辞書から en_us.json を抽出する
    """

    if not mod["has_lang"]:
        return False

    export_root = Path(export_root)

    destination = export_root / mod["name"]
    destination.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(mod["jar_path"], "r") as zip_file:

        with zip_file.open(mod["lang_path"]) as src:

            data = src.read()

            with open(destination / "en_us.json", "wb") as dst:
                dst.write(data)

    return True