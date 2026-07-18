from pathlib import Path
import shutil
import zipfile

from modules.models import ModInfo


def extract_language_files(
    mods: list[ModInfo],
    export_dir: str | Path = "export"
) -> tuple[int, int]:
    """
    en_us.jsonをexportフォルダへ抽出する

    Returns
    -------
    (成功数, 失敗数)
    """

    export_path = Path(export_dir)

    if export_path.exists():
        shutil.rmtree(export_path)

    export_path.mkdir()

    success = 0
    failed = 0

    for mod in mods:

        if not mod.has_lang:
            continue

        try:

            with zipfile.ZipFile(mod.jar_path, "r") as jar:

                destination = (
                    export_path
                    / mod.name
                    / "en_us.json"
                )

                destination.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                with jar.open(mod.lang_path) as source:

                    destination.write_bytes(source.read())

            success += 1

        except Exception as e:

            print(e)
            failed += 1

    return success, failed