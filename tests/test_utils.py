import pytest
from xtrad_stt.core.utils.logger import setup_logger
from xtrad_stt.core.utils.cache import STTCache
from xtrad_stt.core.utils.errors import STTError

def test_logger():
    logger = setup_logger(log_level="DEBUG")
    assert logger.level == 10  # DEBUG level

def test_cache_disabled():
    cache = STTCache(enabled=False)
    assert cache.get("key") is None
    cache.set("key", b"data")
    assert cache.get("key") is None

def test_stt_error():
    with pytest.raises(STTError):
        raise STTError("Test error")