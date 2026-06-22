import pathlib
import logging
from datetime import datetime

logs_dir = pathlib.Path('logs')
logs_dir.mkdir(parents = True, exist_ok = True)

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

log_path = logs_dir / LOG_FILE

logging.basicConfig(
    level = logging.INFO,
    format = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(message)s',
    filename = log_path
)

logging.getLogger(__name__)
