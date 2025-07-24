# Configuration

XTrad-STT uses YAML configuration files for flexible setup. Multiple profiles are provided: `default.yaml` (development), `prod.yaml` (cloud), and `edge.yaml` (low-resource devices).

## Example Configuration
```yaml
stt:
  model: faster_whisper
  model_name: null
  device: cuda
  real_time: false
  streaming: false
  vad_enabled: true
  language: sw
  cache_enabled: false
  cache_redis_url: null
  cache_ttl: 3600
  log_level: INFO
  log_file: logs/xtrad_stt.log
  max_concurrency: 4
  batch_size: 1
  model_path: null
  edge_mode: false
  vad_sensitivity: 0.5
  min_speech_duration: 0.1
  max_speech_duration: 10.0
```

## Parameters
- `model`: STT backend (e.g., `faster_whisper`, `vosk`, `nemo`).
- `model_name`: Specific model identifier (e.g., `livetrad/faster-whisper-swahili`).
- `device`: Hardware device (`cpu`, `cuda`).
- `real_time`: Enable real-time transcription.
- `streaming`: Enable streaming mode.
- `vad_enabled`: Enable Voice Activity Detection.
- `language`: Language code (e.g., `sw` for Swahili).
- `cache_enabled`: Enable caching for performance.
- `cache_redis_url`: Redis URL for caching.
- `cache_ttl`: Cache time-to-live in seconds.
- `log_level`: Logging level (`DEBUG`, `INFO`, `ERROR`).
- `log_file`: Path to log file.
- `max_concurrency`: Maximum concurrent transcription tasks.
- `batch_size`: Batch size for processing.
- `model_path`: Local path to model weights (optional).
- `edge_mode`: Optimize for low-resource devices.
- `vad_sensitivity`: VAD sensitivity (0.0 to 1.0).
- `min_speech_duration`: Minimum speech duration for VAD (seconds).
- `max_speech_duration`: Maximum speech duration for VAD (seconds).