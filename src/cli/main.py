import click
import asyncio
from ..core.stt.factory import get_stt
from ..config.config import load_config
from ..core.utils.logger import setup_logger
from ..core.utils.errors import STTTranscriptionError

@click.command()
@click.option("--input", required=True, help="Input audio file or stream")
@click.option("--language", default="sw", help="Language code (e.g., sw for Swahili)")
@click.option("--config", default="config/default.yaml", help="Configuration file")
@click.option("--output", default="output.txt", help="Output text file")
@click.option("--vad", is_flag=True, help="Enable Voice Activity Detection")
@click.option("--stream", is_flag=True, help="Enable streaming mode")
def transcribe(input, language, config, output, vad, stream):
    """
    Transcribe audio to text using XTrad-STT.
    """
    logger = setup_logger()
    try:
        config_data = load_config(config)
        stt = get_stt(config_data["model"], **config_data)
        
        logger.info(f"Transcribing audio: {input} (language: {language})")
        
        if stream:
            async def audio_stream():
                with open(input, "rb") as f:
                    yield f.read()
            async_gen = stt.stream_async(audio_stream(), language=language, vad_enabled=vad)
            with open(output, "w") as f:
                async for text, segments in async_gen:
                    f.write(text + "\n")
        else:
            with open(input, "rb") as f:
                audio = f.read()
            text, segments = stt.transcribe(audio, language=language, vad_enabled=vad)
            with open(output, "w") as f:
                f.write(text)
        
        logger.info(f"Transcription saved to {output}")
        click.echo(f"Transcription saved to {output}")
    except STTTranscriptionError as e:
        logger.error(f"Transcription failed: {e}")
        click.echo(f"Error: {e}", err=True)