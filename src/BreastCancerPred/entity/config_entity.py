from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    all_schema: dict
    STATUS_FILE: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    X_train_path: Path
    Y_train_path: Path
    model_name: str

@dataclass
class ModelEValuationConfig:
    root_dir: Path 
    X_test_path: Path
    Y_test_path: Path
    model_path: Path