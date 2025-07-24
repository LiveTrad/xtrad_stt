# Contributing to XTrad-STT

Thank you for your interest in contributing to XTrad-STT! We welcome contributions to enhance the framework.

## How to Contribute
1. Fork the repository and create a branch.
2. Implement new STT backends in `src/xtrad_stt/core/stt/`, ensuring they inherit from `BaseSTT`.
3. Add tests in `tests/` using pytest.
4. Update documentation in `docs/` as needed.
5. Run `poetry run pre-commit run --all-files` to ensure code quality.
6. Submit a pull request with a clear description of your changes.

## Adding a New Backend
1. Create a new file in `src/xtrad_stt/core/stt/` (e.g., `my_backend.py`).
2. Implement the `BaseSTT` interface with `transcribe_async` and `stream_async`.
3. Update `factory.py` to include your backend.
4. Add tests in `tests/test_my_backend.py`.

## License
All contributions are licensed under Apache 2.0.