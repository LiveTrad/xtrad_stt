# Architecture

XTrad-STT is a modular Speech-to-Text framework with a plugin-based architecture.

## Components
- **BaseSTT**: Abstract interface for STT backends (`transcribe_async`, `stream_async`, `transcribe`, `stream`).
- **Factory**: Dynamically loads backends based on configuration.
- **Configuration**: YAML-based with Pydantic validation, supporting default, prod, and edge profiles.
- **CLI**: Command-line interface using `click` with streaming and VAD support.
- **UI**: Streamlit for a user-friendly demo.
- **Utilities**: Centralized logging, error handling, and optional caching.

## Design Principles
- **Modularity**: Backends are pluggable via `BaseSTT`.
- **Scalability**: Supports local (CPU/GPU), cloud (Docker), and edge (low-resource) deployments.
- **Extensibility**: Easy to add new backends or fine-tune for languages like Swahili.
- **Robustness**: Centralized logging, error handling, and caching for performance.