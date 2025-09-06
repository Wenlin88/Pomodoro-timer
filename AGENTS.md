# Repository Guidelines

## Project Structure & Module Organization
- `pomodoro/`: Core package (config, session, sound, notes, CLI, app).
  - `pomodoro/ui/`: PyQt6 widgets, dialogs, and window composition.
- `main.py`: Developer entry point for local runs.
- `icons/`, `sounds/`: Packaged assets used by the UI.
- `pyproject.toml`: Package metadata and console script (`pomodoro`).
- `config.json`: Example defaults; user config is written to `~/.pomodoro/config.json` at first run.

## Build, Test, and Development Commands
- Quick run (no clone): `uvx pomodoro`
- Setup (editable): `uv pip install -e .` (Python 3.12+)
- Run app (installed/source): `uv run pomodoro` or `uv run python main.py`
- CLI example: `uvx pomodoro --focus 45 --rest 15`
- Package (optional): `python -m build` (requires `pip install build`)

## Coding Style & Naming Conventions
- Follow PEP 8; 4-space indentation; keep lines ~88–100 chars.
- Names: modules `lower_snake_case.py`; functions/vars `snake_case`; classes `PascalCase`; constants `UPPER_SNAKE`.
- Prefer type hints and docstrings (PEP 257). Keep UI code in `pomodoro/ui/` and business logic in non-UI modules.
- No formatter mandated; Black/Ruff are welcome. Do not add new tooling without discussion.

## Testing Guidelines
- Test suite: `pytest` with tests in `tests/` (`test_*.py`).
- Run all tests: `uv run pytest`
- Focused runs: `uv run pytest -q -k config` or `-k session`
- Add small, isolated tests (e.g., `session` logging, `config` load/save). Use `tmp_path` to avoid writing to user files.
- Manual checks: launch app, run a full focus/rest cycle, verify sounds, config persistence, and Obsidian links if enabled.

## Commit & Pull Request Guidelines
- Commits: short, imperative subject (≤72 chars); explain why in the body; reference issues (e.g., `#123`) when relevant.
- Suggested prefixes: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`.
- PRs: clear description, screenshots/GIFs for UI changes, steps to validate, linked issues, and update `CHANGELOG.md` for user-visible changes.

## Security & Configuration Tips
- Do not commit personal `~/.pomodoro/config.json` or OS-specific paths.
- When adding assets to `icons/` or `sounds/`, keep filenames descriptive (e.g., `focus_end.mp3`) and load via existing utilities.
- Avoid blocking the UI thread; use timers/slots appropriately in PyQt6.
