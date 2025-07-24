class STTError(Exception):
    """Base exception for XTrad-STT errors."""
    pass

class STTConfigError(STTError):
    """Raised when configuration is invalid."""
    pass

class STTTranscriptionError(STTError):
    """Raised when transcription fails."""
    pass

class STTStreamError(STTError):
    """Raised when streaming fails."""
    pass