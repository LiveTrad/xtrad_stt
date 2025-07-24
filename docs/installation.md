# Installation

## Prerequisites
- Python 3.8+
- Poetry (`pip install poetry`)
- Docker (optional, for containerized deployment)

## Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/LiveTrad/xtrad-stt.git
   cd xtrad-stt
   ```
2. Install dependencies:
   ```bash
   poetry install
   poetry shell
   ```
3. Run tests:
   ```bash
   poetry run pytest tests/
   ```
4. Run CLI:
   ```bash
   xtrad-stt --input audio.wav --language sw --output text.txt
   ```
5. Run Streamlit:
   ```bash
   poetry run streamlit run src/xtrad_stt/ui/app.py
   ```
6. Run with Docker:
   ```bash
   docker-compose up
   ```