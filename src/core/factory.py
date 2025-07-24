from typing import Any
from .base import BaseSTT
from ..utils.errors import STTError

def get_stt(model_name: str, **kwargs) -> BaseSTT:
    """
    Factory function to load STT backends.
    
    Args:
        model_name (str): Name of the STT backend (e.g., 'faster_whisper', 'vosk').
        **kwargs: Configuration parameters for the backend.
    
    Returns:
        BaseSTT: Instance of the specified STT backend.
    
    Raises:
        STTError: If the model_name is not supported.
    """
    raise STTError(f"Unknown STT model: {model_name}")