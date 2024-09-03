from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_type: str
    kaggle_competition_name: str
    local_data_file: Path
    unzip_dir: Path