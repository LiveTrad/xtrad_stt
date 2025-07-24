import streamlit as st
from ..core.stt.factory import get_stt
from ..config.config import load_config
from ..core.utils.logger import setup_logger
from ..core.utils.errors import STTTranscriptionError

st.title("XTrad-STT: Speech-to-Text Transcription")

logger = setup_logger()

config_file = st.file_uploader("Upload YAML config", type="yaml")
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])
language = st.text_input("Language", value="sw")
vad_enabled = st.checkbox("Enable Voice Activity Detection", value=True)
stream_mode = st.checkbox("Enable Streaming")

if st.button("Transcribe"):
    try:
        config = load_config(config_file.name if config_file else "config/default.yaml")
        stt = get_stt(config["model"], **config)
        
        logger.info(f"Transcribing audio: {audio_file.name if audio_file else 'unknown'} (language: {language})")
        
        if stream_mode:
            async def audio_stream():
                yield audio_file.read()
            async_gen = stt.stream_async(audio_stream(), language=language, vad_enabled=vad_enabled)
            text, segments = [], []
            async for t, s in async_gen:
                text.append(t)
                segments.extend(s)
            text = " ".join(text)
        else:
            text, segments = stt.transcribe(audio_file.read(), language=language, vad_enabled=vad_enabled)
        
        st.text_area("Transcription", text)
        st.json(segments)
        logger.info("Transcription completed successfully")
    except STTTranscriptionError as e:
        logger.error(f"Transcription failed: {e}")
        st.error(f"Error: {e}")