from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ModInfo:
    """
    Minecraft MODの情報を保持するクラス
    """

    name: str
    jar_name: str
    jar_path: Path

    has_lang: bool = False
    lang_path: str | None = None

    language_count: int = 0