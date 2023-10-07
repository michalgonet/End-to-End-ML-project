import os
from pathlib import Path
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = Path(log_dir) / "running_logs.log"
log_filepath.parent.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("CNN_Classifier_Logger")
