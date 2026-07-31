from dataclasses import dataclass
from pathlib import Path

import yaml

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[2] / "config.yaml"


@dataclass(frozen=True, slots=True)
class AppConfig:
    cooldown_seconds: float


def load_app_config(path: Path | None = None) -> AppConfig:
    config_path = path or DEFAULT_CONFIG_PATH
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open(encoding="utf-8") as config_file:
        raw_config = yaml.safe_load(config_file) or {}

    cooldown_seconds = raw_config.get("cooldown_seconds", 1)
    if cooldown_seconds <= 0:
        raise ValueError("cooldown_seconds must be greater than 0")

    return AppConfig(cooldown_seconds=float(cooldown_seconds))
