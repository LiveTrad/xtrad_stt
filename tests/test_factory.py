import pytest
from xtrad_stt.core.stt.factory import get_stt
from xtrad_stt.core.utils.errors import STTError

def test_get_stt_invalid():
    with pytest.raises(STTError, match="Unknown STT model: invalid"):
        get_stt("invalid")