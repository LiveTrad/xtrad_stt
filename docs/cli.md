# CLI Usage

The XTrad-STT CLI allows users to transcribe audio to text.

## Command
```bash
xtrad-stt --input audio.wav --language sw --output text.txt --vad
```

## Options
- `--input`: Input audio file or stream.
- `--language`: Language code (e.g., `sw` for Swahili).
- `--config`: Path to YAML configuration file.
- `--output`: Output text file (e.g., `text.txt`).
- `--vad`: Enable Voice Activity Detection.
- `--stream`: Enable streaming mode.