#entity -return type of a function

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)  # @decerator(parameter)
class DataIngestionConfig:  # dataclass
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


