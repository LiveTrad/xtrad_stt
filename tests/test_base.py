import pytest
from xtrad_stt.core.stt.base import BaseSTT

class DummySTT(BaseSTT):
    async def transcribe_async(self, audio_stream: bytes, language: str = None, vad_enabled: bool = True):
        return "dummy text", [{"text": "dummy", "start": 0, "end": 1, "confidence": 0.9}]
    
    async def stream_async(self, audio_stream, language: str = None, vad_enabled: bool = True):
        yield "dummy text", [{"text": "dummy", "start": 0, "end": 1, "confidence": 0.9}]

@pytest.mark.asyncio
async def test_base_stt_async():
    stt = DummySTT()
    text, segments = await stt.transcribe_async(b"dummy audio", language="sw", vad_enabled=True)
    assert text == "dummy text"
    assert segments[0]["text"] == "dummy"

@pytest.mark.asyncio
async def test_base_stt_stream():
    stt = DummySTT()
    async_gen = stt.stream_async([b"dummy audio"], language="sw", vad_enabled=True)
    text, segments = [t async for t, _ in async_gen][0], [s[0] async for _, s in async_gen][0]
    assert text == "dummy text"
    assert segments["text"] == "dummy"

def test_base_stt_sync():
    stt = DummySTT()
    text, segments = stt.transcribe(b"dummy audio", language="sw", vad_enabled=True)
    assert text == "dummy text"
    assert segments[0]["text"] == "dummy"