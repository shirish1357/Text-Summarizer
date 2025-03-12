from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
import textSummarizer.constants
# print(dir(textSummarizer.constants))  # List all available attributes
import importlib
import textSummarizer.constants
from textSummarizer.entity import DataIngestionConfig

importlib.reload(textSummarizer.constants)  # Force reload
# print(dir(textSummarizer.constants))  # Check if CONFIG_FILE_PATH is listed

from textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
# print(CONFIG_FILE_PATH)  # Verify it prints correctly

from pathlib import Path



class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = Path("/Users/shirishghimire/Desktop/Data_Scientist/Text-Summarizer/config/config.yaml"),
        params_filepath: Path = Path("/Users/shirishghimire/Desktop/Data_Scientist/Text-Summarizer/params.yaml")
    ):
        """Initializes ConfigurationManager with explicit config and params file paths."""
        
        print(f"Loading config file from: {config_filepath}")  # Debugging line
        print(f"Loading params file from: {params_filepath}")  # Debugging line
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Fetches data ingestion configuration from config.yaml."""
        
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config