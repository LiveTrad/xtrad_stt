import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_level: str = "INFO", log_file: str = "logs/xtrad_stt.log") -> logging.Logger:
    """
    Set up a centralized logger for XTrad-STT.
    
    Args:
        log_level (str): Logging level (e.g., 'DEBUG', 'INFO').
        log_file (str): Path to the log file.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("XTrad-STT")
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        logger.addHandler(console_handler)
        
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = RotatingFileHandler(log_file, maxBytes=10_000_000, backupCount=5)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        logger.addHandler(file_handler)
    
    return logger