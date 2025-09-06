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

## Windows/Pwsh Run Notes (Agents)
- Prefer `apply_patch` for edits; avoid ad‑hoc mass text ops.
- Use PowerShell-native tools (no Bash heredocs `<<`, `nl`, `sed`). For text: `Get-Content -Raw`/`Set-Content` and `Select-String`/`-replace`.
- For quick Python, use `python -c "..."`; do not rely on shell heredocs.
- Quote/escape carefully: backtick is pwsh escape. Use single quotes or here-strings `@'...'@` for regex/Markdown.
- Handle CRLF vs LF differences; make small, contextual changes instead of brittle multi-line regex.
- Check tool availability (e.g., `rg`) before use; otherwise fall back to `Select-String`.
- Avoid non-existent cmdlets (e.g., `Apply-ContentPatch`); only the `apply_patch` tool patches files.
- Group necessary commands and avoid no-op runs to reduce wasted executions (and cost). Limit networked commands to essentials.

Common gotchas and safe patterns
- Do not use Bash heredocs: `python - << 'PY'` fails in pwsh. Use `python -c "..."`.
- Avoid GNU tools not on Windows: `nl`, `sed`, etc. Use `Get-Content`, `Set-Content`, `Select-String`.
- Escape metacharacters in args: wrap regex with single quotes; avoid unescaped `|`, `(`, `)`, `*` in pwsh strings.
- Commit messages with parentheses/pipes: pass as separate `-m` args and avoid characters that pwsh parses; or use `git commit -F` with a temp file.
- Editing Markdown fences with regex is brittle. Prefer `apply_patch` to modify specific hunks.
- CRLF/LF: avoid regex relying on newlines; operate on logical sections or exact anchors.

### uv on Windows
- Install uv: `pip install uv` or use the official installer from Astral.
- Ensure `uv.exe` is on PATH (close/reopen terminal if needed).
- Quick run without cloning: `uvx pomodoro`
- Local dev: `uv pip install -e .` then `uv run pomodoro`
- Tests: `uv pip install -e . pytest` then `uv run pytest`
