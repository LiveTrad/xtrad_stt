import pytest
from xtrad_stt.config.config import load_config, STTConfigError
from tempfile import NamedTemporaryFile
import yaml

def test_load_config():
    config_data = {
        "stt": {
            "model": "faster_whisper",
            "model_name": null,
            "device": "cuda",
            "real_time": False,
            "streaming": False,
            "vad_enabled": True,
            "language": "sw",
            "cache_enabled": False,
            "cache_redis_url": None,
            "cache_ttl": 3600,
            "log_level": "INFO",
            "log_file": "logs/xtrad_stt.log",
            "max_concurrency": 4,
            "batch_size": 1,
            "model_path": None,
            "edge_mode": False,
            "vad_sensitivity": 0.5,
            "min_speech_duration": 0.1,
            "max_speech_duration": 10.0
        }
    }
    with NamedTemporaryFile(mode="w", suffix=".yaml") as f:
        yaml.dump(config_data, f)
        config = load_config(f.name)
    assert config["model"] == "faster_whisper"
    assert config["language"] == "sw"

def test_load_invalid_config():
    with NamedTemporaryFile(mode="w", suffix=".yaml") as f:
        yaml.dump({}, f)
        with pytest.raises(STTConfigError, match="Invalid configuration"):
            load_config(f.name)