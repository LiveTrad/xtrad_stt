# XTrad-TTS

**XTrad-TTS** is a modular, extensible, and open-source Text-to-Speech (TTS) framework designed for the **LiveTrad-S2S** project. It supports multiple backends (e.g., MeloTTS, OpenVoice, Bark, Piper) and is optimized for multilingual applications, including African languages like Swahili. Licensed under **Apache 2.0**, XTrad-TTS is user-friendly with a CLI and Streamlit interface, deployable locally, in the cloud, or on edge devices, and welcomes community contributions.

## Features
- **Modular Architecture**: Pluggable TTS backends via a factory pattern.
- **Multilingual Support**: Optimized for low-resource languages (e.g., Swahili) with fine-tuning capabilities.
- **Real-Time and Batch**: Supports streaming and batch synthesis.
- **User-Friendly**: CLI for simple usage and Streamlit for a graphical interface.
- **Scalability**: Local (CPU/GPU), cloud (Docker), and edge (low-resource) deployments.
- **Open-Source**: Apache 2.0 license, hosted on GitHub and PyPI.

## Installation
```bash
pip install xtrad-tts
```

## Quick Start
```bash
xtrad-tts --input text.txt --language sw --output audio.wav
```

## Streamlit Demo
```bash
poetry run streamlit run src/xtrad_tts/ui/app.py
```

## Contributing
See [docs/contributing.md](docs/contributing.md) for guidelines on adding backends, fine-tuning, or improving documentation.

## License
Apache 2.0