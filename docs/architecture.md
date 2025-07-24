# Architecture

XTrad-STT is a modular Speech-to-Text framework with a plugin-based architecture.

## Components
- **BaseSTT**: Abstract interface for STT backends (`transcribe_async`, `transcribe`).
- **Factory**: Dynamically loads backends (e.g., Faster-Whisper, Vosk) based on configuration.
- **Configuration**: YAML-based with Pydantic validation.
- **CLI**: Command-line interface using `click`.
- **UI**: Streamlit for a user-friendly demo.

## Design Principles
- **Modularity**: Backends are pluggable via `BaseSTT`.
- **Scalability**: Supports local, cloud, and edge deployments.
- **Extensibility**: Easy to add new backends or fine-tune for languages like Swahili.