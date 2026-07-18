from pathlib import Path
import zipfile

from modules.models import ModInfo


def scan_mods(folder_path: str | Path) -> list[ModInfo]:
    """
    modsフォルダを走査して
    各MODの言語ファイル情報を取得する
    """

    folder = Path(folder_path)

    mods: list[ModInfo] = []

    for jar in sorted(folder.glob("*.jar")):

        mod = ModInfo(
            name=jar.stem,
            jar_name=jar.name,
            jar_path=jar,
        )

        try:
            with zipfile.ZipFile(jar, "r") as archive:

                for filename in archive.namelist():

                    if "/lang/" in filename:

                        mod.language_count += 1

                    if filename.endswith("/lang/en_us.json"):

                        mod.has_lang = True
                        mod.lang_path = filename

        except zipfile.BadZipFile:
            print(f"壊れたjar: {jar.name}")

        mods.append(mod)

    return mods