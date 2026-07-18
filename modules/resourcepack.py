from pathlib import Path
import json
import shutil

PACK_NAME = "Minecraft-Mod-Translator"
PACK_FORMAT = 48
PACK_DESCRIPTION = "Minecraft MOD Translator"


def build_resource_pack(
    export_dir: str | Path = "export",
    output_dir: str | Path = "resourcepack",
) -> tuple[int, int]:
    """
    exportフォルダ内のja_jp.jsonから
    Minecraft用Resource Packを生成する。

    Returns
    -------
    (コピー成功数, コピー失敗数)
    """

    export_dir = Path(export_dir)
    output_dir = Path(output_dir)

    pack_dir = output_dir / PACK_NAME

    if pack_dir.exists():
        shutil.rmtree(pack_dir)

    assets_dir = pack_dir / "assets"
    assets_dir.mkdir(parents=True)

    success = 0
    failed = 0

    for mod_dir in export_dir.iterdir():

        if not mod_dir.is_dir():
            continue

        ja_file = mod_dir / "ja_jp.json"

        if not ja_file.exists():
            continue

        target = (
            assets_dir
            / mod_dir.name.lower()
            / "lang"
            / "ja_jp.json"
        )

        target.parent.mkdir(parents=True, exist_ok=True)

        try:
            shutil.copy2(ja_file, target)
            success += 1

        except Exception as e:
            print(e)
            failed += 1

    pack_meta = {
        "pack": {
            "pack_format": PACK_FORMAT,
            "description": PACK_DESCRIPTION,
        }
    }

    with open(
        pack_dir / "pack.mcmeta",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            pack_meta,
            f,
            indent=4,
            ensure_ascii=False,
        )

    return success, failed