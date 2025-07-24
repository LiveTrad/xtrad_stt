from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, AsyncGenerator, Tuple, List
from ..utils.errors import STTError

class BaseSTT(ABC):
    """Abstract base class for STT backends."""
    
    @abstractmethod
    async def transcribe_async(self, audio_stream: bytes, language: str = None, 
                              vad_enabled: bool = True) -> Tuple[str, List[Dict]]:
        """
        Transcribe audio stream asynchronously.
        
        Args:
            audio_stream (bytes): Audio input as bytes.
            language (str, optional): Language code (e.g., 'sw' for Swahili).
            vad_enabled (bool): Enable Voice Activity Detection.
        
        Returns:
            Tuple[str, List[Dict]]: Transcribed text and segments (e.g., timestamps, confidence).
        
        Raises:
            STTError: If transcription fails.
        """
        pass
    
    @abstractmethod
    async def stream_async(self, audio_stream: AsyncGenerator[bytes, None], language: str = None, 
                          vad_enabled: bool = True) -> AsyncGenerator[Tuple[str, List[Dict]], None]:
        """
        Stream transcription results asynchronously for real-time use.
        
        Args:
            audio_stream (AsyncGenerator[bytes, None]): Stream of audio chunks.
            language (str, optional): Language code.
            vad_enabled (bool): Enable Voice Activity Detection.
        
        Yields:
            Tuple[str, List[Dict]]: Partial transcription and segments.
        
        Raises:
            STTError: If streaming fails.
        """
        pass
    
    def transcribe(self, audio_stream: bytes, language: str = None, vad_enabled: bool = True) -> Tuple[str, List[Dict]]:
        """
        Synchronous transcription for non real-time use.
        
        Args:
            audio_stream (bytes): Audio input as bytes.
            language (str, optional): Language code.
            vad_enabled (bool): Enable Voice Activity Detection.
        
        Returns:
            Tuple[str, List[Dict]]: Transcribed text and segments.
        
        Raises:
            STTError: If transcription fails.
        """
        import asyncio
        return asyncio.run(self.transcribe_async(audio_stream, language, vad_enabled))
    
    def stream(self, audio_stream: bytes, language: str = None, vad_enabled: bool = True) -> Any:
        """
        Synchronous streaming for non real-time use.
        
        Args:
            audio_stream (bytes): Audio input as bytes.
            language (str, optional): Language code.
            vad_enabled (bool): Enable Voice Activity Detection.
        
        Returns:
            Any: Generator of transcription results.
        
        Raises:
            STTError: If streaming fails.
        """
        import asyncio
        async_gen = self.stream_async([audio_stream], language, vad_enabled)
        return asyncio.run(async_gen.__anext__())