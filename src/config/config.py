import yaml
from pydantic import BaseModel
from typing import Optional, Dict
from ..core.utils.errors import STTConfigError
from ..core.utils.logger import setup_logger

class STTConfig(BaseModel):
    model: str = "faster_whisper"
    model_name: Optional[str] = None
    device: str = "cuda"
    real_time: bool = False
    streaming: bool = False
    vad_enabled: bool = True
    language: str = "sw"
    cache_enabled: bool = False
    cache_redis_url: Optional[str] = None
    cache_ttl: int = 3600
    log_level: str = "INFO"
    log_file: str = "logs/xtrad_stt.log"
    max_concurrency: int = 4
    batch_size: int = 1
    model_path: Optional[str] = None
    edge_mode: bool = False
    vad_sensitivity: float = 0.5
    min_speech_duration: float = 0.1
    max_speech_duration: float = 10.0

def load_config(config_path: str) -> dict:
    """
    Load and validate configuration from a YAML file.
    
    Args:
        config_path (str): Path to the YAML configuration file.
    
    Returns:
        dict: Validated configuration.
    
    Raises:
        STTConfigError: If configuration is invalid.
    """
    logger = setup_logger()
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        if not config or "stt" not in config:
            raise STTConfigError("Invalid configuration: 'stt' section missing")
        return STTConfig(**config["stt"]).dict()
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        raise STTConfigError(f"Configuration error: {e}")