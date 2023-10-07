from pathlib import Path
import urllib.request as request
import zipfile
from CNN_Classifier import logger
from CNN_Classifier.utils.common import get_size
from CNN_Classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not Path(self.config.local_data_file).exists():
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f'{filename} downloaded with following info {headers}')
        else:
            logger.info(f'Files already exists of size: {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        """
        unzip_path = Path(self.config.unzip_dir)
        unzip_path.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
