from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

# Explicitly define available imports
__all__ = ["CONFIG_FILE_PATH", "PARAMS_FILE_PATH"]
